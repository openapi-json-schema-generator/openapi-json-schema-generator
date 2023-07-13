# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


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
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["myNumber"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["myString"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["myBoolean"]) -> bool:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["myNumber"],
            typing_extensions.Literal["myString"],
            typing_extensions.Literal["myBoolean"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: ObjectModelWithRefPropsDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectModelWithRefProps.validate(arg, configuration=configuration)
ObjectModelWithRefPropsDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


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

