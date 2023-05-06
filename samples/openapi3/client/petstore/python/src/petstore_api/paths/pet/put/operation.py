# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions, security_schemes
import datetime  # noqa: F401
import decimal  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from .. import path
from .responses import (
    response_400,
    response_404,
    response_405,
)
from . import request_body
from .security import (
    security_requirement_object_0,
    security_requirement_object_1,
)


_security: typing.List[security_schemes.SecurityRequirementObject] = [
    security_requirement_object_0.security_requirement_object,
    security_requirement_object_1.security_requirement_object,
]


__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '400': typing.Type[response_400.ResponseFor400],
        '404': typing.Type[response_404.ResponseFor404],
        '405': typing.Type[response_405.ResponseFor405],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '400': response_400.ResponseFor400,
    '404': response_404.ResponseFor404,
    '405': response_405.ResponseFor405,
}


class BaseApi(api_client.Api):
    @typing.overload
    def _update_pet(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            dict,
            frozendict.frozendict
        ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _update_pet(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/xml"].schema,
            dict,
            frozendict.frozendict
        ],
        content_type: typing_extensions.Literal["application/xml"],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _update_pet(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            request_body.RequestBody.content["application/xml"].schema,
            dict,
            frozendict.frozendict
        ],
        content_type: str = ...,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _update_pet(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            request_body.RequestBody.content["application/xml"].schema,
            dict,
            frozendict.frozendict
        ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _update_pet(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            request_body.RequestBody.content["application/xml"].schema,
            dict,
            frozendict.frozendict
        ],
        content_type: str = ...,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _update_pet(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            request_body.RequestBody.content["application/xml"].schema,
            dict,
            frozendict.frozendict
        ],
        content_type: str = 'application/json',
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Update an existing pet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path

        _headers = HTTPHeaderDict()
        # TODO add cookie handling

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body.RequestBody.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        host = self.api_client.configuration.get_server_url(
            'servers', server_index
        )
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            'paths/' + path + '/put/security',
            _security,
            security_index
        )

        response = self.api_client.call_api(
            resource_path=used_path,
            method='put',
            host=host,
            headers=_headers,
            fields=_fields,
            body=_body,
            security_requirement_object=security_requirement_object,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            status = str(response.status)
            if status in _status_code_to_response:
                status: typing_extensions.Literal[
                    '400',
                    '404',
                    '405',
                ]
                api_response = _status_code_to_response[status].deserialize(
                    response, self.api_client.schema_configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 399:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class UpdatePet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    update_pet = BaseApi._update_pet


class ApiForPut(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    put = BaseApi._update_pet
