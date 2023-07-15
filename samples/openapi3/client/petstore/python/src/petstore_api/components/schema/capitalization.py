# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

SmallCamel: typing_extensions.TypeAlias = schemas.StrSchema
CapitalCamel: typing_extensions.TypeAlias = schemas.StrSchema
SmallSnake: typing_extensions.TypeAlias = schemas.StrSchema
CapitalSnake: typing_extensions.TypeAlias = schemas.StrSchema
SCAETHFlowPoints: typing_extensions.TypeAlias = schemas.StrSchema
ATTNAME: typing_extensions.TypeAlias = schemas.StrSchema
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


class CapitalizationDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "smallCamel",
        "CapitalCamel",
        "small_Snake",
        "Capital_Snake",
        "SCA_ETH_Flow_Points",
        "ATT_NAME",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["smallCamel"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["CapitalCamel"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["small_Snake"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["Capital_Snake"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["SCA_ETH_Flow_Points"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["ATT_NAME"]) -> str:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "smallCamel":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "CapitalCamel":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "small_Snake":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "Capital_Snake":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "SCA_ETH_Flow_Points":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "ATT_NAME":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(key=key))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: CapitalizationDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Capitalization.validate(arg, configuration=configuration)
CapitalizationDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Capitalization(
    schemas.Schema[CapitalizationDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: CapitalizationDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            CapitalizationDictInput,
            CapitalizationDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> CapitalizationDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

