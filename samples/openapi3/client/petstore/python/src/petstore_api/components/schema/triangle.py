# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class Triangle(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        # any type
        discriminator: typing.Mapping[str, typing.Mapping[str, typing.Type[schemas.Schema]]] = dataclasses.field(
            default_factory=lambda: {
                'triangleType': {
                    'EquilateralTriangle': equilateral_triangle.EquilateralTriangle,
                    'IsoscelesTriangle': isosceles_triangle.IsoscelesTriangle,
                    'ScaleneTriangle': scalene_triangle.ScaleneTriangle,
                }
            }
        )
        one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore


    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[None, schemas.NoneClass],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Triangle[schemas.NoneClass]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[bool, schemas.BoolClass],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Triangle[schemas.BoolClass]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[decimal.Decimal, float, int],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Triangle[decimal.Decimal]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Triangle[str]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Sequence[
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Triangle[tuple]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[
            DictInput,
            Triangle[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Triangle[frozendict.frozendict]: ...

    @typing.overload
    def __new__(
        cls,
        arg: bytes,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Triangle[bytes]: ...

    @typing.overload
    def __new__(
        cls,
        arg: io.FileIO,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Triangle[schemas.FileIO]: ...

    def __new__(
        cls,
        arg: schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ):
        inst = super().__new__(
            cls,
            arg,
            configuration=configuration,
        )
        inst = typing.cast(
            Triangle[
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


from petstore_api.components.schema import equilateral_triangle
from petstore_api.components.schema import isosceles_triangle
from petstore_api.components.schema import scalene_triangle
OneOf = typing.Tuple[
    typing.Type[equilateral_triangle.EquilateralTriangle],
    typing.Type[isosceles_triangle.IsoscelesTriangle],
    typing.Type[scalene_triangle.ScaleneTriangle],
]
