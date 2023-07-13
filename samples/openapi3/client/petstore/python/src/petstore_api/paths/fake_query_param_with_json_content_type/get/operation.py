# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *
from petstore_api import api_client
from petstore_api.shared_imports.operation_imports import *

from .. import path
from .responses import response_200
from .parameters import parameter_0


AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.fake_query_param_with_json_content_type.get.parameters.parameter_0.content.application_json import schema as parameter_0_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "someParam": typing.Type[parameter_0_schema.Schema],
    }
)


class QueryParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def someParam(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("someParam")

    def __new__(cls, arg: QueryParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return QueryParameters.validate(arg, configuration=configuration)
QueryParametersDictInput = typing_extensions.TypedDict(
    'QueryParametersDictInput',
    {
        "someParam": typing.Union[
            dict,
            schemas.immutabledict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ],
    }
)


@dataclasses.dataclass(frozen=True)
class QueryParameters(
    schemas.Schema[QueryParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "someParam",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: QueryParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QueryParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

query_parameter_classes = (
    parameter_0.Parameter0,
)


__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200.ResponseFor200],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200.ResponseFor200,
}
_non_error_status_codes = frozenset({
    '200',
})

_all_accept_content_types = (
    "application/json",
)


class BaseApi(api_client.Api):
    @typing.overload
    def _query_param_with_json_content_type(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        *,
        skip_deserialization: typing_extensions.Literal[False] = False,
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_200.ApiResponse: ...

    @typing.overload
    def _query_param_with_json_content_type(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        *,
        skip_deserialization: typing_extensions.Literal[True],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _query_param_with_json_content_type(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        *,
        skip_deserialization: bool = False,
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        query param with json content-type
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        query_params = QueryParameters.validate(query_params)
        used_path, query_params_suffix = self._get_used_path(
            path,
            query_parameters=query_parameter_classes,
            query_params=query_params
        )
        _headers = self._get_headers(accept_content_types=accept_content_types)
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            query_params_suffix=query_params_suffix,
            method='get',
            host=host,
            headers=_headers,
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
                typing_extensions.Literal[
                    '200',
                ],
                status
            )
            return _status_code_to_response[status_code].deserialize(
                raw_response, self.api_client.schema_configuration)

        response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        self._verify_response_status(response)
        return response


class QueryParamWithJsonContentType(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    query_param_with_json_content_type = BaseApi._query_param_with_json_content_type


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    get = BaseApi._query_param_with_json_content_type
