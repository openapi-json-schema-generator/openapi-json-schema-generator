# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Width: typing_extensions.TypeAlias = schemas.DecimalSchema

from petstore_api.components.schema import decimal_payload
from petstore_api.components.schema import money
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "length": typing.Type[decimal_payload.DecimalPayload],
        "width": typing.Type[Width],
        "cost": typing.Type[money.Money],
    }
)


class ObjectWithDecimalPropertiesDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "length",
        "width",
        "cost",
    })
    
    @property
    def length(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("length", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def width(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("width", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def cost(self) -> typing.Union[money.MoneyDict, schemas.Unset]:
        val = self.get("cost", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            money.MoneyDict,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)

    def __new__(cls, arg: ObjectWithDecimalPropertiesDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectWithDecimalProperties.validate(arg, configuration=configuration)
ObjectWithDecimalPropertiesDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ObjectWithDecimalProperties(
    schemas.Schema[ObjectWithDecimalPropertiesDict, tuple]
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
            schemas.immutabledict: ObjectWithDecimalPropertiesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjectWithDecimalPropertiesDictInput,
            ObjectWithDecimalPropertiesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjectWithDecimalPropertiesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

