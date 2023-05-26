# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class JSONPatchRequestMoveCopy(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "from",
            "op",
            "path",
        }
        
        class Properties:
            _From: typing_extensions.TypeAlias = schemas.StrSchema[U]
            Path: typing_extensions.TypeAlias = schemas.StrSchema[U]
            
            
            class Op(
                schemas.StrSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "move": "MOVE",
                        "copy": "COPY",
                    }
                
                @schemas.classproperty
                def MOVE(cls):
                    return cls("move") # type: ignore
                
                @schemas.classproperty
                def COPY(cls):
                    return cls("copy") # type: ignore
            __annotations__ = {
                "from": _From,
                "path": Path,
                "op": Op,
            }
        AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema[U]
    
    @property
    def op(self) -> Schema_.Properties.Op[str]:
        return self.__getitem__("op")
    
    @property
    def path(self) -> Schema_.Properties.Path[str]:
        return self.__getitem__("path")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> Schema_.Properties._From[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op"]) -> Schema_.Properties.Op[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> Schema_.Properties.Path[str]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["from"],
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
            Schema_.Properties.Op,
            str
        ],
        path: typing.Union[
            Schema_.Properties.Path,
            str
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> JSONPatchRequestMoveCopy[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            op=op,
            path=path,
            configuration_=configuration_,
        )
        inst = typing.cast(
            JSONPatchRequestMoveCopy[frozendict.frozendict],
            inst
        )
        return inst
