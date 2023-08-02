# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Uuid: typing_extensions.TypeAlias = schemas.UUIDSchema
DateTime: typing_extensions.TypeAlias = schemas.DateTimeSchema

from petstore_api.components.schema import animal


class MapDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def get_additional_property_(self, name: str) -> typing.Union[animal.AnimalDict, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            animal.AnimalDict,
            val
        )

    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Any,
    ):
        return Map.validate(kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: MapDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapDict:
        return Map.validate(arg, configuration=configuration)
MapDictInput = typing.Mapping[
    str,
    typing.Union[
        animal.AnimalDict,
        dict,
        schemas.immutabledict
    ],
]


@dataclasses.dataclass(frozen=True)
class Map(
    schemas.Schema[MapDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[animal.Animal] = dataclasses.field(default_factory=lambda: animal.Animal) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MapDict
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
        return super().validate_base(
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


class MixedPropertiesAndAdditionalPropertiesClassDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "uuid",
        "dateTime",
        "map",
    })
    
    @property
    def uuid(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("uuid", schemas.unset)
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
    def map(self) -> typing.Union[MapDict, schemas.Unset]:
        val = self.get("map", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            MapDict,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)

    @staticmethod
    def from_dict_(
        arg: MixedPropertiesAndAdditionalPropertiesClassDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MixedPropertiesAndAdditionalPropertiesClassDict:
        return MixedPropertiesAndAdditionalPropertiesClass.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        uuid: typing.Union[str, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[str, schemas.Unset] = schemas.unset,
        map: typing.Union[
            MapDict,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_ = {}
        for key, val in (
            ("uuid", uuid),
            ("dateTime", dateTime),
            ("map", map),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        return MixedPropertiesAndAdditionalPropertiesClass.validate(arg_, configuration=configuration_)
MixedPropertiesAndAdditionalPropertiesClassDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class MixedPropertiesAndAdditionalPropertiesClass(
    schemas.Schema[MixedPropertiesAndAdditionalPropertiesClassDict, tuple]
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
            schemas.immutabledict: MixedPropertiesAndAdditionalPropertiesClassDict
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
        return super().validate_base(
            arg,
            configuration=configuration,
        )

