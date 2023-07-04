# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
import datetime
import dataclasses
import io
import typing
import uuid

import immutabledict
import typing_extensions

from petstore_api.configurations import schema_configuration

from . import schema


T = typing.TypeVar('T')
U = typing.TypeVar('U')


@dataclasses.dataclass(frozen=True)
class ListSchema(schema.Schema[immutabledict.immutabledict, U]):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            typing.Sequence[schema.INPUT_TYPES_ALL_INCL_SCHEMA],
            U
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> U:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class NoneSchema(schema.Schema):
    types: typing.FrozenSet[typing.Type] = frozenset({schema.none_type_})

    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class NumberSchema(schema.Schema):
    """
    This is used for type: number with no format
    Both integers AND floats are accepted
    """
    types: typing.FrozenSet[typing.Type] = frozenset({float, int})

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

    @classmethod
    def validate(
        cls,
        arg: typing.Union[int, float],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class IntSchema(NumberSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({int})
    format: str = 'int'

    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> int:
        return super().validate(arg, configuration)


@dataclasses.dataclass(frozen=True)
class Int32Schema(IntSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({int})
    format: str = 'int32'

    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> int:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class Int64Schema(IntSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({int})
    format: str = 'int64'

    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> int:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class Float32Schema(NumberSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({float})
    format: str = 'float'

    @classmethod
    def validate(
        cls,
        arg: float,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> float:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class Float64Schema(NumberSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({float})
    format: str = 'double'

    @classmethod
    def validate(
        cls,
        arg: float,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> float:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class StrSchema(schema.Schema):
    """
    date + datetime string types must inherit from this class
    That is because one can validate a str payload as both:
    - type: string (format unset)
    - type: string, format: date
    """
    types: typing.FrozenSet[typing.Type] = frozenset({str})

    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class UUIDSchema(StrSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({str})
    format: str = 'uuid'

    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, uuid.UUID],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class DateSchema(StrSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({str})
    format: str = 'date'

    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, datetime.date],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class DateTimeSchema(StrSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({str})
    format: str = 'date-time'

    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, datetime.datetime],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str:
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class DecimalSchema(StrSchema):
    types: typing.FrozenSet[typing.Type] = frozenset({str})
    format: str = 'number'

    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str:
        """
        Note: Decimals may not be passed in because cast_to_allowed_types is only invoked once for payloads
        which can be simple (str) or complex (dicts or lists with nested values)
        Because casting is only done once and recursively casts all values prior to validation then for a potential
        client side Decimal input if Decimal was accepted as an input in DecimalSchema then one would not know
        if one was using it for a StrSchema (where it should be cast to str) or one is using it for NumberSchema
        where it should stay as Decimal.
        """
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class BytesSchema(schema.Schema):
    """
    this class will subclass bytes and is immutable
    """
    types: typing.FrozenSet[typing.Type] = frozenset({bytes})

    @classmethod
    def validate(
        cls,
        arg: bytes,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> bytes:
        super_cls: typing.Type = super(schema.Schema, cls)
        return super_cls.validate(arg)


@dataclasses.dataclass(frozen=True)
class FileSchema(schema.Schema):
    """
    This class is NOT immutable
    Dynamic classes are built using it for example when AnyType allows in binary data
    Al other schema classes ARE immutable
    If one wanted to make this immutable one could make this a DictSchema with required properties:
    - data = BytesSchema (which would be an immutable bytes based schema)
    - file_name = StrSchema
    and cast_to_allowed_types would convert bytes and file instances into dicts containing data + file_name
    The downside would be that data would be stored in memory which one may not want to do for very large files

    The developer is responsible for closing this file and deleting it

    This class was kept as mutable:
    - to allow file reading and writing to disk
    - to be able to preserve file name info
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schema.FileIO})

    @classmethod
    def validate(
        cls,
        arg: typing.Union[io.FileIO, io.BufferedReader],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> schema.FileIO:
        super_cls: typing.Type = super(schema.Schema, cls)
        return super_cls.validate(arg)


@dataclasses.dataclass(frozen=True)
class BinarySchema(schema.Schema):
    types: typing.FrozenSet[typing.Type] = frozenset({schema.FileIO, bytes})
    format: str = 'binary'

    one_of: typing.Tuple[typing.Type[schema.Schema], ...] = (
        BytesSchema,
        FileSchema,
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[io.FileIO, io.BufferedReader, bytes],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Union[schema.FileIO, bytes]:
        return super().validate(arg)


@dataclasses.dataclass(frozen=True)
class BoolSchema(schema.Schema):
    types: typing.FrozenSet[typing.Type] = frozenset({bool})

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

    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate(arg, configuration=configuration)


@dataclasses.dataclass(frozen=True)
class NotAnyTypeSchema(schema.AnyTypeSchema):
    """
    Python representation of a schema defined as false or {'not': {}}
    Does not allow inputs in of AnyType
    Note: validations on this class are never run because the code knows that no inputs will ever validate
    """
    not_: typing.Type[schema.Schema] = schema.AnyTypeSchema

    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        return super().validate(arg, configuration=configuration)

OUTPUT_BASE_TYPES = typing.Union[
    immutabledict.immutabledict[str, 'OUTPUT_BASE_TYPES'],
    str,
    int,
    float,
    bool,
    schema.none_type_,
    typing.Tuple['OUTPUT_BASE_TYPES'],
    bytes,
    schema.FileIO
]


@dataclasses.dataclass(frozen=True)
class DictSchema(schema.Schema[T, typing.Tuple[OUTPUT_BASE_TYPES, ...]]):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: T,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> T: ...

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, object],  # object needed as value type for typeddict inputs
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> T: ...

    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ) -> T:
        if isinstance(arg, immutabledict.immutabledict):
            # T use case
            return super().validate(arg, configuration=configuration)
        arg = typing.cast(typing.Mapping[str, schema.INPUT_TYPES_ALL_INCL_SCHEMA], arg)
        return super().validate(arg, configuration=configuration)
