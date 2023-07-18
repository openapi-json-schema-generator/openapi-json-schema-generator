# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from petstore_api import api_client, security_schemes
from petstore_api.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .. import path
from .responses import response_200
from . import request_body
from petstore_api.paths.fake_pet_id_upload_image_with_required_file.post.request_body.content.multipart_form_data import schema as request_body_multipart_form_data_schema
from .parameters import parameter_0
from .security import security_requirement_object_0


AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.fake_pet_id_upload_image_with_required_file.post.parameters.parameter_0 import schema as parameter_0_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "petId": typing.Type[parameter_0_schema.Schema],
    }
)


class PathParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "petId",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def petId(self) -> int:
        return typing.cast(
            int,
            self.__getitem__("petId")
        )

    def __new__(cls, arg: PathParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return PathParameters.validate(arg, configuration=configuration)
PathParametersDictInput = typing_extensions.TypedDict(
    'PathParametersDictInput',
    {
        "petId": int,
    }
)


@dataclasses.dataclass(frozen=True)
class PathParameters(
    schemas.Schema[PathParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
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

_security: typing.List[security_schemes.SecurityRequirementObject] = [
    security_requirement_object_0.security_requirement_object,
]


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
    def _upload_file_with_required_file(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        body: typing.Union[
            request_body_multipart_form_data_schema.SchemaDictInput,
            request_body_multipart_form_data_schema.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        *,
        skip_deserialization: typing_extensions.Literal[False] = False,
        content_type: typing_extensions.Literal["multipart/form-data"] = "multipart/form-data",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_200.ApiResponse: ...

    @typing.overload
    def _upload_file_with_required_file(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        body: typing.Union[
            request_body_multipart_form_data_schema.SchemaDictInput,
            request_body_multipart_form_data_schema.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        *,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: typing_extensions.Literal["multipart/form-data"] = "multipart/form-data",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _upload_file_with_required_file(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        body: typing.Union[
            request_body_multipart_form_data_schema.SchemaDictInput,
            request_body_multipart_form_data_schema.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        *,
        skip_deserialization: bool = False,
        content_type: typing_extensions.Literal["multipart/form-data"] = "multipart/form-data",
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        uploads an image (required)
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
        _headers = self._get_headers(accept_content_types=accept_content_types)
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
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            "paths//fake/{petId}/uploadImageWithRequiredFile/post/security",
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


class UploadFileWithRequiredFile(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    upload_file_with_required_file = BaseApi._upload_file_with_required_file


class ApiForPost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    post = BaseApi._upload_file_with_required_file
