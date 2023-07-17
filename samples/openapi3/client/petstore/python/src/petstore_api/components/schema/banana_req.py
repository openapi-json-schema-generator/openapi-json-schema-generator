# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema
LengthCm: typing_extensions.TypeAlias = schemas.NumberSchema
Sweet: typing_extensions.TypeAlias = schemas.BoolSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "lengthCm": typing.Type[LengthCm],
        "sweet": typing.Type[Sweet],
    }
)
BananaReqRequiredDictInput = typing_extensions.TypedDict(
    'BananaReqRequiredDictInput',
    {
        "lengthCm": typing.Union[
            float,
            int
        ],
    }
)
BananaReqOptionalDictInput = typing_extensions.TypedDict(
    'BananaReqOptionalDictInput',
    {
        "sweet": bool,
    },
    total=False
)


class BananaReqDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "lengthCm",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "sweet",
    })
    
    @property
    def get_property(self, name: typing_extensions.Literal["lengthCm"]) -> typing.Union[int, float]:
        if name == "lengthCm":
            return typing.cast(
                typing.Union[int, float],
                self.__getitem__(name)
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    @property
    def get_property(self, name: typing_extensions.Literal["sweet"]) -> bool:
        if name == "sweet":
            val = self.get(name, schemas.unset)
            if val is schemas.unset:
                return val
            return typing.cast(
                bool,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))

    def __new__(cls, arg: BananaReqDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return BananaReq.validate(arg, configuration=configuration)


class BananaReqDictInput(BananaReqRequiredDictInput, BananaReqOptionalDictInput):
    pass


@dataclasses.dataclass(frozen=True)
class BananaReq(
    schemas.Schema[BananaReqDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "lengthCm",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: BananaReqDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            BananaReqDictInput,
            BananaReqDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> BananaReqDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

