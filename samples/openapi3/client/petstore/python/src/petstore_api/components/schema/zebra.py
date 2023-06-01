# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

AdditionalProperties: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]


class Type(
    schemas.StrSchema[schemas.T]
):


    class Schema_:
        types = {
            str,
        }
        enum_value_to_name = {
            "plains": "PLAINS",
            "mountain": "MOUNTAIN",
            "grevys": "GREVYS",
        }
    
    @schemas.classproperty
    def PLAINS(cls):
        return cls("plains") # type: ignore
    
    @schemas.classproperty
    def MOUNTAIN(cls):
        return cls("mountain") # type: ignore
    
    @schemas.classproperty
    def GREVYS(cls):
        return cls("grevys") # type: ignore


class ClassName(
    schemas.StrSchema[schemas.T]
):


    class Schema_:
        types = {
            str,
        }
        enum_value_to_name = {
            "zebra": "ZEBRA",
        }
    
    @schemas.classproperty
    def ZEBRA(cls):
        return cls("zebra") # type: ignore


class Zebra(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "className",
        }
        properties: ZebraProperties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(ZebraProperties)) # type: ignore
        
        @staticmethod
        def additional_properties():
            return AdditionalProperties
    
    @property
    def className(self) -> ClassName[str]:
        return self.__getitem__("className")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["className"]) -> ClassName[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> Type[str]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> AdditionalProperties[typing.Union[
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
            typing_extensions.Literal["className"],
            typing_extensions.Literal["type"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        className: typing.Union[
            ClassName[str],
            str
        ],
        type: typing.Union[
            Type[str],
            schemas.Unset,
            str
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            AdditionalProperties[typing.Union[
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
    ) -> Zebra[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            className=className,
            type=type,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            Zebra[frozendict.frozendict],
            inst
        )
        return inst

ZebraProperties = typing_extensions.TypedDict(
    'ZebraProperties',
    {
        "type": Type,
        "className": ClassName,
    }
)
