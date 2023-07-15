# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


from petstore_api.components.schema import array_with_validations_in_items
from petstore_api.components.schema import from_schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "from": typing.Type[from_schema.FromSchema],
        "!reference": typing.Type[array_with_validations_in_items.ArrayWithValidationsInItems],
    }
)


class ObjectWithInvalidNamedRefedPropertiesDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "!reference",
        "from",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["!reference"]) -> array_with_validations_in_items.ArrayWithValidationsInItemsTuple:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["from"]) -> from_schema.FromSchemaDict:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "!reference":
            return typing.cast(
                array_with_validations_in_items.ArrayWithValidationsInItemsTuple,
                val
            )
        elif name == "from":
            return typing.cast(
                from_schema.FromSchemaDict,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(key=key))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: ObjectWithInvalidNamedRefedPropertiesDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectWithInvalidNamedRefedProperties.validate(arg, configuration=configuration)
ObjectWithInvalidNamedRefedPropertiesDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ObjectWithInvalidNamedRefedProperties(
    schemas.Schema[ObjectWithInvalidNamedRefedPropertiesDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "!reference",
        "from",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjectWithInvalidNamedRefedPropertiesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjectWithInvalidNamedRefedPropertiesDictInput,
            ObjectWithInvalidNamedRefedPropertiesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjectWithInvalidNamedRefedPropertiesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

