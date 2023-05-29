# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

_Not: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]
AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema[U]
Path: typing_extensions.TypeAlias = schemas.StrSchema[U]


class Op(
    schemas.StrSchema[schemas.T]
):


    class Schema_:
        types = {
            str,
        }
        enum_value_to_name = {
            "remove": "REMOVE",
        }
    
    @schemas.classproperty
    def REMOVE(cls):
        return cls("remove") # type: ignore


class JSONPatchRequestRemove(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "op",
            "path",
        }
        
        @staticmethod
        def properties():
            return {
                "path": Path,
                "op": Op,
            }
        
        @staticmethod
        def additional_properties():
            return AdditionalProperties
    
    @property
    def op(self) -> Op[str]:
        return self.__getitem__("op")
    
    @property
    def path(self) -> Path[str]:
        return self.__getitem__("path")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op"]) -> Op[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> Path[str]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["op"],
            typing_extensions.Literal["path"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        op: typing.Union[
            Op[str],
            str
        ],
        path: typing.Union[
            Path[str],
            str
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> JSONPatchRequestRemove[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            op=op,
            path=path,
            configuration_=configuration_,
        )
        inst = typing.cast(
            JSONPatchRequestRemove[frozendict.frozendict],
            inst
        )
        return inst

