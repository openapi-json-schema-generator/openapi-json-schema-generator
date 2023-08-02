# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class ClassNameEnums:

    @schemas.classproperty
    def DANISH_PIG(cls) -> typing_extensions.Literal["DanishPig"]:
        return ClassName.validate("DanishPig")


@dataclasses.dataclass(frozen=True)
class ClassName(
    schemas.Schema[schemas.immutabledict, str]
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "DanishPig": "DANISH_PIG",
        }
    )
    enums = ClassNameEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["DanishPig"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["DanishPig"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["DanishPig",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "DanishPig",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "DanishPig",
            ],
            validated_arg
        )
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "className": typing.Type[ClassName],
    }
)


class DanishPigDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "className",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def className(self) -> typing_extensions.Literal["DanishPig"]:
        return typing.cast(
            typing_extensions.Literal["DanishPig"],
            self.__getitem__("className")
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)

    @staticmethod
    def from_dict_(
        arg: DanishPigDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DanishPigDict:
        return DanishPig.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        className: typing_extensions.Literal[
            "DanishPig"
        ],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_ = {
            "className": className,
        }
        arg_.update(kwargs)
        return DanishPig.validate(arg_, configuration=configuration_)
DanishPigDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class DanishPig(
    schemas.Schema[DanishPigDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "className",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: DanishPigDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            DanishPigDictInput,
            DanishPigDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DanishPigDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

