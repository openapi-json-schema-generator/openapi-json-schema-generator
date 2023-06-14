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


class Shape(
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
                'shapeType': {
                    'Quadrilateral': quadrilateral.Quadrilateral,
                    'Triangle': triangle.Triangle,
                }
            }
        )
        one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore


    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[None, schemas.NoneClass],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Shape[schemas.NoneClass]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[bool, schemas.BoolClass],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Shape[schemas.BoolClass]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[decimal.Decimal, float, int],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Shape[decimal.Decimal]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Shape[str]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Sequence[schemas.INPUT_TYPES_ALL_INCL_SCHEMA],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Shape[tuple]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[
            DictInput,
            Shape[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Shape[frozendict.frozendict]: ...

    @typing.overload
    def __new__(
        cls,
        arg: bytes,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Shape[bytes]: ...

    @typing.overload
    def __new__(
        cls,
        arg: io.FileIO,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Shape[schemas.FileIO]: ...

    def __new__(
        cls,
        arg: schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ):
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )


from petstore_api.components.schema import quadrilateral
from petstore_api.components.schema import triangle
OneOf = typing.Tuple[
    typing.Type[triangle.Triangle],
    typing.Type[quadrilateral.Quadrilateral],
]
