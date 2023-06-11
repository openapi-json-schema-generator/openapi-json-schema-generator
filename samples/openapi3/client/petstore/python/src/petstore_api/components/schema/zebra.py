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


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "plains": "PLAINS",
                "mountain": "MOUNTAIN",
                "grevys": "GREVYS",
            }
        )
    
    @schemas.classproperty
    def PLAINS(cls) -> Type[str]:
        return cls("plains") # type: ignore
    
    @schemas.classproperty
    def MOUNTAIN(cls) -> Type[str]:
        return cls("mountain") # type: ignore
    
    @schemas.classproperty
    def GREVYS(cls) -> Type[str]:
        return cls("grevys") # type: ignore


class ClassName(
    schemas.StrSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "zebra": "ZEBRA",
            }
        )
    
    @schemas.classproperty
    def ZEBRA(cls) -> ClassName[str]:
        return cls("zebra") # type: ignore
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "type": typing.Type[Type],
        "className": typing.Type[ClassName],
    }
)
# todo properties mapping with required and optional and addprops


class Zebra(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        required: typing.FrozenSet[str] = frozenset({
            "className",
        })
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
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
        arg_: typing.Union[
            DictInput2,
            Zebra[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Zebra[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Zebra[frozendict.frozendict],
            inst
        )
        return inst

