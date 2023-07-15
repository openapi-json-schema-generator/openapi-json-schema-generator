# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



@dataclasses.dataclass(frozen=True)
class Cultivar(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    pattern: schemas.PatternInfo = schemas.PatternInfo(
        pattern=r'^[a-zA-Z\s]*$'  # noqa: E501
    )


@dataclasses.dataclass(frozen=True)
class Origin(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    pattern: schemas.PatternInfo = schemas.PatternInfo(
        pattern=r'^[A-Z\s]*$',  # noqa: E501
        flags=re.I,
    )
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "cultivar": typing.Type[Cultivar],
        "origin": typing.Type[Origin],
    }
)


class AppleDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "cultivar",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "origin",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["cultivar"]) -> str:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["origin"]) -> str:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "cultivar":
            return typing.cast(
                str,
                val
            )
        elif name == "origin":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(key=key))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: AppleDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Apple.validate(arg, configuration=configuration)
AppleDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Apple(
    schemas.Schema[AppleDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.immutabledict,
    })
    required: typing.FrozenSet[str] = frozenset({
        "cultivar",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AppleDict,
        }
    )

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            AppleDictInput,
            AppleDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AppleDict: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )

