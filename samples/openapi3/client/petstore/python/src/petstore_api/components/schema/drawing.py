# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class Shapes(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types = {tuple}
        
        @staticmethod
        def items():
            return shape.Shape

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                shape.Shape[typing.Union[
                    frozendict.frozendict,
                    str,
                    decimal.Decimal,
                    schemas.BoolClass,
                    schemas.NoneClass,
                    tuple,
                    bytes,
                    schemas.FileIO
                ]],
                dict,
                frozendict.frozendict,
                str,
                datetime.date,
                datetime.datetime,
                uuid.UUID,
                int,
                float,
                decimal.Decimal,
                bool,
                None,
                list,
                tuple,
                bytes,
                io.FileIO,
                io.BufferedReader
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> Shapes[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Shapes[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> shape.Shape[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]:
        return super().__getitem__(name)



class Drawing(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types = {frozendict.frozendict}
        properties: DrawingProperties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(DrawingProperties)) # type: ignore
        
        @staticmethod
        def additional_properties():
            return fruit.Fruit
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mainShape"]) -> shape.Shape[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapeOrNull"]) -> shape_or_null.ShapeOrNull[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nullableShape"]) -> nullable_shape.NullableShape[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapes"]) -> Shapes[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> fruit.Fruit[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["mainShape"],
            typing_extensions.Literal["shapeOrNull"],
            typing_extensions.Literal["nullableShape"],
            typing_extensions.Literal["shapes"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        mainShape: typing.Union[
            shape.Shape[typing.Union[
                frozendict.frozendict,
                str,
                decimal.Decimal,
                schemas.BoolClass,
                schemas.NoneClass,
                tuple,
                bytes,
                schemas.FileIO
            ]],
            schemas.Unset,
            dict,
            frozendict.frozendict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ] = schemas.unset,
        shapeOrNull: typing.Union[
            shape_or_null.ShapeOrNull[typing.Union[
                frozendict.frozendict,
                str,
                decimal.Decimal,
                schemas.BoolClass,
                schemas.NoneClass,
                tuple,
                bytes,
                schemas.FileIO
            ]],
            schemas.Unset,
            dict,
            frozendict.frozendict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ] = schemas.unset,
        nullableShape: typing.Union[
            nullable_shape.NullableShape[typing.Union[
                frozendict.frozendict,
                str,
                decimal.Decimal,
                schemas.BoolClass,
                schemas.NoneClass,
                tuple,
                bytes,
                schemas.FileIO
            ]],
            schemas.Unset,
            dict,
            frozendict.frozendict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ] = schemas.unset,
        shapes: typing.Union[
            Shapes[tuple],
            schemas.Unset,
            list,
            tuple
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            fruit.Fruit[typing.Union[
                frozendict.frozendict,
                str,
                decimal.Decimal,
                schemas.BoolClass,
                schemas.NoneClass,
                tuple,
                bytes,
                schemas.FileIO
            ]],
            dict,
            frozendict.frozendict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ],
    ) -> Drawing[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            mainShape=mainShape,
            shapeOrNull=shapeOrNull,
            nullableShape=nullableShape,
            shapes=shapes,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            Drawing[frozendict.frozendict],
            inst
        )
        return inst


from petstore_api.components.schema import fruit
from petstore_api.components.schema import nullable_shape
from petstore_api.components.schema import shape
from petstore_api.components.schema import shape_or_null
DrawingProperties = typing.TypedDict(
    'DrawingProperties',
    {
        "mainShape": shape.Shape,
        "shapeOrNull": shape_or_null.ShapeOrNull,
        "nullableShape": nullable_shape.NullableShape,
        "shapes": Shapes,
    }
)
