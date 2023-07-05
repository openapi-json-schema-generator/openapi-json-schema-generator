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
    response_400,
)
from .parameters import parameter_0
from .security import (
    security_requirement_object_0,
    security_requirement_object_1,
)


AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.pet_find_by_tags.get.parameters.parameter_0 import schema as parameter_0_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "tags": typing.Type[parameter_0_schema.Schema],
    }
)


class QueryParametersDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def tags(self) -> parameter_0_schema.SchemaTuple:
        return self.__getitem__("tags")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> parameter_0_schema.SchemaTuple:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["tags"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: QueryParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return QueryParameters.validate(arg, configuration=configuration)
    
    def __init__(self, arg: QueryParametersDictInput, **kwargs: typing.Optional[schema_configuration.SchemaConfiguration]):
        super().__init__(arg)  # needed to omit passing on configuration in kwargs
QueryParametersDictInput = typing_extensions.TypedDict(
    'QueryParametersDictInput',
    {
        "tags": typing.Union[
            parameter_0_schema.SchemaTuple,
            list,
            tuple
        ],
    }
)


@dataclasses.dataclass(frozen=True)
class QueryParameters(
    schemas.DictSchema[QueryParametersDict]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "tags",
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

_security: typing.List[security_schemes.SecurityRequirementObject] = [
    security_requirement_object_0.security_requirement_object,
    security_requirement_object_1.security_requirement_object,
]


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


class BaseApi(api_client.Api):
    @typing.overload
    def _find_pets_by_tags(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False
    ) -> response_200.ResponseFor200.response_cls: ...

    @typing.overload
    def _find_pets_by_tags(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _find_pets_by_tags(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: bool = False
    ):
        """
        Finds Pets by tags
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
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            'servers', server_index
        )
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            'paths/' + path + '/get/security',
            _security,
            security_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='get',
            host=host,
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


class FindPetsByTags(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    find_pets_by_tags = BaseApi._find_pets_by_tags


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    get = BaseApi._find_pets_by_tags
