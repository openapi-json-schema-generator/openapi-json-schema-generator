# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

Color: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "color": typing.Type[Color],
    }
)


class GmFruitDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def color(self) -> str:
        return self.__getitem__("color")

    def __new__(cls, arg: GmFruitDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return GmFruit.validate(arg, configuration=configuration)
GmFruitDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class GmFruit(
    schemas.AnyTypeSchema[GmFruitDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    any_of: AnyOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AnyOf)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: GmFruitDict,
        }
    )


from petstore_api.components.schema import apple
from petstore_api.components.schema import banana
AnyOf = typing.Tuple[
    typing.Type[apple.Apple],
    typing.Type[banana.Banana],
]
