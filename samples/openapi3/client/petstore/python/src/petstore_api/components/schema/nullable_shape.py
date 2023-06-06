# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

_2: typing_extensions.TypeAlias = schemas.NoneSchema[U]


class NullableShape(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    The value may be a shape or the 'null' value. For a composed schema to validate a null payload, one of its chosen oneOf schemas must be type null or nullable (introduced in OAS schema >= 3.0)
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        # any type
        one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore


    def __new__(
        cls,
        *args_: schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ) -> NullableShape[
        typing.Union[
            frozendict.frozendict,
            str,
            decimal.Decimal,
            schemas.BoolClass,
            schemas.NoneClass,
            tuple,
            bytes,
            schemas.FileIO
        ]
    ]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            NullableShape[
                typing.Union[
                    frozendict.frozendict,
                    str,
                    decimal.Decimal,
                    schemas.BoolClass,
                    schemas.NoneClass,
                    tuple,
                    bytes,
                    schemas.FileIO
                ]
            ],
            inst
        )
        return inst


from petstore_api.components.schema import quadrilateral
from petstore_api.components.schema import triangle
OneOf = typing.Tuple[
    typing.Type[triangle.Triangle],
    typing.Type[quadrilateral.Quadrilateral],
    typing.Type[_2[schemas.U]],
]
