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


@dataclasses.dataclass(frozen=True)
class Int32(
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


@dataclasses.dataclass(frozen=True)
class PatternWithoutDelimiter(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    pattern: schemas.PatternInfo = schemas.PatternInfo(
        pattern=r'^[A-Z].*'  # noqa: E501
    )
Byte: typing_extensions.TypeAlias = schemas.StrSchema
Binary: typing_extensions.TypeAlias = schemas.BinarySchema
Date: typing_extensions.TypeAlias = schemas.DateSchema


@dataclasses.dataclass(frozen=True)
class DateTime(
    schemas.DateTimeSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    format: str = 'date-time'


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
Callback: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "integer": typing.Type[Integer],
        "int32": typing.Type[Int32],
        "int64": typing.Type[Int64],
        "number": typing.Type[Number],
        "float": typing.Type[_Float],
        "double": typing.Type[Double],
        "string": typing.Type[String],
        "pattern_without_delimiter": typing.Type[PatternWithoutDelimiter],
        "byte": typing.Type[Byte],
        "binary": typing.Type[Binary],
        "date": typing.Type[Date],
        "dateTime": typing.Type[DateTime],
        "password": typing.Type[Password],
        "callback": typing.Type[Callback],
    }
)


class SchemaDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "byte",
        "double",
        "number",
        "pattern_without_delimiter",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "integer",
        "int32",
        "int64",
        "float",
        "string",
        "binary",
        "date",
        "dateTime",
        "password",
        "callback",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["byte"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["double"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["number"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["pattern_without_delimiter"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["integer"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["int32"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["int64"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["float"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["string"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["binary"]) -> typing.Union[bytes, schemas.FileIO]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["date"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["dateTime"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["password"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["callback"]) -> str:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "byte":
            return typing.cast(
                str,
                val
            )
        elif name == "double":
            return typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "number":
            return typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "pattern_without_delimiter":
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
        elif name == "date":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "dateTime":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "password":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "callback":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: SchemaDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Schema.validate(arg, configuration=configuration)
SchemaDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.Schema[SchemaDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "byte",
        "double",
        "number",
        "pattern_without_delimiter",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: SchemaDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            SchemaDictInput,
            SchemaDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SchemaDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

