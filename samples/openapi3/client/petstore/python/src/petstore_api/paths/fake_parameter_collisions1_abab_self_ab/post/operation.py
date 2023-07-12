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
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.request_body.content.application_json import schema as request_body_application_json_schema
from .parameters import (
    parameter_0,
    parameter_1,
    parameter_2,
    parameter_3,
    parameter_4,
    parameter_5,
    parameter_6,
    parameter_7,
    parameter_8,
    parameter_9,
    parameter_10,
    parameter_11,
    parameter_12,
    parameter_13,
    parameter_14,
    parameter_15,
    parameter_16,
    parameter_17,
    parameter_18,
)


AdditionalProperties2: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_0 import schema as parameter_0_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_1 import schema as parameter_1_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_2 import schema as parameter_2_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_3 import schema as parameter_3_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_4 import schema as parameter_4_schema
Properties2 = typing_extensions.TypedDict(
    'Properties2',
    {
        "1": typing.Type[parameter_0_schema.Schema],
        "aB": typing.Type[parameter_1_schema.Schema],
        "Ab": typing.Type[parameter_2_schema.Schema],
        "A-B": typing.Type[parameter_4_schema.Schema],
        "self": typing.Type[parameter_3_schema.Schema],
    }
)


class QueryParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["1"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aB"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Ab"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["A-B"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["1"],
            typing_extensions.Literal["aB"],
            typing_extensions.Literal["Ab"],
            typing_extensions.Literal["A-B"],
            typing_extensions.Literal["self"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: QueryParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return QueryParameters.validate(arg, configuration=configuration)
QueryParametersDictInput = typing_extensions.TypedDict(
    'QueryParametersDictInput',
    {
        "1": str,
        "aB": str,
        "Ab": str,
        "A-B": str,
        "self": str,
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class QueryParameters(
    schemas.Schema[QueryParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties2 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties2)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties2] = dataclasses.field(default_factory=lambda: AdditionalProperties2) # type: ignore
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


AdditionalProperties3: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_5 import schema as parameter_5_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_6 import schema as parameter_6_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_7 import schema as parameter_7_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_8 import schema as parameter_8_schema
Properties3 = typing_extensions.TypedDict(
    'Properties3',
    {
        "1": typing.Type[parameter_5_schema.Schema],
        "aB": typing.Type[parameter_6_schema.Schema],
        "A-B": typing.Type[parameter_8_schema.Schema],
        "self": typing.Type[parameter_7_schema.Schema],
    }
)


class HeaderParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["1"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aB"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["A-B"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["1"],
            typing_extensions.Literal["aB"],
            typing_extensions.Literal["A-B"],
            typing_extensions.Literal["self"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: HeaderParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return HeaderParameters.validate(arg, configuration=configuration)
HeaderParametersDictInput = typing_extensions.TypedDict(
    'HeaderParametersDictInput',
    {
        "1": str,
        "aB": str,
        "A-B": str,
        "self": str,
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class HeaderParameters(
    schemas.Schema[HeaderParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties3 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties3)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties3] = dataclasses.field(default_factory=lambda: AdditionalProperties3) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: HeaderParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeaderParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )


AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_10 import schema as parameter_10_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_11 import schema as parameter_11_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_12 import schema as parameter_12_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_13 import schema as parameter_13_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_9 import schema as parameter_9_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "1": typing.Type[parameter_9_schema.Schema],
        "aB": typing.Type[parameter_10_schema.Schema],
        "Ab": typing.Type[parameter_11_schema.Schema],
        "A-B": typing.Type[parameter_13_schema.Schema],
        "self": typing.Type[parameter_12_schema.Schema],
    }
)


class PathParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def Ab(self) -> str:
        return self.__getitem__("Ab")
    
    @property
    def aB(self) -> str:
        return self.__getitem__("aB")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["1"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["A-B"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Ab"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aB"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["1"],
            typing_extensions.Literal["A-B"],
            typing_extensions.Literal["Ab"],
            typing_extensions.Literal["aB"],
            typing_extensions.Literal["self"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: PathParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return PathParameters.validate(arg, configuration=configuration)
PathParametersDictInput = typing_extensions.TypedDict(
    'PathParametersDictInput',
    {
        "1": str,
        "A-B": str,
        "Ab": str,
        "aB": str,
        "self": str,
    }
)


@dataclasses.dataclass(frozen=True)
class PathParameters(
    schemas.Schema[PathParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "1",
        "A-B",
        "Ab",
        "aB",
        "self",
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


AdditionalProperties4: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_14 import schema as parameter_14_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_15 import schema as parameter_15_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_16 import schema as parameter_16_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_17 import schema as parameter_17_schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_18 import schema as parameter_18_schema
Properties4 = typing_extensions.TypedDict(
    'Properties4',
    {
        "1": typing.Type[parameter_14_schema.Schema],
        "aB": typing.Type[parameter_15_schema.Schema],
        "Ab": typing.Type[parameter_16_schema.Schema],
        "A-B": typing.Type[parameter_18_schema.Schema],
        "self": typing.Type[parameter_17_schema.Schema],
    }
)


class CookieParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["1"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aB"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Ab"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["A-B"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["1"],
            typing_extensions.Literal["aB"],
            typing_extensions.Literal["Ab"],
            typing_extensions.Literal["A-B"],
            typing_extensions.Literal["self"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: CookieParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return CookieParameters.validate(arg, configuration=configuration)
CookieParametersDictInput = typing_extensions.TypedDict(
    'CookieParametersDictInput',
    {
        "1": str,
        "aB": str,
        "Ab": str,
        "A-B": str,
        "self": str,
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class CookieParameters(
    schemas.Schema[CookieParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties4 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties4)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties4] = dataclasses.field(default_factory=lambda: AdditionalProperties4) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: CookieParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            CookieParametersDictInput,
            CookieParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> CookieParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

query_parameter_classes = (
    parameter_0.Parameter0,
    parameter_1.Parameter1,
    parameter_2.Parameter2,
    parameter_3.Parameter3,
    parameter_4.Parameter4,
)
header_parameter_classes = (
    parameter_5.Parameter5,
    parameter_6.Parameter6,
    parameter_7.Parameter7,
    parameter_8.Parameter8,
)
path_parameter_classes = (
    parameter_9.Parameter9,
    parameter_10.Parameter10,
    parameter_11.Parameter11,
    parameter_12.Parameter12,
    parameter_13.Parameter13,
)
cookie_parameter_classes = (
    parameter_9.Parameter9,
    parameter_10.Parameter10,
    parameter_11.Parameter11,
    parameter_12.Parameter12,
    parameter_13.Parameter13,
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
    def _parameter_collisions(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        body: typing.Union[
            schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
            None
        ] = None,
        cookie_params: typing.Union[
            CookieParametersDictInput,
            CookieParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: typing_extensions.Literal[False] = False,
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_200.ApiResponse: ...

    @typing.overload
    def _parameter_collisions(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        body: typing.Union[
            schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
            None
        ] = None,
        cookie_params: typing.Union[
            CookieParametersDictInput,
            CookieParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _parameter_collisions(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        body: typing.Union[
            schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
            None
        ] = None,
        cookie_params: typing.Union[
            CookieParametersDictInput,
            CookieParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: bool = False,
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        parameter collision case
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        path_params = PathParameters.validate(path_params)
        if query_params is not None:
            query_params = QueryParameters.validate(query_params)
        if header_params is not None:
            header_params = HeaderParameters.validate(header_params)
        if cookie_params is not None:
            cookie_params = CookieParameters.validate(cookie_params)
        used_path, query_params_suffix = self._get_used_path(
            path,
            path_parameters=path_parameter_classes,
            path_params=path_params,
            query_parameters=query_parameter_classes,
            query_params=query_params
        )
        _headers = self._get_headers(
            header_parameters=header_parameter_classes,
            header_params=header_params,
            accept_content_types=accept_content_types,
            skip_validation=True
        )
        # TODO add cookie handling

        _fields, _body = self._get_fields_and_body(
            request_body=request_body.RequestBody,
            body=body,
            headers=_headers,
            content_type=content_type
        )
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            query_params_suffix=query_params_suffix,
            method='post',
            host=host,
            headers=_headers,
            fields=_fields,
            body=_body,
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


class ParameterCollisions(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    parameter_collisions = BaseApi._parameter_collisions


class ApiForPost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    post = BaseApi._parameter_collisions
