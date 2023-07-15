# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from petstore_api.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_json import schema as application_json_schema
from .headers import header_ref_schema_header
from .headers import header_int32
from .headers import header_ref_content_schema_header
from .headers import header_string_header
from .headers import header_number_header
parameters: typing.Dict[str, typing.Type[api_client.HeaderParameterWithoutName]] = {
    'ref-schema-header': header_ref_schema_header.RefSchemaHeader,
    'int32': header_int32.Int32,
    'ref-content-schema-header': header_ref_content_schema_header.RefContentSchemaHeader,
    'stringHeader': header_string_header.StringHeader,
    'numberHeader': header_number_header.NumberHeader,
}

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.components.headers.header_int32_json_content_type_header.content.application_json import schema as header_int32_json_content_type_header_schema
from petstore_api.components.headers.header_number_header import schema as header_number_header_schema
from petstore_api.components.headers.header_string_header import schema as header_string_header_schema
from petstore_api.components.schema import string_with_validation
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "ref-schema-header": typing.Type[string_with_validation.StringWithValidation],
        "int32": typing.Type[header_int32_json_content_type_header_schema.Schema],
        "ref-content-schema-header": typing.Type[string_with_validation.StringWithValidation],
        "stringHeader": typing.Type[header_string_header_schema.Schema],
        "numberHeader": typing.Type[header_number_header_schema.Schema],
    }
)
HeadersRequiredDictInput = typing_extensions.TypedDict(
    'HeadersRequiredDictInput',
    {
        "int32": int,
        "ref-content-schema-header": str,
        "ref-schema-header": str,
        "stringHeader": str,
    }
)
HeadersOptionalDictInput = typing_extensions.TypedDict(
    'HeadersOptionalDictInput',
    {
        "numberHeader": typing.Union[
            str
        ],
    },
    total=False
)


class HeadersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "int32",
        "ref-content-schema-header",
        "ref-schema-header",
        "stringHeader",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "numberHeader",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["int32"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["ref-content-schema-header"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["ref-schema-header"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["stringHeader"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["numberHeader"]) -> str:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "int32":
            return typing.cast(
                int,
                val
            )
        elif name == "ref-content-schema-header":
            return typing.cast(
                str,
                val
            )
        elif name == "ref-schema-header":
            return typing.cast(
                str,
                val
            )
        elif name == "stringHeader":
            return typing.cast(
                str,
                val
            )
        elif name == "numberHeader":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))

    def __new__(cls, arg: HeadersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Headers.validate(arg, configuration=configuration)


class HeadersDictInput(HeadersRequiredDictInput, HeadersOptionalDictInput):
    pass


@dataclasses.dataclass(frozen=True)
class Headers(
    schemas.Schema[HeadersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "int32",
        "ref-content-schema-header",
        "ref-schema-header",
        "stringHeader",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: HeadersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            HeadersDictInput,
            HeadersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeadersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass
class ApiResponse(api_response.ApiResponse):
    response: urllib3.HTTPResponse
    body: application_json_schema.api_response.ApiResponseDict
    headers: HeadersDict


class SuccessWithJsonApiResponse(api_client.OpenApiResponse[ApiResponse]):
    response_cls = ApiResponse


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema
    content = {
        'application/json': ApplicationJsonMediaType,
    }
    headers=parameters
    headers_schema = Headers
