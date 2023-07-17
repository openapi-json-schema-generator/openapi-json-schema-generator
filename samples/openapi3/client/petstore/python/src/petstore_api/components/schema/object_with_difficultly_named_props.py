# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

SpecialPropertyName: typing_extensions.TypeAlias = schemas.Int64Schema
_123List: typing_extensions.TypeAlias = schemas.StrSchema
_123Number: typing_extensions.TypeAlias = schemas.IntSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "$special[property.name]": typing.Type[SpecialPropertyName],
        "123-list": typing.Type[_123List],
        "123Number": typing.Type[_123Number],
    }
)


class ObjectWithDifficultlyNamedPropsDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "123-list",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "$special[property.name]",
        "123Number",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["123-list"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["$special[property.name]"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["123Number"]) -> int:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "123-list":
            return typing.cast(
                str,
                val
            )
        elif name == "$special[property.name]":
            return val if val is schemas.unset else typing.cast(
                int,
                val
            )
        elif name == "123Number":
            return val if val is schemas.unset else typing.cast(
                int,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    def get_additional_property_(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: ObjectWithDifficultlyNamedPropsDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectWithDifficultlyNamedProps.validate(arg, configuration=configuration)
ObjectWithDifficultlyNamedPropsDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ObjectWithDifficultlyNamedProps(
    schemas.Schema[ObjectWithDifficultlyNamedPropsDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    model with properties that have invalid names for python
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "123-list",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjectWithDifficultlyNamedPropsDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjectWithDifficultlyNamedPropsDictInput,
            ObjectWithDifficultlyNamedPropsDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjectWithDifficultlyNamedPropsDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

