# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class QuadrilateralType(
    schemas.StrSchema[schemas.T]
):


    class Schema_:
        types = {
            str,
        }
        enum_value_to_name = {
            "SimpleQuadrilateral": "SIMPLE_QUADRILATERAL",
        }
    
    @schemas.classproperty
    def SIMPLE_QUADRILATERAL(cls):
        return cls("SimpleQuadrilateral") # type: ignore


class _1(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types = {frozendict.frozendict}
        properties: _1Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(_1Properties)) # type: ignore
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quadrilateralType"]) -> QuadrilateralType[str]: ...
    
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
            typing_extensions.Literal["quadrilateralType"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        quadrilateralType: typing.Union[
            QuadrilateralType[str],
            schemas.Unset,
            str
        ] = schemas.unset,
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
    ) -> _1[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            quadrilateralType=quadrilateralType,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            _1[frozendict.frozendict],
            inst
        )
        return inst



class SimpleQuadrilateral(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        # any type
        
        @staticmethod
        def all_of():
            return (
                quadrilateral_interface.QuadrilateralInterface,
                _1,
            )


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
    ) -> SimpleQuadrilateral[
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
            SimpleQuadrilateral[
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


from petstore_api.components.schema import quadrilateral_interface
_1Properties = typing_extensions.TypedDict(
    '_1Properties',
    {
        "quadrilateralType": QuadrilateralType,
    }
)
