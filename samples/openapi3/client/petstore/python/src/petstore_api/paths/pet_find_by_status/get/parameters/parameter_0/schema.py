# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class Items(
    schemas.StrSchema[schemas.T]
):


    class Schema_:
        types = {
            str,
        }
        default = "available"
        enum_value_to_name = {
            "available": "AVAILABLE",
            "pending": "PENDING",
            "sold": "SOLD",
        }
    
    @schemas.classproperty
    def AVAILABLE(cls):
        return cls("available") # type: ignore
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("pending") # type: ignore
    
    @schemas.classproperty
    def SOLD(cls):
        return cls("sold") # type: ignore


class Schema(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types = {tuple}
        
        @staticmethod
        def items():
            return Items

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                Items[str],
                str
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> Schema[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Schema[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items[str]:
        return super().__getitem__(name)

