# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class ObjectWithCollidingProperties(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    component with properties that have name collisions
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            SomeProp: typing_extensions.TypeAlias = schemas.DictSchema[U]
            Someprop: typing_extensions.TypeAlias = schemas.DictSchema[U]
            __annotations__ = {
                "someProp": SomeProp,
                "someprop": Someprop,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someProp"]) -> Schema_.Properties.SomeProp[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someprop"]) -> Schema_.Properties.Someprop[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.AnyTypeSchema[typing.Union[
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
            typing_extensions.Literal["someProp"],
            typing_extensions.Literal["someprop"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        someProp: typing.Union[
            Schema_.Properties.SomeProp[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        someprop: typing.Union[
            Schema_.Properties.Someprop[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            dict,
            frozendict.frozendict,
            list,
            tuple,
            decimal.Decimal,
            float,
            int,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            bool,
            None,
            bytes,
            io.FileIO,
            io.BufferedReader,
            schemas.Schema
        ],
    ) -> ObjectWithCollidingProperties[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            someProp=someProp,
            someprop=someprop,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            ObjectWithCollidingProperties[frozendict.frozendict],
            inst
        )
        return inst
