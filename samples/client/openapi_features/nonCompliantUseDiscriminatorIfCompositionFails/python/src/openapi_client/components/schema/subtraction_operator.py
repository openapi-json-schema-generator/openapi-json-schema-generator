# coding: utf-8

"""
    discriminator-test
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from openapi_client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema
A: typing_extensions.TypeAlias = schemas.Float64Schema
B: typing_extensions.TypeAlias = schemas.Float64Schema


@dataclasses.dataclass(frozen=True)
class OperatorId(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: typing.Literal["SUB"] = "SUB"
Properties = typing.TypedDict(
    'Properties',
    {
        "a": typing.Type[A],
        "b": typing.Type[B],
        "operator_id": typing.Type[OperatorId],
    }
)


class SubtractionOperatorDict(schemas.immutabledict[str, typing.Union[
    str,
    typing.Union[int, float],
]]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "a",
        "b",
        "operator_id",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        a: typing.Union[
            int,
            float
        ],
        b: typing.Union[
            int,
            float
        ],
        operator_id: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "a": a,
            "b": b,
            "operator_id": operator_id,
        }
        used_arg_ = typing.cast(SubtractionOperatorDictInput, arg_)
        return SubtractionOperator.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            SubtractionOperatorDictInput,
            SubtractionOperatorDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SubtractionOperatorDict:
        return SubtractionOperator.validate(arg, configuration=configuration)
    
    @property
    def a(self) -> typing.Union[int, float]:
        return typing.cast(
            typing.Union[int, float],
            self.__getitem__("a")
        )
    
    @property
    def b(self) -> typing.Union[int, float]:
        return typing.cast(
            typing.Union[int, float],
            self.__getitem__("b")
        )
    
    @property
    def operator_id(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("operator_id")
        )
SubtractionOperatorDictInput = typing.TypedDict(
    'SubtractionOperatorDictInput',
    {
        "a": typing.Union[
            int,
            float
        ],
        "b": typing.Union[
            int,
            float
        ],
        "operator_id": str,
    }
)


@dataclasses.dataclass(frozen=True)
class SubtractionOperator(
    schemas.Schema[SubtractionOperatorDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "a",
        "b",
        "operator_id",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: SubtractionOperatorDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            SubtractionOperatorDictInput,
            SubtractionOperatorDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SubtractionOperatorDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

