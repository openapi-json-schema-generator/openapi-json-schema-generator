# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.components.headers.header_int32_json_content_type_header.content.application_json import schema as schema_2
from petstore_api.components.headers.header_number_header import schema as schema_4
from petstore_api.components.schema import string_with_validation
from petstore_api.paths.user_login.get.responses.response_200.headers.header_x_expires_after import schema as schema_3
from petstore_api.paths.user_login.get.responses.response_200.headers.header_x_rate_limit.content.application_json import schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "X-Rate-Limit": typing.Type[schema.Schema],
        "int32": typing.Type[schema_2.Schema],
        "X-Expires-After": typing.Type[schema_3.Schema],
        "ref-content-schema-header": typing.Type[string_with_validation.StringWithValidation],
        "numberHeader": typing.Type[schema_4.Schema],
    }
)
HeadersRequiredDictInput = typing_extensions.TypedDict(
    'HeadersRequiredDictInput',
    {
        "X-Rate-Limit": int,
        "int32": int,
        "ref-content-schema-header": str,
    }
)
HeadersOptionalDictInput = typing_extensions.TypedDict(
    'HeadersOptionalDictInput',
    {
        "X-Expires-After": typing.Union[
            str,
            datetime.datetime
        ],
        "numberHeader": typing.Union[
            str
        ],
    },
    total=False
)


class HeadersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "X-Rate-Limit",
        "int32",
        "ref-content-schema-header",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "X-Expires-After",
        "numberHeader",
    })
    
    @property
    def int32(self) -> int:
        return typing.cast(
            int,
            self.__getitem__("int32")
        )
    
    @property
    def numberHeader(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("numberHeader", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )

    @staticmethod
    def from_dict_(
        arg: HeadersDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeadersDict:
        return Headers.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        int32,
        numberHeader: typing.Union[
            schemas.Unset,
            typing.Any
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_ = {
            "int32": int32,
        }
        for key, val in (
            ("numberHeader", numberHeader),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        return Headers.validate(arg_, configuration=configuration_)


class HeadersDictInput(HeadersRequiredDictInput, HeadersOptionalDictInput):
    pass


@dataclasses.dataclass(frozen=True)
class Headers(
    schemas.Schema[HeadersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "X-Rate-Limit",
        "int32",
        "ref-content-schema-header",
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

