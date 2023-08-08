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

from petstore_api.components.headers.header_int32_json_content_type_header.content.application_json import schema
from petstore_api.components.headers.header_number_header import schema as schema_3
from petstore_api.components.headers.header_string_header import schema as schema_2
from petstore_api.components.schema import string_with_validation
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "ref-schema-header": typing.Type[string_with_validation.StringWithValidation],
        "int32": typing.Type[schema.Schema],
        "ref-content-schema-header": typing.Type[string_with_validation.StringWithValidation],
        "stringHeader": typing.Type[schema_2.Schema],
        "numberHeader": typing.Type[schema_3.Schema],
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
        "numberHeader": str,
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
    
    def __new__(
        cls,
        *,
        int32: int,
        stringHeader: str,
        numberHeader: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "int32": int32,
            "stringHeader": stringHeader,
        }
        for key, val in (
            ("numberHeader", numberHeader),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        used_arg_ = typing.cast(HeadersDictInput, arg_)
        return Headers.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            HeadersDictInput,
            HeadersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeadersDict:
        return Headers.validate(arg, configuration=configuration)
    
    @property
    def int32(self) -> int:
        return typing.cast(
            int,
            self.__getitem__("int32")
        )
    
    @property
    def stringHeader(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("stringHeader")
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

