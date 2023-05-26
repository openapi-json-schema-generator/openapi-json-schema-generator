# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class JSONPatchRequestAddReplaceTest(
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
            "value",
        }
        
        class Properties:
            Path: typing_extensions.TypeAlias = schemas.StrSchema[U]
            Value: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]
            
            
            class Op(
                schemas.StrSchema[schemas.T]
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
                    return cls("add") # type: ignore
                
                @schemas.classproperty
                def REPLACE(cls):
                    return cls("replace") # type: ignore
                
                @schemas.classproperty
                def TEST(cls):
                    return cls("test") # type: ignore
            __annotations__ = {
                "path": Path,
                "value": Value,
                "op": Op,
            }
        AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema[U]
    
    @property
    def op(self) -> Schema_.Properties.Op[str]:
        return self.__getitem__("op")
    
    @property
    def path(self) -> Schema_.Properties.Path[str]:
        return self.__getitem__("path")
    
    @property
    def value(self) -> Schema_.Properties.Value[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]:
        return self.__getitem__("value")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op"]) -> Schema_.Properties.Op[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> Schema_.Properties.Path[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> Schema_.Properties.Value[typing.Union[
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
        op: typing.Union[
            Schema_.Properties.Op,
            str
        ],
        path: typing.Union[
            Schema_.Properties.Path,
            str
        ],
        value: typing.Union[
            Schema_.Properties.Value,
            dict,
            frozendict.frozendict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> JSONPatchRequestAddReplaceTest[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            op=op,
            path=path,
            value=value,
            configuration_=configuration_,
        )
        inst = typing.cast(
            JSONPatchRequestAddReplaceTest[frozendict.frozendict],
            inst
        )
        return inst
