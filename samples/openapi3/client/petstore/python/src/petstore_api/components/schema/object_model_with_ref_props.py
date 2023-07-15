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
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["myNumber"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["myString"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["myBoolean"]) -> bool:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "myNumber":
            return val if val is schemas.unset else typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "myString":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        elif name == "myBoolean":
            return val if val is schemas.unset else typing.cast(
                bool,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(key=key))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

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

