# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class JSONPatchRequestAddReplaceTest(
    schemas.DictSchema
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
            "value",
        }
        
        class Properties:
            Path = schemas.StrSchema
            Value = schemas.AnyTypeSchema
            
            
            class Op(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "add": "ADD",
                        "replace": "REPLACE",
                        "test": "TEST",
                    }
                
                @schemas.classproperty
                def ADD(cls):
                    return cls("add")
                
                @schemas.classproperty
                def REPLACE(cls):
                    return cls("replace")
                
                @schemas.classproperty
                def TEST(cls):
                    return cls("test")
            __annotations__ = {
                "path": Path,
                "value": Value,
                "op": Op,
            }
        AdditionalProperties = schemas.NotAnyTypeSchema
    
    @property
    def op(self) -> Schema_.Properties.Op:
        return self.__getitem__("op")
    
    @property
    def path(self) -> Schema_.Properties.Path:
        return self.__getitem__("path")
    
    @property
    def value(self) -> Schema_.Properties.Value:
        return self.__getitem__("value")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op"]) -> Schema_.Properties.Op: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> Schema_.Properties.Path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> Schema_.Properties.Value: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["op"],
            typing_extensions.Literal["path"],
            typing_extensions.Literal["value"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        op: typing.Union[Schema_.Properties.Op, str],
        path: typing.Union[Schema_.Properties.Path, str],
        value: typing.Union[Schema_.Properties.Value, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'JSONPatchRequestAddReplaceTest':
        return super().__new__(
            cls,
            *args_,
            op=op,
            path=path,
            value=value,
            configuration_=configuration_,
        )
