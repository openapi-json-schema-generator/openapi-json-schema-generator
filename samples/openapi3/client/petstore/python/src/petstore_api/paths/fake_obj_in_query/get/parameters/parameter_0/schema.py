# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

Keyword: typing_extensions.TypeAlias = schemas.StrSchema[U]


class Schema(
    schemas.DictSchema[schemas.T]
):


    class Schema_:
        types = {frozendict.frozendict}
        
        @staticmethod
        def properties():
            return {
                "keyword": Keyword,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyword"]) -> Keyword[str]: ...
    
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
            typing_extensions.Literal["keyword"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        keyword: typing.Union[
            Keyword[str],
            schemas.Unset,
            str
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
    ) -> Schema[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            keyword=keyword,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            Schema[frozendict.frozendict],
            inst
        )
        return inst

