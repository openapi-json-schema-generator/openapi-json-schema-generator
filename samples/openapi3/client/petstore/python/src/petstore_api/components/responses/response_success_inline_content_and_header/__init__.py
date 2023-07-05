# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *
from petstore_api.shared_imports.response_imports import *

from . import content
from .headers import header_some_header
parameters: typing.Dict[str, typing.Type[api_client.HeaderParameterWithoutName]] = {
    'someHeader': header_some_header.SomeHeader,
}

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.components.responses.response_success_inline_content_and_header.headers.header_some_header import schema as header_some_header_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "someHeader": typing.Type[header_some_header_schema.Schema],
    }
)


class HeadersDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someHeader"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["someHeader"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: HeadersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Headers.validate(arg, configuration=configuration)
HeadersDictInput = typing_extensions.TypedDict(
    'HeadersDictInput',
    {
        "someHeader": str,
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class Headers(
    schemas.DictSchema[HeadersDict]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            immutabledict.immutabledict: HeadersDict
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
        return super().validate(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass
class ApiSuccessInlineContentAndHeader(api_response.ApiResponse):
    response: urllib3.HTTPResponse
    body: content.application_json.schema.SchemaDict
    headers: HeadersDict


class SuccessInlineContentAndHeader(api_client.OpenApiResponse[ApiSuccessInlineContentAndHeader]):
    response_cls = ApiSuccessInlineContentAndHeader


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = content.application_json.schema.Schema
    Content = typing_extensions.TypedDict(
        'Content',
        {
            'application/json': typing.Type[ApplicationJsonMediaType],
        }
    )
    content: Content = {
        'application/json': ApplicationJsonMediaType,
    }
    headers=parameters
    headers_schema = Headers
