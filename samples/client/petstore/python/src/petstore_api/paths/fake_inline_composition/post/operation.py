# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client
from petstore_api.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from petstore_api.paths.fake_inline_composition.post.request_body.content.application_json import schema
from petstore_api.paths.fake_inline_composition.post.request_body.content.multipart_form_data import schema as schema_2

from .. import path
from .responses import response_200
from . import request_body
from .parameters import (
    parameter_0,
    parameter_1,
)
from .query_parameters import QueryParameters, QueryParametersDictInput, QueryParametersDict
query_parameter_classes = (
    parameter_0.Parameter0,
    parameter_1.Parameter1,
)


__StatusCodeToResponse = typing.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200._200],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200._200,
}
_non_error_status_codes = frozenset({
    '200',
})

_all_accept_content_types = (
    "application/json",
    "multipart/form-data",
)


class BaseApi(api_client.Api):
    @typing.overload
    def _inline_composition(
        self,
        body: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: typing.Literal[False] = False,
        content_type: typing.Literal["application/json"] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_200.ApiResponse: ...

    @typing.overload
    def _inline_composition(
        self,
        body: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: typing.Literal[True],
        content_type: typing.Literal["application/json"] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _inline_composition(
        self,
        body: typing.Union[
            schema_2.SchemaDictInput,
            schema_2.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: typing.Literal[False] = False,
        content_type: typing.Literal["multipart/form-data"],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_200.ApiResponse: ...

    @typing.overload
    def _inline_composition(
        self,
        body: typing.Union[
            schema_2.SchemaDictInput,
            schema_2.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: typing.Literal[True],
        content_type: typing.Literal["multipart/form-data"],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _inline_composition(
        self,
        body: typing.Union[
            typing.Union[
                schemas.INPUT_TYPES_ALL,
                schemas.OUTPUT_BASE_TYPES
            ],
            typing.Union[
                schema_2.SchemaDictInput,
                schema_2.SchemaDict,
            ],
            schemas.Unset,
        ] = schemas.unset,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: bool = False,
        content_type: typing.Literal[
            "application/json",
            "multipart/form-data",
        ] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        testing composed schemas at inline locations
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        if query_params is not None:
            query_params = QueryParameters.validate(
                query_params,
                configuration=self.api_client.schema_configuration
            )
        used_path, query_params_suffix = self._get_used_path(
            path,
            query_parameters=query_parameter_classes,
            query_params=query_params,
            skip_validation=True
        )
        headers = self._get_headers(accept_content_types=accept_content_types)
        # TODO add cookie handling

        fields, serialized_body = self._get_fields_and_body(
            request_body=request_body.RequestBody,
            body=body,
            content_type=content_type,
            headers=headers
        )
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            query_params_suffix=query_params_suffix,
            method='post',
            host=host,
            headers=headers,
            fields=fields,
            body=serialized_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            skip_deser_response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
            self._verify_response_status(skip_deser_response)
            return skip_deser_response

        status = str(raw_response.status)
        if status in _non_error_status_codes:
            status_code = typing.cast(
                typing.Literal[
                    '200',
                ],
                status
            )
            return _status_code_to_response[status_code].deserialize(
                raw_response, self.api_client.schema_configuration)

        response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        self._verify_response_status(response)
        return response


class InlineComposition(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    inline_composition = BaseApi._inline_composition


class ApiForPost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    post = BaseApi._inline_composition
