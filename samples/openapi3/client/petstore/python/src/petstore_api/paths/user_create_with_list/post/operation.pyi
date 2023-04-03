# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
import datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from .responses import response_default
from . import request_body



class BaseApi(api_client.Api):
    @typing.overload
    def _create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...

    @typing.overload
    def _create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...


    @typing.overload
    def _create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_default.Default.response_cls,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = 'application/json',
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Creates list of users with given input array
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

        response = self.api_client.call_api(
            resource_path=used_path,
            method='post',
            host=host,
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            api_response = default_response.deserialize(response, self.api_client.schema_configuration)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class CreateUsersWithListInput(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names

    @typing.overload
    def create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...

    @typing.overload
    def create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...


    @typing.overload
    def create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_default.Default.response_cls,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def create_users_with_list_input(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = 'application/json',
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._create_users_with_list_input(
            body=body,
            content_type=content_type,
            server_index=server_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForPost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: typing_extensions.Literal["application/json"] = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...


    @typing.overload
    def post(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = ...,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_default.Default.response_cls,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        body: typing.Union[
            request_body.RequestBody.content["application/json"].schema,
            list,
            tuple
        ],
        content_type: str = 'application/json',
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._create_users_with_list_input(
            body=body,
            content_type=content_type,
            server_index=server_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


