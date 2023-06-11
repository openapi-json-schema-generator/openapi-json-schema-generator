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
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[shape.Shape] = dataclasses.field(default_factory=lambda: shape.Shape) # type: ignore

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                shape.Shape[
                    schemas.INPUT_BASE_TYPES
                ],
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
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
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

DictInput = typing.Mapping[
    str,
    typing.Union[
        AdditionalProperties[
            schemas.INPUT_BASE_TYPES
        ],
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
]


class Drawing(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
        additional_properties: typing.Type[fruit.Fruit] = dataclasses.field(default_factory=lambda: fruit.Fruit) # type: ignore
    
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
        arg_: typing.Union[
            DictInput,
            Drawing[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Drawing[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
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
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "mainShape": typing.Type[shape.Shape],
        "shapeOrNull": typing.Type[shape_or_null.ShapeOrNull],
        "nullableShape": typing.Type[nullable_shape.NullableShape],
        "shapes": typing.Type[Shapes],
    }
)
