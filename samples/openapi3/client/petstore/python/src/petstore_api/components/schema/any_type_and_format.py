# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



@dataclasses.dataclass(frozen=True)
class Uuid(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'uuid'



@dataclasses.dataclass(frozen=True)
class Date(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'date'



@dataclasses.dataclass(frozen=True)
class DateTime(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'date-time'



@dataclasses.dataclass(frozen=True)
class Number(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'number'



@dataclasses.dataclass(frozen=True)
class Binary(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'binary'



@dataclasses.dataclass(frozen=True)
class Int32(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'int32'



@dataclasses.dataclass(frozen=True)
class Int64(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'int64'



@dataclasses.dataclass(frozen=True)
class Double(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'double'



@dataclasses.dataclass(frozen=True)
class _Float(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'float'

Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "uuid": typing.Type[Uuid],
        "date": typing.Type[Date],
        "date-time": typing.Type[DateTime],
        "number": typing.Type[Number],
        "binary": typing.Type[Binary],
        "int32": typing.Type[Int32],
        "int64": typing.Type[Int64],
        "double": typing.Type[Double],
        "float": typing.Type[_Float],
    }
)


class AnyTypeAndFormatDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date-time"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["binary"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int32"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int64"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["uuid"],
            typing_extensions.Literal["date"],
            typing_extensions.Literal["date-time"],
            typing_extensions.Literal["number"],
            typing_extensions.Literal["binary"],
            typing_extensions.Literal["int32"],
            typing_extensions.Literal["int64"],
            typing_extensions.Literal["double"],
            typing_extensions.Literal["float"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: AnyTypeAndFormatDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return AnyTypeAndFormat.validate(arg, configuration=configuration)
AnyTypeAndFormatDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class AnyTypeAndFormat(
    schemas.Schema[AnyTypeAndFormatDict, typing.Tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AnyTypeAndFormatDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            AnyTypeAndFormatDictInput,
            AnyTypeAndFormatDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AnyTypeAndFormatDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

