# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



@dataclasses.dataclass(frozen=True)
class Integer(
    schemas.IntSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        int,
    })
    format: str = 'int'
    inclusive_maximum: typing.Union[int, float] = 100
    inclusive_minimum: typing.Union[int, float] = 10
    multiple_of: typing.Union[int, float] = 2
Int32: typing_extensions.TypeAlias = schemas.Int32Schema


@dataclasses.dataclass(frozen=True)
class Int32withValidations(
    schemas.Int32Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        int,
    })
    format: str = 'int32'
    inclusive_maximum: typing.Union[int, float] = 200
    inclusive_minimum: typing.Union[int, float] = 20
Int64: typing_extensions.TypeAlias = schemas.Int64Schema


@dataclasses.dataclass(frozen=True)
class Number(
    schemas.NumberSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        float,
        int,
    })
    inclusive_maximum: typing.Union[int, float] = 543.2
    inclusive_minimum: typing.Union[int, float] = 32.1
    multiple_of: typing.Union[int, float] = 32.5


@dataclasses.dataclass(frozen=True)
class _Float(
    schemas.Float32Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        float,
        int,
    })
    format: str = 'float'
    inclusive_maximum: typing.Union[int, float] = 987.6
    inclusive_minimum: typing.Union[int, float] = 54.3
Float32: typing_extensions.TypeAlias = schemas.Float32Schema


@dataclasses.dataclass(frozen=True)
class Double(
    schemas.Float64Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        float,
        int,
    })
    format: str = 'double'
    inclusive_maximum: typing.Union[int, float] = 123.4
    inclusive_minimum: typing.Union[int, float] = 67.8
Float64: typing_extensions.TypeAlias = schemas.Float64Schema
Items: typing_extensions.TypeAlias = schemas.NumberSchema


class ArrayWithUniqueItemsTuple(
    typing.Tuple[
        typing.Union[int, float],
        ...
    ]
):

    def __new__(cls, arg: ArrayWithUniqueItemsTupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ArrayWithUniqueItems.validate(arg, configuration=configuration)
ArrayWithUniqueItemsTupleInput = typing.Union[
    typing.List[
        typing.Union[
            float,
            int
        ],
    ],
    typing.Tuple[
        typing.Union[
            float,
            int
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class ArrayWithUniqueItems(
    schemas.Schema[schemas.immutabledict, ArrayWithUniqueItemsTuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    unique_items: bool = True
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: ArrayWithUniqueItemsTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ArrayWithUniqueItemsTupleInput,
            ArrayWithUniqueItemsTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ArrayWithUniqueItemsTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )


@dataclasses.dataclass(frozen=True)
class String(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    pattern: schemas.PatternInfo = schemas.PatternInfo(
        pattern=r'[a-z]',  # noqa: E501
        flags=re.I,
    )
Byte: typing_extensions.TypeAlias = schemas.StrSchema
Binary: typing_extensions.TypeAlias = schemas.BinarySchema
Date: typing_extensions.TypeAlias = schemas.DateSchema
DateTime: typing_extensions.TypeAlias = schemas.DateTimeSchema
Uuid: typing_extensions.TypeAlias = schemas.UUIDSchema
UuidNoExample: typing_extensions.TypeAlias = schemas.UUIDSchema


@dataclasses.dataclass(frozen=True)
class Password(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    format: str = 'password'
    max_length: int = 64
    min_length: int = 10


@dataclasses.dataclass(frozen=True)
class PatternWithDigits(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    pattern: schemas.PatternInfo = schemas.PatternInfo(
        pattern=r'^\d{10}$'  # noqa: E501
    )


@dataclasses.dataclass(frozen=True)
class PatternWithDigitsAndDelimiter(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    pattern: schemas.PatternInfo = schemas.PatternInfo(
        pattern=r'^image_\d{1,3}$',  # noqa: E501
        flags=re.I,
    )
NoneProp: typing_extensions.TypeAlias = schemas.NoneSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "integer": typing.Type[Integer],
        "int32": typing.Type[Int32],
        "int32withValidations": typing.Type[Int32withValidations],
        "int64": typing.Type[Int64],
        "number": typing.Type[Number],
        "float": typing.Type[_Float],
        "float32": typing.Type[Float32],
        "double": typing.Type[Double],
        "float64": typing.Type[Float64],
        "arrayWithUniqueItems": typing.Type[ArrayWithUniqueItems],
        "string": typing.Type[String],
        "byte": typing.Type[Byte],
        "binary": typing.Type[Binary],
        "date": typing.Type[Date],
        "dateTime": typing.Type[DateTime],
        "uuid": typing.Type[Uuid],
        "uuidNoExample": typing.Type[UuidNoExample],
        "password": typing.Type[Password],
        "pattern_with_digits": typing.Type[PatternWithDigits],
        "pattern_with_digits_and_delimiter": typing.Type[PatternWithDigitsAndDelimiter],
        "noneProp": typing.Type[NoneProp],
    }
)


class FormatTestDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "byte",
        "date",
        "number",
        "password",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "integer",
        "int32",
        "int32withValidations",
        "int64",
        "float",
        "float32",
        "double",
        "float64",
        "arrayWithUniqueItems",
        "string",
        "binary",
        "dateTime",
        "uuid",
        "uuidNoExample",
        "pattern_with_digits",
        "pattern_with_digits_and_delimiter",
        "noneProp",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["byte"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["date"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["number"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["password"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["integer"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["int32"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["int32withValidations"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["int64"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["float"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["float32"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["double"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["float64"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["arrayWithUniqueItems"]) -> ArrayWithUniqueItemsTuple:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["string"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["binary"]) -> typing.Union[bytes, schemas.FileIO]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["dateTime"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["uuid"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["uuidNoExample"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["pattern_with_digits"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["pattern_with_digits_and_delimiter"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["noneProp"]) -> None:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "byte":
            return typing.cast(
                str,
                val
            )
        elif name == "date":
            return typing.cast(
                str,
                val
            )
        elif name == "number":
            return typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "password":
            return typing.cast(
                str,
                val
            )
        elif name == "integer":
            return val if val is schemas.unset else typing.cast(
                int,
                val
            )
        elif name == "int32":
            return val if val is schemas.unset else typing.cast(
                int,
                val
            )
        elif name == "int32withValidations":
            return val if val is schemas.unset else typing.cast(
                int,
                val
            )
        elif name == "int64":
            return val if val is schemas.unset else typing.cast(
                int,
                val
            )
        elif name == "float":
            return val if val is schemas.unset else typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "float32":
            return val if val is schemas.unset else typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "double":
            return val if val is schemas.unset else typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "float64":
            return val if val is schemas.unset else typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "arrayWithUniqueItems":
            return val if val is schemas.unset else typing.cast(
                ArrayWithUniqueItemsTuple,
                val
            )
        elif name == "string":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "binary":
            return val if val is schemas.unset else typing.cast(
                typing.Union[bytes, schemas.FileIO],
                val
            )
        elif name == "dateTime":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "uuid":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "uuidNoExample":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "pattern_with_digits":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "pattern_with_digits_and_delimiter":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "noneProp":
            return val if val is schemas.unset else typing.cast(
                None,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: FormatTestDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return FormatTest.validate(arg, configuration=configuration)
FormatTestDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class FormatTest(
    schemas.Schema[FormatTestDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "byte",
        "date",
        "number",
        "password",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: FormatTestDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            FormatTestDictInput,
            FormatTestDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> FormatTestDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

