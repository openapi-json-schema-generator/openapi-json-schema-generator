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


class ReqPropsFromTrueAddProps(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "invalid-name",
            "validName",
        }
        AdditionalProperties = schemas.AnyTypeSchema
    
    @property
    def validName(self) -> Schema_.AdditionalProperties:
        return self.__getitem__("validName")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invalid-name"]) -> Schema_.AdditionalProperties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validName"]) -> Schema_.AdditionalProperties: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> Schema_.AdditionalProperties: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["invalid-name"],
            typing_extensions.Literal["validName"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        validName: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
    ) -> 'ReqPropsFromTrueAddProps':
        return super().__new__(
            cls,
            *args_,
            validName=validName,
            configuration_=configuration_,
            **kwargs,
        )
