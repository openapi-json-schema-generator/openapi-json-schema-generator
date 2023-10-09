# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.AnyTypeSchema
Foo: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "foo": typing.Type[Foo],
    }
)


class UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "foo",
    })
    
    def __new__(
        cls,
        *,
        foo: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("foo", foo),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDictInput, arg_)
        return UnevaluatedpropertiesWithAdjacentAdditionalproperties.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDictInput,
            UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDict:
        return UnevaluatedpropertiesWithAdjacentAdditionalproperties.validate(arg, configuration=configuration)
    
    @property
    def foo(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("foo", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            val
        )
UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]
UnevaluatedProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema


@dataclasses.dataclass(frozen=True)
class UnevaluatedpropertiesWithAdjacentAdditionalproperties(
    schemas.Schema[UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    unevaluated_properties: typing.Type[UnevaluatedProperties] = dataclasses.field(default_factory=lambda: UnevaluatedProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDictInput,
            UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> UnevaluatedpropertiesWithAdjacentAdditionalpropertiesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

