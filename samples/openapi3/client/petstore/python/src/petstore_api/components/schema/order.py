# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

Id: typing_extensions.TypeAlias = schemas.Int64Schema
PetId: typing_extensions.TypeAlias = schemas.Int64Schema
Quantity: typing_extensions.TypeAlias = schemas.Int32Schema
ShipDate: typing_extensions.TypeAlias = schemas.DateTimeSchema


class StatusEnums:

    @schemas.classproperty
    def PLACED(cls) -> str:
        return Status.validate("placed")

    @schemas.classproperty
    def APPROVED(cls) -> str:
        return Status.validate("approved")

    @schemas.classproperty
    def DELIVERED(cls) -> str:
        return Status.validate("delivered")


@dataclasses.dataclass(frozen=True)
class Status(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, bool, schemas.none_type_], str] = dataclasses.field(
        default_factory=lambda: {
            "placed": "PLACED",
            "approved": "APPROVED",
            "delivered": "DELIVERED",
        }
    )
    enums = StatusEnums

    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "placed",
        "approved",
        "delivered",
    ]:
        return super().validate(
            arg,
            configuration=configuration,
        )


@dataclasses.dataclass(frozen=True)
class Complete(
    schemas.BoolSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        schemas.Bool,
    })
    default: bool = False
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "id": typing.Type[Id],
        "petId": typing.Type[PetId],
        "quantity": typing.Type[Quantity],
        "shipDate": typing.Type[ShipDate],
        "status": typing.Type[Status],
        "complete": typing.Type[Complete],
    }
)


class OrderDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> int:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["petId"]) -> int:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> int:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipDate"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["complete"]) -> bool:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["id"],
            typing_extensions.Literal["petId"],
            typing_extensions.Literal["quantity"],
            typing_extensions.Literal["shipDate"],
            typing_extensions.Literal["status"],
            typing_extensions.Literal["complete"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: OrderDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Order.validate(arg, configuration=configuration)
OrderDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class Order(
    schemas.DictSchema[OrderDict]
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
            schemas.immutabledict: OrderDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            OrderDictInput,
            OrderDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> OrderDict:
        return super().validate(
            arg,
            configuration=configuration,
        )

