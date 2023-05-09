# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client
from petstore_api.shared_imports.operation_imports import *

from .. import path
from .responses import response_default



default_response = response_default.Default


class BaseApi(api_client.Api):
    @typing.overload
    def _logout_user(
        self,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...

    @typing.overload
    def _logout_user(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _logout_user(
        self,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_default.Default.response_cls,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _logout_user(
        self,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Logs out current logged in user session
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            'servers', server_index
        )

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get',
            host=host,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            api_response = default_response.deserialize(response, self.api_client.schema_configuration)

        self._verify_response_status(api_response)

        return api_response


class LogoutUser(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    logout_user = BaseApi._logout_user


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    get = BaseApi._logout_user
