# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

A: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "a": typing.Type[A],
    }
)


class SpecialModelNameDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "a",
    })
    
    def get_property(self, name: typing_extensions.Literal["a"]) -> str:
        if name == "a":
            val = self.get(name, schemas.unset)
            if val is schemas.unset:
                return val
            return typing.cast(
                str,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: SpecialModelNameDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return SpecialModelName.validate(arg, configuration=configuration)
SpecialModelNameDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class SpecialModelName(
    schemas.Schema[SpecialModelNameDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    model with an invalid class name for python
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: SpecialModelNameDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            SpecialModelNameDictInput,
            SpecialModelNameDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SpecialModelNameDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

