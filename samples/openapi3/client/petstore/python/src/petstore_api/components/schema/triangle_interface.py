# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class ShapeType(
    schemas.StrSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "Triangle": "TRIANGLE",
            }
        )
    
    @schemas.classproperty
    def TRIANGLE(cls) -> ShapeType[str]:
        return cls("Triangle") # type: ignore
TriangleType: typing_extensions.TypeAlias = schemas.StrSchema[U]
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "shapeType": typing.Type[ShapeType],
        "triangleType": typing.Type[TriangleType],
    }
)

class TriangleInterface(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        # any type
        required: typing.FrozenSet[str] = frozenset({
            "shapeType",
            "triangleType",
        })
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore

    
    @property
    def shapeType(self) -> ShapeType[str]:
        return self.__getitem__("shapeType")
    
    @property
    def triangleType(self) -> TriangleType[str]:
        return self.__getitem__("triangleType")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapeType"]) -> ShapeType[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triangleType"]) -> TriangleType[str]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.AnyTypeSchema[typing.Union[
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
            typing_extensions.Literal["shapeType"],
            typing_extensions.Literal["triangleType"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[
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
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            dict,
            frozendict.frozendict,
            list,
            tuple,
            decimal.Decimal,
            float,
            int,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            bool,
            None,
            bytes,
            io.FileIO,
            io.BufferedReader,
            schemas.Schema
        ],
    ) -> TriangleInterface[
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
            TriangleInterface[
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

