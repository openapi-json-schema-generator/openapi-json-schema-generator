# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class Player(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    a model that includes a self reference this forces properties and additionalProperties to be lazy loaded in python models because the Player class has not fully loaded when defining properties
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            Name: typing_extensions.TypeAlias = schemas.StrSchema[U]
        
            @staticmethod
            def enemy_player() -> typing.Type['Player']:
                return Player
            __annotations__ = {
                "name": Name,
                "enemyPlayer": enemy_player,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> Schema_.Properties.Name[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enemyPlayer"]) -> Player[frozendict.frozendict]: ...
    
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
            typing_extensions.Literal["name"],
            typing_extensions.Literal["enemyPlayer"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        name: typing.Union[Schema_.Properties.Name, str, schemas.Unset] = schemas.unset,
        enemyPlayer: typing.Union['Player', dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> Player[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            name=name,
            enemyPlayer=enemyPlayer,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            Player[frozendict.frozendict],
            inst
        )
        return inst
