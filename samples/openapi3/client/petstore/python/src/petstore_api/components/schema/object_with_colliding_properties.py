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


class ObjectWithCollidingPropertiesDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someProp"]) -> immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someprop"]) -> immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["someProp"],
            typing_extensions.Literal["someprop"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
ObjectWithCollidingPropertiesDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class ObjectWithCollidingProperties(
    schemas.DictSchema[ObjectWithCollidingPropertiesDict]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    component with properties that have name collisions
    """
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            immutabledict.immutabledict: ObjectWithCollidingPropertiesDict
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
        return super().validate(
            arg,
            configuration=configuration,
        )

