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

from petstore_api.paths.fake_inline_composition.post.parameters.parameter_0 import schema
from petstore_api.paths.fake_inline_composition.post.parameters.parameter_1 import schema as schema_2
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "compositionAtRoot": typing.Type[schema.Schema],
        "compositionInProperty": typing.Type[schema_2.Schema],
    }
)


class QueryParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "compositionAtRoot",
        "compositionInProperty",
    })
    
    @property
    def compositionAtRoot(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("compositionAtRoot", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            val
        )
    
    @property
    def compositionInProperty(self) -> typing.Union[schema_2.SchemaDict, schemas.Unset]:
        val = self.get("compositionInProperty", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schema_2.SchemaDict,
            val
        )

    @staticmethod
    def from_dict_(
        arg: QueryParametersDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QueryParametersDict:
        return QueryParameters.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        compositionAtRoot: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        compositionInProperty: typing.Union[
            schema_2.SchemaDictInput,
            schema_2.SchemaDict,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("compositionAtRoot", compositionAtRoot),
            ("compositionInProperty", compositionInProperty),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        used_arg_ = typing.cast(QueryParametersDictInput, arg_)
        return QueryParameters.validate(used_arg_, configuration=configuration_)
QueryParametersDictInput = typing_extensions.TypedDict(
    'QueryParametersDictInput',
    {
        "compositionAtRoot": typing.Union[
            dict,
            schemas.immutabledict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ],
        "compositionInProperty": typing.Union[
            schema_2.SchemaDict,
            dict,
            schemas.immutabledict
        ],
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class QueryParameters(
    schemas.Schema[QueryParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
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

