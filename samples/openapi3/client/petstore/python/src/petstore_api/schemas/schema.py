from __future__ import annotations
import datetime
import dataclasses
import io
import types
import typing
import uuid

import immutabledict
import typing_extensions

from petstore_api import exceptions
from petstore_api.configurations import schema_configuration

from . import validation

none_type_ = type(None)
T = typing.TypeVar('T')
U = typing.TypeVar('U')

class SchemaTyped:
    additional_properties: typing.Type[Schema]
    all_of: typing.Tuple[typing.Type[Schema], ...]
    any_of: typing.Tuple[typing.Type[Schema], ...]
    discriminator: typing.Mapping[str, typing.Mapping[str, typing.Type[Schema]]]
    default: typing.Union[str, int, float, bool, None]
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, bool, None], str]
    exclusive_maximum: typing.Union[int, float]
    exclusive_minimum: typing.Union[int, float]
    format: str
    inclusive_maximum: typing.Union[int, float]
    inclusive_minimum: typing.Union[int, float]
    items: typing.Type[Schema]
    max_items: int
    max_length: int
    max_properties: int
    min_items: int
    min_length: int
    min_properties: int
    multiple_of: typing.Union[int, float]
    not_: typing.Type[Schema]
    one_of: typing.Tuple[typing.Type[Schema], ...]
    pattern: validation.PatternInfo
    properties: typing.Mapping[str, typing.Type[Schema]]
    required: typing.FrozenSet[str]
    types: typing.FrozenSet[typing.Type]
    unique_items: bool


class FileIO(io.FileIO):
    """
    A class for storing files
    Note: this class is not immutable
    """

    def __new__(cls, arg: typing.Union[io.FileIO, io.BufferedReader]):
        if isinstance(arg, (io.FileIO, io.BufferedReader)):
            if arg.closed:
                raise exceptions.ApiValueError('Invalid file state; file is closed and must be open')
            arg.close()
            super_cls: typing.Type = super(FileIO, cls)
            inst = super_cls.__new__(cls, arg.name)
            super(FileIO, inst).__init__(arg.name)
            return inst
        raise exceptions.ApiValueError('FileIO must be passed arg which contains the open file')

    def __init__(self, arg: typing.Union[io.FileIO, io.BufferedReader]):
        """
        Needed for instantiation when passing in arguments of the above type
        """
        pass


def cast_to_allowed_types(
    arg: typing.Union[
        dict,
        immutabledict.immutabledict,
        list,
        tuple,
        float,
        int,
        str,
        datetime.date,
        datetime.datetime,
        uuid.UUID,
        bool,
        None,
        bytes,
        io.FileIO,
        io.BufferedReader,
        'Schema',
    ],
    from_server: bool,
    validated_path_to_schemas: typing.Dict[typing.Tuple[typing.Union[str, int], ...], typing.Set[typing.Union['Schema', str, int, float, bool, None, immutabledict.immutabledict, tuple]]],
    path_to_item: typing.Tuple[typing.Union[str, int], ...],
    path_to_type: typing.Dict[typing.Tuple[typing.Union[str, int], ...], typing.Type]
) -> typing.Union[
    immutabledict.immutabledict,
    tuple,
    float,
    int,
    str,
    bytes,
    bool,
    None,
    FileIO]:
    """
    Casts the input payload arg into the allowed types
    The input validated_path_to_schemas is mutated by running this function

    When from_server is False then
    - date/datetime is cast to str
    - int/float is cast to Decimal

    If a Schema instance is passed in it is converted back to a primitive instance because
    One may need to validate that data to the original Schema class AND additional different classes
    those additional classes will need to be added to the new manufactured class for that payload
    If the code didn't do this and kept the payload as a Schema instance it would fail to validate to other
    Schema classes and the code wouldn't be able to mfg a new class that includes all valid schemas
    TODO: store the validated schema classes in validation_metadata

    Args:
        arg: the payload
        from_server: whether this payload came from the server or not
        validated_path_to_schemas: a dict that stores the validated classes at any path location in the payload
    """
    type_error = exceptions.ApiTypeError(f"Invalid type. Required value type is str and passed type was {type(arg)} at {path_to_item}")
    if isinstance(arg, str):
        path_to_type[path_to_item] = str
        return str(arg)
    elif isinstance(arg, (dict, immutabledict.immutabledict)):
        path_to_type[path_to_item] = immutabledict.immutabledict
        return immutabledict.immutabledict(
            {
                key: cast_to_allowed_types(
                    val,
                    from_server,
                    validated_path_to_schemas,
                    path_to_item + (key,),
                    path_to_type,
                )
                for key, val in arg.items()
            }
        )
    elif isinstance(arg, bool):
        path_to_type[path_to_item] = bool
        """
        this check must come before isinstance(arg, (int, float))
        because isinstance(True, int) is True
        """
        if arg:
            return True
        return False
    elif isinstance(arg, int):
        path_to_type[path_to_item] = int
        return arg
    elif isinstance(arg, float):
        path_to_type[path_to_item] = float
        return arg
    elif isinstance(arg, (tuple, list)):
        path_to_type[path_to_item] = tuple
        return tuple(
            [
                cast_to_allowed_types(
                    item,
                    from_server,
                    validated_path_to_schemas,
                    path_to_item + (i,),
                    path_to_type,
                )
                for i, item in enumerate(arg)
            ]
        )
    elif isinstance(arg, none_type_):
        path_to_type[path_to_item] = none_type_
        return None
    elif isinstance(arg, (datetime.date, datetime.datetime)):
        path_to_type[path_to_item] = str
        if not from_server:
            return arg.isoformat()
        raise type_error
    elif isinstance(arg, uuid.UUID):
        path_to_type[path_to_item] = str
        if not from_server:
            return str(arg)
        raise type_error
    elif isinstance(arg, bytes):
        path_to_type[path_to_item] = bytes
        return bytes(arg)
    elif isinstance(arg, (io.FileIO, io.BufferedReader)):
        path_to_type[path_to_item] = FileIO
        return FileIO(arg)
    raise exceptions.ApiTypeError('Invalid type passed in got input={} type={}'.format(arg, type(arg)))


