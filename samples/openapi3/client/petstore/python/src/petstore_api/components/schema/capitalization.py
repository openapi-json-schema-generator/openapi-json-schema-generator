# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

"""todo define mapping here"""
SmallCamel: typing_extensions.TypeAlias = schemas.StrSchema[U]
"""todo define mapping here"""
CapitalCamel: typing_extensions.TypeAlias = schemas.StrSchema[U]
"""todo define mapping here"""
SmallSnake: typing_extensions.TypeAlias = schemas.StrSchema[U]
"""todo define mapping here"""
CapitalSnake: typing_extensions.TypeAlias = schemas.StrSchema[U]
"""todo define mapping here"""
SCAETHFlowPoints: typing_extensions.TypeAlias = schemas.StrSchema[U]
"""todo define mapping here"""
ATTNAME: typing_extensions.TypeAlias = schemas.StrSchema[U]
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "smallCamel": typing.Type[SmallCamel],
        "CapitalCamel": typing.Type[CapitalCamel],
        "small_Snake": typing.Type[SmallSnake],
        "Capital_Snake": typing.Type[CapitalSnake],
        "SCA_ETH_Flow_Points": typing.Type[SCAETHFlowPoints],
        "ATT_NAME": typing.Type[ATTNAME],
    }
)
"""todo define mapping here"""


class Capitalization(
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
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smallCamel"]) -> SmallCamel[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CapitalCamel"]) -> CapitalCamel[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["small_Snake"]) -> SmallSnake[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Capital_Snake"]) -> CapitalSnake[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SCA_ETH_Flow_Points"]) -> SCAETHFlowPoints[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ATT_NAME"]) -> ATTNAME[str]: ...
    
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
            typing_extensions.Literal["smallCamel"],
            typing_extensions.Literal["CapitalCamel"],
            typing_extensions.Literal["small_Snake"],
            typing_extensions.Literal["Capital_Snake"],
            typing_extensions.Literal["SCA_ETH_Flow_Points"],
            typing_extensions.Literal["ATT_NAME"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg_: typing.Union[
            DictInput,
            Capitalization[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Capitalization[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Capitalization[frozendict.frozendict],
            inst
        )
        return inst

