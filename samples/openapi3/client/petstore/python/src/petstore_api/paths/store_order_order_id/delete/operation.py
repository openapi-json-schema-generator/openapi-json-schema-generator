# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from petstore_api import api_client, exceptions
from petstore_api.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .. import path
from .responses import (
    response_400,
    response_404,
)
from .parameters import parameter_0


AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.store_order_order_id.delete.parameters.parameter_0 import schema as parameter_0_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "order_id": typing.Type[parameter_0_schema.Schema],
    }
)


class PathParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "order_id",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def get_order_id(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("order_id")
        )

    def __new__(cls, arg: PathParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return PathParameters.validate(arg, configuration=configuration)
PathParametersDictInput = typing_extensions.TypedDict(
    'PathParametersDictInput',
    {
        "order_id": str,
    }
)


@dataclasses.dataclass(frozen=True)
class PathParameters(
    schemas.Schema[PathParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "order_id",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: PathParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            PathParametersDictInput,
            PathParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PathParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

path_parameter_classes = (
    parameter_0.Parameter0,
)


__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '400': typing.Type[response_400.ResponseFor400],
        '404': typing.Type[response_404.ResponseFor404],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '400': response_400.ResponseFor400,
    '404': response_404.ResponseFor404,
}
_error_status_codes = frozenset({
    '400',
    '404',
})


class BaseApi(api_client.Api):
    @typing.overload
    def _delete_order(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        *,
        skip_deserialization: typing_extensions.Literal[False] = False,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _delete_order(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        *,
        skip_deserialization: typing_extensions.Literal[True],
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _delete_order(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        *,
        skip_deserialization: bool = False,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        Delete purchase order by ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        path_params = PathParameters.validate(path_params)
        used_path, query_params_suffix = self._get_used_path(
            path,
            path_parameters=path_parameter_classes,
            path_params=path_params
        )
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='delete',
            host=host,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            skip_deser_response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
            self._verify_response_status(skip_deser_response)
            return skip_deser_response

        status = str(raw_response.status)
        if status in _error_status_codes:
            error_status_code = typing.cast(
                typing_extensions.Literal[
                    '400',
                    '404',
                ],
                status
            )
            error_response = _status_code_to_response[error_status_code].deserialize(
                raw_response, self.api_client.schema_configuration)
            raise exceptions.ApiException(
                status=error_response.response.status,
                reason=error_response.response.reason,
                api_response=error_response
            )

        response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        self._verify_response_status(response)
        return response


class DeleteOrder(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    delete_order = BaseApi._delete_order


class ApiForDelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    delete = BaseApi._delete_order
