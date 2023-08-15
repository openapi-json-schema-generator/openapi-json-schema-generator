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

from petstore_api.paths.fake.get.parameters.parameter_2 import schema as schema_4
from petstore_api.paths.fake.get.parameters.parameter_3 import schema as schema_2
from petstore_api.paths.fake.get.parameters.parameter_4 import schema as schema_3
from petstore_api.paths.fake.get.parameters.parameter_5 import schema
Properties = typing.TypedDict(
    'Properties',
    {
        "enum_query_double": typing.Type[schema.Schema],
        "enum_query_string": typing.Type[schema_2.Schema],
        "enum_query_integer": typing.Type[schema_3.Schema],
        "enum_query_string_array": typing.Type[schema_4.Schema],
    }
)


class QueryParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "enum_query_double",
        "enum_query_string",
        "enum_query_integer",
        "enum_query_string_array",
    })
    
    def __new__(
        cls,
        *,
        enum_query_double: typing.Union[
            int,
            float,
            schemas.Unset
        ] = schemas.unset,
        enum_query_string: typing.Union[
            typing.Literal[
                "_abc",
                "-efg",
                "(xyz)"
            ],
            schemas.Unset
        ] = schemas.unset,
        enum_query_integer: typing.Union[
            typing.Literal[
                1,
                -2
            ],
            schemas.Unset
        ] = schemas.unset,
        enum_query_string_array: typing.Union[
            schema_4.SchemaTupleInput,
            schema_4.SchemaTuple,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("enum_query_double", enum_query_double),
            ("enum_query_string", enum_query_string),
            ("enum_query_integer", enum_query_integer),
            ("enum_query_string_array", enum_query_string_array),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        used_arg_ = typing.cast(QueryParametersDictInput, arg_)
        return QueryParameters.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QueryParametersDict:
        return QueryParameters.validate(arg, configuration=configuration)
    
    @property
    def enum_query_double(self) -> typing.Union[int, float, schemas.Unset]:
        val = self.get("enum_query_double", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Union[int, float],
            val
        )
    
    @property
    def enum_query_string(self) -> typing.Union[typing.Literal["_abc", "-efg", "(xyz)"], schemas.Unset]:
        val = self.get("enum_query_string", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal["_abc", "-efg", "(xyz)"],
            val
        )
    
    @property
    def enum_query_integer(self) -> typing.Union[typing.Literal[1, -2], schemas.Unset]:
        val = self.get("enum_query_integer", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal[1, -2],
            val
        )
    
    @property
    def enum_query_string_array(self) -> typing.Union[schema_4.SchemaTuple, schemas.Unset]:
        val = self.get("enum_query_string_array", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schema_4.SchemaTuple,
            val
        )
QueryParametersDictInput = typing.TypedDict(
    'QueryParametersDictInput',
    {
        "enum_query_double": typing.Union[
            int,
            float
        ],
        "enum_query_string": typing.Literal[
            "_abc",
            "-efg",
            "(xyz)"
        ],
        "enum_query_integer": typing.Literal[
            1,
            -2
        ],
        "enum_query_string_array": typing.Union[
            schema_4.SchemaTupleInput,
            schema_4.SchemaTuple
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

