# coding: utf-8

"""
    Example
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from json_schema_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

SomeProp: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "someProp": typing.Type[SomeProp],
    }
)


class AnyTypeUnevaluatedPropertiesFalseWithPropertiesDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "someProp",
    })
    
    def __new__(
        cls,
        *,
        someProp: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("someProp", someProp),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(AnyTypeUnevaluatedPropertiesFalseWithPropertiesDictInput, arg_)
        return AnyTypeUnevaluatedPropertiesFalseWithProperties.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            AnyTypeUnevaluatedPropertiesFalseWithPropertiesDictInput,
            AnyTypeUnevaluatedPropertiesFalseWithPropertiesDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AnyTypeUnevaluatedPropertiesFalseWithPropertiesDict:
        return AnyTypeUnevaluatedPropertiesFalseWithProperties.validate(arg, configuration=configuration)
    
    @property
    def someProp(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("someProp", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
AnyTypeUnevaluatedPropertiesFalseWithPropertiesDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]
_Not: typing_extensions.TypeAlias = schemas.AnyTypeSchema


@dataclasses.dataclass(frozen=True)
class UnevaluatedProperties(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    not_: typing.Type[_Not] = dataclasses.field(default_factory=lambda: _Not) # type: ignore



@dataclasses.dataclass(frozen=True)
class AnyTypeUnevaluatedPropertiesFalseWithProperties(
    schemas.AnyTypeSchema[AnyTypeUnevaluatedPropertiesFalseWithPropertiesDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    unevaluated_properties: typing.Type[UnevaluatedProperties] = dataclasses.field(default_factory=lambda: UnevaluatedProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AnyTypeUnevaluatedPropertiesFalseWithPropertiesDict,
        }
    )

