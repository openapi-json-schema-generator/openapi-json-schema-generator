# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

Items: typing_extensions.TypeAlias = schemas.NumberSchema


class ArrayNumberTuple(typing.Tuple[schemas.OUTPUT_BASE_TYPES]):
    def __getitem__(self, name: int) -> typing.Union[float, int]:
        return super().__getitem__(name)

    def __new__(cls, arg: ArrayNumberTupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ArrayNumber.validate(arg, configuration=configuration)
ArrayNumberTupleInput = typing.Sequence[
    typing.Union[
        float,
        int
    ],
]


@dataclasses.dataclass(frozen=True)
class ArrayNumber(
    schemas.ListSchema[ArrayNumberTuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: ArrayNumberTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ArrayNumberTupleInput,
            ArrayNumberTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ArrayNumberTuple:
        return super().validate(
            arg,
            configuration=configuration,
        )
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "ArrayNumber": typing.Type[ArrayNumber],
    }
)


class ArrayOfNumberOnlyDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ArrayNumber"]) -> ArrayNumberTuple:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["ArrayNumber"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: ArrayOfNumberOnlyDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ArrayOfNumberOnly.validate(arg, configuration=configuration)
    
    def __init__(self, arg: ArrayOfNumberOnlyDictInput, **kwargs: typing.Optional[schema_configuration.SchemaConfiguration]):
        super().__init__(arg)  # needed to omit passing on configuration in kwargs
ArrayOfNumberOnlyDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class ArrayOfNumberOnly(
    schemas.DictSchema[ArrayOfNumberOnlyDict]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            immutabledict.immutabledict: ArrayOfNumberOnlyDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ArrayOfNumberOnlyDictInput,
            ArrayOfNumberOnlyDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ArrayOfNumberOnlyDict:
        return super().validate(
            arg,
            configuration=configuration,
        )

