# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


from petstore_api.components.schema import boolean
from petstore_api.components.schema import number_with_validations
from petstore_api.components.schema import string
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "myNumber": typing.Type[number_with_validations.NumberWithValidations],
        "myString": typing.Type[string.String],
        "myBoolean": typing.Type[boolean.Boolean],
    }
)


class ObjectModelWithRefPropsDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "myNumber",
        "myString",
        "myBoolean",
    })
    
    @property
    def myNumber(self) -> typing.Union[int, float, schemas.Unset]:
        val = self.get("myNumber", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            typing.Union[int, float],
            val
        )
    
    @property
    def myString(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("myString", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def myBoolean(self) -> typing.Union[bool, schemas.Unset]:
        val = self.get("myBoolean", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            bool,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)

    def __new__(cls, arg: ObjectModelWithRefPropsDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectModelWithRefProps.validate(arg, configuration=configuration)
ObjectModelWithRefPropsDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ObjectModelWithRefProps(
    schemas.Schema[ObjectModelWithRefPropsDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    a model that includes properties which should stay primitive (String + Boolean) and one which is defined as a class, NumberWithValidations
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjectModelWithRefPropsDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjectModelWithRefPropsDictInput,
            ObjectModelWithRefPropsDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjectModelWithRefPropsDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

