# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *
from petstore_api import api_client, security_schemes
from petstore_api.shared_imports.operation_imports import *

from .. import path
from .responses import response_400
from .parameters import (
    parameter_0,
    parameter_1,
)
from .security import (
    security_requirement_object_0,
    security_requirement_object_1,
)


AdditionalProperties2: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.pet_pet_id.delete.parameters.parameter_0 import schema as parameter_0_schema
Properties2 = typing_extensions.TypedDict(
    'Properties2',
    {
        "api_key": typing.Type[parameter_0_schema.Schema],
    }
)


class HeaderParametersDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_key"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["api_key"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: HeaderParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return HeaderParameters.validate(arg, configuration=configuration)
    
    def __init__(self, arg: HeaderParametersDictInput, **kwargs: typing.Optional[schema_configuration.SchemaConfiguration]):
        super().__init__(arg)  # needed to omit passing on configuration in kwargs
HeaderParametersDictInput = typing_extensions.TypedDict(
    'HeaderParametersDictInput',
    {
        "api_key": str,
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class HeaderParameters(
    schemas.DictSchema[HeaderParametersDict]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    properties: Properties2 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties2)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties2] = dataclasses.field(default_factory=lambda: AdditionalProperties2) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            immutabledict.immutabledict: HeaderParametersDict
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
        return super().validate(
            arg,
            configuration=configuration,
        )


AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.pet_pet_id.delete.parameters.parameter_1 import schema as parameter_1_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "petId": typing.Type[parameter_1_schema.Schema],
    }
)


class PathParametersDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def petId(self) -> int:
        return self.__getitem__("petId")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["petId"]) -> int:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["petId"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: PathParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return PathParameters.validate(arg, configuration=configuration)
    
    def __init__(self, arg: PathParametersDictInput, **kwargs: typing.Optional[schema_configuration.SchemaConfiguration]):
        super().__init__(arg)  # needed to omit passing on configuration in kwargs
PathParametersDictInput = typing_extensions.TypedDict(
    'PathParametersDictInput',
    {
        "petId": int,
    }
)


@dataclasses.dataclass(frozen=True)
class PathParameters(
    schemas.DictSchema[PathParametersDict]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "petId",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            immutabledict.immutabledict: PathParametersDict
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
        return super().validate(
            arg,
            configuration=configuration,
        )

header_parameter_classes = (
    parameter_0.Parameter0,
)
path_parameter_classes = (
    parameter_1.Parameter1,
)

_security: typing.List[security_schemes.SecurityRequirementObject] = [
    security_requirement_object_0.security_requirement_object,
    security_requirement_object_1.security_requirement_object,
]


__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '400': typing.Type[response_400.ResponseFor400],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '400': response_400.ResponseFor400,
}


class BaseApi(api_client.Api):
    @typing.overload
    def _delete_pet(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
            None
        ] = None,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = False
    ) -> api_response.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _delete_pet(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
            None
        ] = None,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[True] = ...
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _delete_pet(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
            None
        ] = None,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        skip_deserialization: bool = False
    ):
        """
        Deletes a pet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        path_params = PathParameters.validate(path_params)
        if header_params is not None:
            header_params = HeaderParameters.validate(header_params)
        used_path = self._get_used_path(
            path,
            path_parameters=path_parameter_classes,
            path_params=path_params
        )
        _headers = self._get_headers(
            header_parameters=header_parameter_classes,
            header_params=header_params,
            skip_validation=True
        )
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            'servers', server_index
        )
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            'paths/' + path + '/delete/security',
            _security,
            security_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='delete',
            host=host,
            headers=_headers,
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


class DeletePet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    delete_pet = BaseApi._delete_pet


class ApiForDelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    delete = BaseApi._delete_pet
