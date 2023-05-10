# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class GrandparentAnimal(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "pet_type",
        }
        
        @staticmethod
        def discriminator():
            return {
                'pet_type': {
                    'ChildCat': child_cat.ChildCat,
                    'ParentPet': parent_pet.ParentPet,
                }
            }
        
        class Properties:
            PetType: typing_extensions.TypeAlias = schemas.StrSchema[U]
            __annotations__ = {
                "pet_type": PetType,
            }
    
    pet_type: Schema_.Properties.PetType[str]
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pet_type"]) -> Schema_.Properties.PetType[str]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["pet_type"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        pet_type: typing.Union[Schema_.Properties.PetType, str],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> GrandparentAnimal[frozendict.frozendict]:
        return super().__new__(
            cls,
            *args_,
            pet_type=pet_type,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import child_cat
from petstore_api.components.schema import parent_pet
