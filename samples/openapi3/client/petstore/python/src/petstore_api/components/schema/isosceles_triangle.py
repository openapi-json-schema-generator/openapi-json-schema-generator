# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class IsoscelesTriangle(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        class AllOf:
        
            @staticmethod
            def _0() -> typing.Type[triangle_interface.TriangleInterface]:
                return triangle_interface.TriangleInterface
            
            
            class _1(
                schemas.DictSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    
                    class Properties:
                        
                        
                        class TriangleType(
                            schemas.StrSchema[schemas.T]
                        ):
                        
                        
                            class Schema_:
                                types = {
                                    str,
                                }
                                enum_value_to_name = {
                                    "IsoscelesTriangle": "ISOSCELES_TRIANGLE",
                                }
                            
                            @schemas.classproperty
                            def ISOSCELES_TRIANGLE(cls):
                                return cls("IsoscelesTriangle") # type: ignore
                        __annotations__ = {
                            "triangleType": TriangleType,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["triangleType"]) -> Schema_.Properties.TriangleType[str]: ...
                
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
                        typing_extensions.Literal["triangleType"],
                        str
                    ]
                ):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    triangleType: typing.Union[
                        Schema_.Properties.TriangleType,
                        schemas.Unset,
                        str
                    ] = schemas.unset,
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                ) -> IsoscelesTriangle.Schema_.AllOf._1[frozendict.frozendict]:
                    inst = super().__new__(
                        cls,
                        *args_,
                        triangleType=triangleType,
                        configuration_=configuration_,
                        **kwargs,
                    )
                    inst = typing.cast(
                        IsoscelesTriangle.Schema_.AllOf._1[frozendict.frozendict],
                        inst
                    )
                    return inst
            classes = [
                _0,
                _1,
            ]


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
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> IsoscelesTriangle[
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
            IsoscelesTriangle[
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

from petstore_api.components.schema import triangle_interface
