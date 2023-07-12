# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *
from petstore_api import api_client, security_schemes
from petstore_api.shared_imports.operation_imports import *

from .. import path
from .responses import (
    response_200,
    response_404,
)
from . import request_body
from petstore_api.paths.fake.post.request_body.content.application_x_www_form_urlencoded import schema as request_body_application_x_www_form_urlencoded_schema
from .security import security_requirement_object_0


_security: typing.List[security_schemes.SecurityRequirementObject] = [
    security_requirement_object_0.security_requirement_object,
]


__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200.ResponseFor200],
        '404': typing.Type[response_404.ResponseFor404],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200.ResponseFor200,
    '404': response_404.ResponseFor404,
}


class BaseApi(api_client.Api):
    @typing.overload
    def _endpoint_parameters(
        self,
        body: typing.Union[
            request_body_application_x_www_form_urlencoded_schema.SchemaDictInput,
            request_body_application_x_www_form_urlencoded_schema.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"] = "application/x-www-form-urlencoded",
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False
    ) -> response_200.ResponseFor200.response_cls: ...

    @typing.overload
    def _endpoint_parameters(
        self,
        body: typing.Union[
            request_body_application_x_www_form_urlencoded_schema.SchemaDictInput,
            request_body_application_x_www_form_urlencoded_schema.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"] = "application/x-www-form-urlencoded",
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _endpoint_parameters(
        self,
        body: typing.Union[
            request_body_application_x_www_form_urlencoded_schema.SchemaDictInput,
            request_body_application_x_www_form_urlencoded_schema.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"] = "application/x-www-form-urlencoded",
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: bool = False
    ):
        """
        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path
        _headers = self._get_headers()
        # TODO add cookie handling

        _fields, _body = self._get_fields_and_body(
            request_body=request_body.RequestBody,
            body=body,
            headers=_headers,
            content_type=content_type
        )
        host = self.api_client.configuration.get_server_url(
            'servers', server_index
        )
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            "paths//fake/post/security",
            _security,
            security_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='post',
            host=host,
            headers=_headers,
            fields=_fields,
            body=_body,
            security_requirement_object=security_requirement_object,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        else:
            status = str(raw_response.status)
            if status in _status_code_to_response:
                status = typing.cast(
                    typing_extensions.Literal[
                    '200',
                    '404',
                    ],
                    status
                )
                response = _status_code_to_response[status].deserialize(
                    raw_response, self.api_client.schema_configuration)
            else:
                response = api_response.ApiResponseWithoutDeserialization(response=raw_response)

        self._verify_response_status(response)

        return response


class EndpointParameters(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    endpoint_parameters = BaseApi._endpoint_parameters


class ApiForPost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    post = BaseApi._endpoint_parameters
