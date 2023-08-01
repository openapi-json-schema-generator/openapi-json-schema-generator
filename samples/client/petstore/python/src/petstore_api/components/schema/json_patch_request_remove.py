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
Path: typing_extensions.TypeAlias = schemas.StrSchema


class OpEnums:

    @schemas.classproperty
    def REMOVE(cls) -> typing_extensions.Literal["remove"]:
        return Op.validate("remove")


@dataclasses.dataclass(frozen=True)
class Op(
    schemas.Schema[schemas.immutabledict, str]
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "remove": "REMOVE",
        }
    )
    enums = OpEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["remove"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["remove"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["remove",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "remove",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "remove",
            ],
            validated_arg
        )
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "path": typing.Type[Path],
        "op": typing.Type[Op],
    }
)


class JSONPatchRequestRemoveDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "op",
        "path",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def op(self) -> typing_extensions.Literal["remove"]:
        return typing.cast(
            typing_extensions.Literal["remove"],
            self.__getitem__("op")
        )
    
    @property
    def path(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("path")
        )

    @staticmethod
    def from_dict_(
        arg: JSONPatchRequestRemoveDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> JSONPatchRequestRemoveDict:
        return JSONPatchRequestRemove.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        op,
        path,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_ = {
            "op": op,
            "path": path,
        }
        return JSONPatchRequestRemove.validate(arg_, configuration=configuration_)
JSONPatchRequestRemoveDictInput = typing_extensions.TypedDict(
    'JSONPatchRequestRemoveDictInput',
    {
        "op": str,
        "path": str,
    }
)


@dataclasses.dataclass(frozen=True)
class JSONPatchRequestRemove(
    schemas.Schema[JSONPatchRequestRemoveDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "op",
        "path",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: JSONPatchRequestRemoveDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            JSONPatchRequestRemoveDictInput,
            JSONPatchRequestRemoveDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> JSONPatchRequestRemoveDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

