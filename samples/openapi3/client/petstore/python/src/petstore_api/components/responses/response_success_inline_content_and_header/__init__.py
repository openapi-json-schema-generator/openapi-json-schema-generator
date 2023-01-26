# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import dataclasses
import datetime
import decimal
import io
import typing
import uuid

import frozendict
import typing_extensions
import urllib3

from petstore_api import api_client
from petstore_api import schemas
from .content. import  as _
from .headers import 


class Header:
    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
            'someHeader': typing.Union[.., str, ],
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        .,
    ]

@dataclasses.dataclass
class _ApiResponse(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        _.,
    ]
    headers: Header.Params


class (api_client.OpenApiResponse[_ApiResponse]):
    response_cls = _ApiResponse


    class __MediaType(api_client.MediaType):
        schema: typing.Type[_.] = _.
    __Content = typing_extensions.TypedDict(
        '__Content',
        {
            '': typing.Type[__MediaType],
        }
    )
    content: __Content = {
        '': __MediaType,
    }
    headers=Header.parameters
