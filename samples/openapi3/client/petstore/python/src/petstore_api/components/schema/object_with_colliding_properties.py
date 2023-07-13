# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

SomeProp: typing_extensions.TypeAlias = schemas.DictSchema
Someprop2: typing_extensions.TypeAlias = schemas.DictSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "someProp": typing.Type[SomeProp],
        "someprop": typing.Type[Someprop2],
    }
)


class ObjectWithCollidingPropertiesDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def some_prop(self) -> schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]:
        return self.__getitem__("someProp")
    
    @property
    def someprop(self) -> schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]:
        return self.__getitem__("someprop")
    
    def additional_properties(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__(name)

    def __new__(cls, arg: ObjectWithCollidingPropertiesDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectWithCollidingProperties.validate(arg, configuration=configuration)
ObjectWithCollidingPropertiesDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class ObjectWithCollidingProperties(
    schemas.Schema[ObjectWithCollidingPropertiesDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    component with properties that have name collisions
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjectWithCollidingPropertiesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjectWithCollidingPropertiesDictInput,
            ObjectWithCollidingPropertiesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjectWithCollidingPropertiesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

