# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class JSONPatchRequest(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        types = {tuple}
        
        
        class JSONPatchRequest(
            schemas.AnyTypeSchema,
        ):
            """NOTE: This class is auto generated by OpenAPI Generator.
            Ref: https://openapi-generator.tech
        
            Do not edit the class manually.
            """
        
        
            class MetaOapg:
                # any type
                
                class OneOf:
                
                    @staticmethod
                    def json_patch_request() -> typing.Type['json_patch_request_add_replace_test.JSONPatchRequestAddReplaceTest']:
                        return json_patch_request_add_replace_test.JSONPatchRequestAddReplaceTest
                
                    @staticmethod
                    def json_patch_request() -> typing.Type['json_patch_request_remove.JSONPatchRequestRemove']:
                        return json_patch_request_remove.JSONPatchRequestRemove
                
                    @staticmethod
                    def json_patch_request() -> typing.Type['json_patch_request_move_copy.JSONPatchRequestMoveCopy']:
                        return json_patch_request_move_copy.JSONPatchRequestMoveCopy
                    classes = [
                        json_patch_request,
                        json_patch_request,
                        json_patch_request,
                    ]
        
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'JSONPatchRequest':
                return super().__new__(
                    cls,
                    *_args,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.JSONPatchRequest, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.JSONPatchRequest, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'JSONPatchRequest':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.JSONPatchRequest:
        return super().__getitem__(i)
