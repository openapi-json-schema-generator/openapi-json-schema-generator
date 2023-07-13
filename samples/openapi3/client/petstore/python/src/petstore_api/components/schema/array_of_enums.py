# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


from petstore_api.components.schema import string_enum


class ArrayOfEnumsTuple(
    typing.Tuple[
        typing.Union[
            None,
            typing_extensions.Literal["placed", "approved", "delivered", "single quoted", "multiple\nlines", "double quote \n with newline"],
        ],
        ...
    ]
):
    def __getitem__(self, name: int) -> typing.Union[
        None,
        typing_extensions.Literal["placed", "approved", "delivered", "single quoted", "multiple\nlines", "double quote \n with newline"],
    ]:
        return super().__getitem__(name)

    def __new__(cls, arg: ArrayOfEnumsTupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ArrayOfEnums.validate(arg, configuration=configuration)
ArrayOfEnumsTupleInput = typing.Union[
    typing.List[
        typing.Union[
            None,
            str
        ],
    ],
    typing.Tuple[
        typing.Union[
            None,
            str
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class ArrayOfEnums(
    schemas.Schema[schemas.immutabledict, ArrayOfEnumsTuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[string_enum.StringEnum] = dataclasses.field(default_factory=lambda: string_enum.StringEnum) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: ArrayOfEnumsTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ArrayOfEnumsTupleInput,
            ArrayOfEnumsTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ArrayOfEnumsTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
