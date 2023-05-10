# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class Schema(
    schemas.DictSchema[schemas.T]
):


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
        
            @staticmethod
            def string() -> typing.Type['foo.Foo']:
                return foo.Foo
            __annotations__ = {
                "string": string,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["string"]) -> foo.Foo[frozendict.frozendict]: ...
    
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
            typing_extensions.Literal["string"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        string: typing.Union['foo.Foo', dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> Schema[frozendict.frozendict]:
        return super().__new__(
            cls,
            *args_,
            string=string,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import foo
