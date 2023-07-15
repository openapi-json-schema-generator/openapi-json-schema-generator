# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class ReqPropsFromUnsetAddPropsDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "invalid-name",
        "validName",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["invalid-name"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["validName"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "invalid-name":
            return typing.cast(
                schemas.OUTPUT_BASE_TYPES,
                val
            )
        elif name == "validName":
            return typing.cast(
                schemas.OUTPUT_BASE_TYPES,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(key=key))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: ReqPropsFromUnsetAddPropsDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ReqPropsFromUnsetAddProps.validate(arg, configuration=configuration)
ReqPropsFromUnsetAddPropsDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ReqPropsFromUnsetAddProps(
    schemas.Schema[ReqPropsFromUnsetAddPropsDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "invalid-name",
        "validName",
    })
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ReqPropsFromUnsetAddPropsDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ReqPropsFromUnsetAddPropsDictInput,
            ReqPropsFromUnsetAddPropsDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ReqPropsFromUnsetAddPropsDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

