# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *
from petstore_api import api_client
from petstore_api.shared_imports.operation_imports import *

from .. import path
from .responses import (
    response_200,
    response_400,
)
from .parameters import (
    parameter_0,
    parameter_1,
)


AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.user_login.get.parameters.parameter_0 import schema as parameter_0_schema
from petstore_api.paths.user_login.get.parameters.parameter_1 import schema as parameter_1_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "password": typing.Type[parameter_1_schema.Schema],
        "username": typing.Type[parameter_0_schema.Schema],
    }
)


class QueryParametersDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def password(self) -> str:
        return self.__getitem__("password")
    
    @property
    def username(self) -> str:
        return self.__getitem__("username")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["password"],
            typing_extensions.Literal["username"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: QueryParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return QueryParameters.validate(arg, configuration=configuration)
QueryParametersDictInput = typing_extensions.TypedDict(
    'QueryParametersDictInput',
    {
        "password": str,
        "username": str,
    }
)


@dataclasses.dataclass(frozen=True)
class QueryParameters(
    schemas.DictSchema[QueryParametersDict]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "password",
        "username",
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
    parameter_1.Parameter1,
)


__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200.ResponseFor200],
        '400': typing.Type[response_400.ResponseFor400],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200.ResponseFor200,
    '400': response_400.ResponseFor400,
}

_all_accept_content_types = (
    "application/xml",
    "application/json",
)


class BaseApi(api_client.Api):
    @typing.overload
    def _login_user(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False
    ) -> response_200.ResponseFor200.response_cls: ...

    @typing.overload
    def _login_user(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _login_user(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: bool = False
    ):
        """
        Logs user into the system
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
        _headers = self._get_headers(accept_content_types=accept_content_types)
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            'servers', server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='get',
            host=host,
            headers=_headers,
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
                    '400',
                    ],
                    status
                )
                response = _status_code_to_response[status].deserialize(
                    raw_response, self.api_client.schema_configuration)
            else:
                response = api_response.ApiResponseWithoutDeserialization(response=raw_response)

        self._verify_response_status(response)

        return response


class LoginUser(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    login_user = BaseApi._login_user


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    get = BaseApi._login_user
