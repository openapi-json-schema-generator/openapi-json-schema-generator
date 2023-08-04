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


class CapitalizationDict(schemas.immutabledict[str, str]):

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
    @staticmethod
    def from_dict_(
        arg: CapitalizationDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> CapitalizationDict:
        return Capitalization.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        *,
        smallCamel: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        CapitalCamel: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        small_Snake: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        Capital_Snake: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        SCA_ETH_Flow_Points: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        ATT_NAME: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("smallCamel", smallCamel),
            ("CapitalCamel", CapitalCamel),
            ("small_Snake", small_Snake),
            ("Capital_Snake", Capital_Snake),
            ("SCA_ETH_Flow_Points", SCA_ETH_Flow_Points),
            ("ATT_NAME", ATT_NAME),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(CapitalizationDictInput, arg_)
        return Capitalization.validate(used_arg_, configuration=configuration_)

    
    @property
    def smallCamel(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("smallCamel", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def CapitalCamel(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("CapitalCamel", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def small_Snake(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("small_Snake", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def Capital_Snake(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("Capital_Snake", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def SCA_ETH_Flow_Points(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("SCA_ETH_Flow_Points", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def ATT_NAME(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("ATT_NAME", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
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

