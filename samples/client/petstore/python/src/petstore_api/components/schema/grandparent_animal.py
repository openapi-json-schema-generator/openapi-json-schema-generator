# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

PetType: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "pet_type": typing.Type[PetType],
    }
)


class GrandparentAnimalDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "pet_type",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def pet_type(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("pet_type")
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)

    @staticmethod
    def from_dict_(
        arg: GrandparentAnimalDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> GrandparentAnimalDict:
        return GrandparentAnimal.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        pet_type,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_ = {
            "pet_type": pet_type,
        }
        arg_.update(kwargs)
        return GrandparentAnimal.validate(arg_, configuration=configuration_)
GrandparentAnimalDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class GrandparentAnimal(
    schemas.Schema[GrandparentAnimalDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "pet_type",
    })
    discriminator: typing.Mapping[str, typing.Mapping[str, typing.Type[schemas.Schema]]] = dataclasses.field(
        default_factory=lambda: {
            'pet_type': {
                'ChildCat': child_cat.ChildCat,
                'ParentPet': parent_pet.ParentPet,
            }
        }
    )
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: GrandparentAnimalDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            GrandparentAnimalDictInput,
            GrandparentAnimalDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> GrandparentAnimalDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )


from petstore_api.components.schema import child_cat
from petstore_api.components.schema import parent_pet
