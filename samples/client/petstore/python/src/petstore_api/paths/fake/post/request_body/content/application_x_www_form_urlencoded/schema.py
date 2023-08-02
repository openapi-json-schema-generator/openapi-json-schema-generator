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
    
    @property
    def byte(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("byte")
        )
    
    @property
    def double(self) -> typing.Union[int, float]:
        return typing.cast(
            typing.Union[int, float],
            self.__getitem__("double")
        )
    
    @property
    def number(self) -> typing.Union[int, float]:
        return typing.cast(
            typing.Union[int, float],
            self.__getitem__("number")
        )
    
    @property
    def pattern_without_delimiter(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("pattern_without_delimiter")
        )
    
    @property
    def integer(self) -> typing.Union[int, schemas.Unset]:
        val = self.get("integer", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            int,
            val
        )
    
    @property
    def int32(self) -> typing.Union[int, schemas.Unset]:
        val = self.get("int32", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            int,
            val
        )
    
    @property
    def int64(self) -> typing.Union[int, schemas.Unset]:
        val = self.get("int64", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            int,
            val
        )
    
    @property
    def string(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("string", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def binary(self) -> typing.Union[bytes, schemas.FileIO, schemas.Unset]:
        val = self.get("binary", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Union[bytes, schemas.FileIO],
            val
        )
    
    @property
    def date(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("date", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def dateTime(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("dateTime", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def password(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("password", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def callback(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("callback", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)

    @staticmethod
    def from_dict_(
        arg: SchemaDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SchemaDict:
        return Schema.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        byte: str,
        double: typing.Union[
            int,
            float
        ],
        number: typing.Union[
            int,
            float
        ],
        pattern_without_delimiter: str,
        integer: typing.Union[
            int,
            schemas.Unset
        ] = schemas.unset,
        int32: typing.Union[
            int,
            schemas.Unset
        ] = schemas.unset,
        int64: typing.Union[
            int,
            schemas.Unset
        ] = schemas.unset,
        string: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        binary: typing.Union[
            bytes,
            schemas.FileIO,
            schemas.Unset
        ] = schemas.unset,
        date: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        dateTime: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        password: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        callback: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_ = {
            "byte": byte,
            "double": double,
            "number": number,
            "pattern_without_delimiter": pattern_without_delimiter,
        }
        for key, val in (
            ("integer", integer),
            ("int32", int32),
            ("int64", int64),
            ("string", string),
            ("binary", binary),
            ("date", date),
            ("dateTime", dateTime),
            ("password", password),
            ("callback", callback),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(SchemaDictInput, arg_)
        return Schema.validate(used_arg_, configuration=configuration_)
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

