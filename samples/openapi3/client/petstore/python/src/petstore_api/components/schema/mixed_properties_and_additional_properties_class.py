# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

Uuid: typing_extensions.TypeAlias = schemas.UUIDSchema
DateTime: typing_extensions.TypeAlias = schemas.DateTimeSchema

from petstore_api.components.schema import animal


class MapDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    def __getitem__(self, name: str) -> animal.AnimalDict:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: MapDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Map.validate(arg, configuration=configuration)
MapDictInput = typing.Mapping[
    str,
    typing.Union[
        animal.AnimalDict,
        dict,
        immutabledict.immutabledict
    ],
]


@dataclasses.dataclass(frozen=True)
class Map(
    schemas.DictSchema[MapDict]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    additional_properties: typing.Type[animal.Animal] = dataclasses.field(default_factory=lambda: animal.Animal) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            immutabledict.immutabledict: MapDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MapDictInput,
            MapDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapDict:
        return super().validate(
            arg,
            configuration=configuration,
        )

Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "uuid": typing.Type[Uuid],
        "dateTime": typing.Type[DateTime],
        "map": typing.Type[Map],
    }
)


class MixedPropertiesAndAdditionalPropertiesClassDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map"]) -> MapDict:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["uuid"],
            typing_extensions.Literal["dateTime"],
            typing_extensions.Literal["map"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: MixedPropertiesAndAdditionalPropertiesClassDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return MixedPropertiesAndAdditionalPropertiesClass.validate(arg, configuration=configuration)
MixedPropertiesAndAdditionalPropertiesClassDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class MixedPropertiesAndAdditionalPropertiesClass(
    schemas.DictSchema[MixedPropertiesAndAdditionalPropertiesClassDict]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            immutabledict.immutabledict: MixedPropertiesAndAdditionalPropertiesClassDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MixedPropertiesAndAdditionalPropertiesClassDictInput,
            MixedPropertiesAndAdditionalPropertiesClassDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MixedPropertiesAndAdditionalPropertiesClassDict:
        return super().validate(
            arg,
            configuration=configuration,
        )

