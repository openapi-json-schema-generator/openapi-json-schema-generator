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
    def BASQUE_PIG(cls) -> typing.Literal["BasquePig"]:
        return ClassName.validate("BasquePig")


@dataclasses.dataclass(frozen=True)
class ClassName(
    schemas.Schema[schemas.immutabledict, str]
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "BasquePig": "BASQUE_PIG",
        }
    )
    enums = ClassNameEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["BasquePig"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["BasquePig"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["BasquePig",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "BasquePig",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "BasquePig",
            ],
            validated_arg
        )
Properties = typing.TypedDict(
    'Properties',
    {
        "className": typing.Type[ClassName],
    }
)


class BasquePigDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "className",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        className: typing.Literal[
            "BasquePig"
        ],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "className": className,
        }
        arg_.update(kwargs)
        used_arg_ = typing.cast(BasquePigDictInput, arg_)
        return BasquePig.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            BasquePigDictInput,
            BasquePigDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> BasquePigDict:
        return BasquePig.validate(arg, configuration=configuration)
    
    @property
    def className(self) -> typing.Literal["BasquePig"]:
        return typing.cast(
            typing.Literal["BasquePig"],
            self.__getitem__("className")
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
BasquePigDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class BasquePig(
    schemas.Schema[BasquePigDict, tuple]
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
            schemas.immutabledict: BasquePigDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            BasquePigDictInput,
            BasquePigDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> BasquePigDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