class SingletonMeta(type):
    """
    A singleton class for schemas
    Schemas are frozen classes that are never instantiated with init args
    All args come from defaults
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Schema(typing.Generic[T, U], validation.SchemaValidator, metaclass=SingletonMeta):
    """
    the base class of all swagger/openapi schemas/models
    """
    @staticmethod
    def __bases_by_type():
        return {
            str: (str, UnsetAnyTypeSchema),
            int: (int, UnsetAnyTypeSchema),
            float: (float, UnsetAnyTypeSchema),
            bool: (bool, UnsetAnyTypeSchema),
            none_type_: (none_type_, UnsetAnyTypeSchema),
            tuple: (tuple, UnsetAnyTypeSchema),
            immutabledict.immutabledict: (immutabledict.immutabledict, UnsetAnyTypeSchema),
            bytes: (bytes, UnsetAnyTypeSchema),
            FileIO: (FileIO, UnsetAnyTypeSchema),
        }

    @classmethod
    def __get_path_to_schemas(
        cls,
        arg,
        validation_metadata: validation.ValidationMetadata,
        path_to_type: typing.Dict[typing.Tuple[typing.Union[str, int], ...], typing.Type]
    ) -> typing.Dict[typing.Tuple[typing.Union[str, int], ...], typing.Tuple[typing.Type]]:
        """
        Run all validations in the json schema and return a dict of
        json schema to tuple of validated schemas
        """
        _path_to_schemas = {}
        if validation_metadata.validation_ran_earlier(cls):
            validation.add_deeper_validated_schemas(validation_metadata, _path_to_schemas)
        else:
            other_path_to_schemas = cls._validate(arg, validation_metadata=validation_metadata)
            validation.update(_path_to_schemas, other_path_to_schemas)
        # loop through it make a new class for each entry
        # do not modify the returned result because it is cached and we would be modifying the cached value
        path_to_schemas = {}
        for path, schema_classes in _path_to_schemas.items():
            path_to_schemas[path] = tuple(schema_classes)
        """
        For locations that validation did not check
        the code still needs to store type + schema information for instantiation
        All of those schemas will be UnsetAnyTypeSchema
        """
        missing_paths = path_to_type.keys() - path_to_schemas.keys()
        for missing_path in missing_paths:
            value_type = path_to_type[missing_path]
            bases = cls.__bases_by_type()[value_type]
            path_to_schemas[missing_path] = bases

        return path_to_schemas

    @staticmethod
    def __get_items(
        arg: typing.Tuple[typing.Any],
        path_to_item: typing.Tuple[typing.Union[str, int], ...],
        path_to_schemas: typing.Dict[typing.Tuple[typing.Union[str, int], ...], typing.Tuple[typing.Type]]
    ):
        '''
        Schema __get_items
        '''
        cast_items = []

        for i, value in enumerate(arg):
            item_path_to_item = path_to_item + (i,)
            item_cls = path_to_schemas[item_path_to_item][-1]
            new_value = item_cls._get_new_instance_without_conversion(
                value,
                item_path_to_item,
                path_to_schemas
            )
            cast_items.append(new_value)

        return tuple(cast_items)

    @staticmethod
    def __get_properties(
        arg: immutabledict.immutabledict[str, typing.Any],
        path_to_item: typing.Tuple[typing.Union[str, int], ...],
        path_to_schemas: typing.Dict[typing.Tuple[typing.Union[str, int], ...], typing.Tuple[typing.Type]]
    ):
        """
        Schema __get_properties, this is how properties are set
        These values already passed validation
        """
        dict_items = {}

        for property_name_js, value in arg.items():
            property_path_to_item = path_to_item + (property_name_js,)
            property_cls = path_to_schemas[property_path_to_item][-1]
            new_value = property_cls._get_new_instance_without_conversion(
                value,
                property_path_to_item,
                path_to_schemas
            )
            dict_items[property_name_js] = new_value

        return immutabledict.immutabledict(dict_items)

    @classmethod
    def _get_new_instance_without_conversion(
        cls,
        arg: typing.Any,
        path_to_item: typing.Tuple[typing.Union[str, int], ...],
        path_to_schemas: typing.Dict[typing.Tuple[typing.Union[str, int], ...], typing.Tuple[typing.Type]]
    ):
        # We have a Dynamic class and we are making an instance of it
        if isinstance(arg, immutabledict.immutabledict):
            used_arg = cls.__get_properties(arg, path_to_item, path_to_schemas)
        elif isinstance(arg, tuple):
            used_arg = cls.__get_items(arg, path_to_item, path_to_schemas)
        else:
            """
            str = openapi str, datetime.date, and datetime.datetime
            FileIO = openapi binary type and the user inputs a file
            bytes = openapi binary type and the user inputs bytes
            """
            return arg
        arg_type = type(arg)
        type_to_output_cls = cls.__get_type_to_output_cls()
        if type_to_output_cls is None:
            return used_arg
        if arg_type not in type_to_output_cls:
            return used_arg
        output_cls = type_to_output_cls[arg_type]
        if arg_type is tuple and issubclass(output_cls, typing.Tuple):
            return super(output_cls, output_cls).__new__(output_cls, used_arg)
        assert issubclass(output_cls, immutabledict.immutabledict)
        inst = super(output_cls, output_cls).__new__(output_cls, used_arg)
        inst.__init__(used_arg)
        return inst

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal[True],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[True]: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal[False],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[False]: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: bool,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> bool: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> int: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: float,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> float: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            typing.Sequence[INPUT_TYPES_ALL_INCL_SCHEMA],
            U
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> U: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            typing.Mapping[str, INPUT_TYPES_ALL_INCL_SCHEMA],
            T
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> T: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: bytes,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> bytes: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[io.FileIO, FileIO],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> FileIO: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: io.BufferedReader,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> FileIO: ...

    @classmethod
    def __get_type_to_output_cls(cls) -> typing.Optional[typing.Mapping[type, type]]:
        type_to_output_cls = getattr(cls(), 'type_to_output_cls', None)
        type_to_output_cls = typing.cast(typing.Optional[typing.Mapping[type, type]], type_to_output_cls)
        return type_to_output_cls

    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        """
        Schema validate

        Args:
            arg (int/float/str/list/tuple/dict/immutabledict.immutabledict/bool/None): the value
            configuration: contains the schema_configuration.SchemaConfiguration that enables json schema validation keywords
                like minItems, minLength etc
        """
        if isinstance(arg, (tuple, immutabledict.immutabledict)):
            type_to_output_cls = cls.__get_type_to_output_cls()
            if type_to_output_cls is not None:
                for output_cls in type_to_output_cls.values():
                    if isinstance(arg, output_cls):
                        # U + T use case, don't run validations twice
                        return arg

        from_server = False
        validated_path_to_schemas = {}
        path_to_type = {}
        cast_arg = cast_to_allowed_types(
            arg, from_server, validated_path_to_schemas, ('args[0]',), path_to_type)
        validation_metadata = validation.ValidationMetadata(
            path_to_item=('args[0]',),
            configuration=configuration or schema_configuration.SchemaConfiguration(),
            validated_path_to_schemas=immutabledict.immutabledict(validated_path_to_schemas)
        )
        path_to_schemas = cls.__get_path_to_schemas(cast_arg, validation_metadata, path_to_type)
        return cls._get_new_instance_without_conversion(
            cast_arg,
            validation_metadata.path_to_item,
            path_to_schemas,
        )

def get_class(
    item_cls: typing.Union[types.FunctionType, staticmethod, typing.Type[Schema]],
    local_namespace: typing.Optional[dict] = None
) -> typing.Type[Schema]:
    if isinstance(item_cls, typing._GenericAlias): # type: ignore
        # petstore_api.schemas.StrSchema[~U] -> petstore_api.schemas.StrSchema
        origin_cls = typing_extensions.get_origin(item_cls)
        if origin_cls is None:
            raise ValueError('origin class must not be None')
        return origin_cls
    elif isinstance(item_cls, types.FunctionType):
        # referenced schema
        return item_cls()
    elif isinstance(item_cls, staticmethod):
        # referenced schema
        return item_cls.__func__()
    elif isinstance(item_cls, type):
        return item_cls
    elif isinstance(item_cls, typing.ForwardRef):
        return item_cls._evaluate(None, local_namespace)
    raise ValueError('invalid class value passed in')


@dataclasses.dataclass(frozen=True)
class AnyTypeSchema(Schema[T, U]):
    # Python representation of a schema defined as true or {}
    pass


class UnsetAnyTypeSchema(AnyTypeSchema[T, U]):
    # Used when additionalProperties/items was not explicitly defined and a defining schema is needed
    pass

INPUT_TYPES_ALL_INCL_SCHEMA = typing.Union[
    dict,
    immutabledict.immutabledict,
    list,
    tuple,
    float,
    int,
    str,
    datetime.date,
    datetime.datetime,
    uuid.UUID,
    bool,
    None,
    bytes,
    io.FileIO,
    io.BufferedReader,
]