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
from . import request_body
from .parameters import parameter_0


AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.fake_body_with_query_params.put.parameters.parameter_0 import schema as parameter_0_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "query": typing.Type[parameter_0_schema.Schema],
    }
)


class QueryParametersDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def query(self) -> str:
        return self.__getitem__("query")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["query"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
QueryParametersDictInput = typing_extensions.TypedDict(
    'QueryParametersDictInput',
    {
        "query": str,
    }
)


@dataclasses.dataclass(frozen=True)
class QueryParameters(
    schemas.DictSchema[QueryParametersDict]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "query",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            immutabledict.immutabledict: QueryParametersDict
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
        return super().validate(
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


class BaseApi(api_client.Api):
    @typing.overload
    def _body_with_query_params(
        self,
        body: typing.Union[
            request_body.content.application_json.schema.user.UserDictInput,
            request_body.content.application_json.schema.user.UserDict,
        ],
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False
    ) -> response_200.ResponseFor200.response_cls: ...

    @typing.overload
    def _body_with_query_params(
        self,
        body: typing.Union[
            request_body.content.application_json.schema.user.UserDictInput,
            request_body.content.application_json.schema.user.UserDict,
        ],
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _body_with_query_params(
        self,
        body: typing.Union[
            request_body.content.application_json.schema.user.UserDictInput,
            request_body.content.application_json.schema.user.UserDict,
        ],
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: bool = False
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        query_params = QueryParameters.validate(query_params)
        used_path = self._get_used_path(
            path,
            query_parameters=query_parameter_classes,
            query_params=query_params
        )
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

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='put',
            host=host,
            headers=_headers,
            fields=_fields,
            body=_body,
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
                    ],
                    status
                )
                response = _status_code_to_response[status].deserialize(
                    raw_response, self.api_client.schema_configuration)
            else:
                response = api_response.ApiResponseWithoutDeserialization(response=raw_response)

        self._verify_response_status(response)

        return response


class BodyWithQueryParams(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    body_with_query_params = BaseApi._body_with_query_params


class ApiForPut(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    put = BaseApi._body_with_query_params
