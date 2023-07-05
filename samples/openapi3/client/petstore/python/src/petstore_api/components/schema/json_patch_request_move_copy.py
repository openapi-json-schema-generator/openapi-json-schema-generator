# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema
_From: typing_extensions.TypeAlias = schemas.StrSchema
Path: typing_extensions.TypeAlias = schemas.StrSchema


class OpEnums:

    @schemas.classproperty
    def MOVE(cls) -> str:
        return Op.validate("move")

    @schemas.classproperty
    def COPY(cls) -> str:
        return Op.validate("copy")


@dataclasses.dataclass(frozen=True)
class Op(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, bool, schemas.none_type_], str] = dataclasses.field(
        default_factory=lambda: {
            "move": "MOVE",
            "copy": "COPY",
        }
    )
    enums = OpEnums
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "from": typing.Type[_From],
        "path": typing.Type[Path],
        "op": typing.Type[Op],
    }
)


class JSONPatchRequestMoveCopyDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def op(self) -> str:
        return self.__getitem__("op")
    
    @property
    def path(self) -> str:
        return self.__getitem__("path")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["from"],
            typing_extensions.Literal["op"],
            typing_extensions.Literal["path"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: JSONPatchRequestMoveCopyDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return JSONPatchRequestMoveCopy.validate(arg, configuration=configuration)
    
    def __init__(self, arg: JSONPatchRequestMoveCopyDictInput, **kwargs: typing.Optional[schema_configuration.SchemaConfiguration]):
        super().__init__(arg)  # needed to omit passing on configuration in kwargs
JSONPatchRequestMoveCopyDictInput = typing_extensions.TypedDict(
    'JSONPatchRequestMoveCopyDictInput',
    {
        "from": str,
        "op": str,
        "path": str,
    }
)


@dataclasses.dataclass(frozen=True)
class JSONPatchRequestMoveCopy(
    schemas.DictSchema[JSONPatchRequestMoveCopyDict]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "from",
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
            immutabledict.immutabledict: JSONPatchRequestMoveCopyDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            JSONPatchRequestMoveCopyDictInput,
            JSONPatchRequestMoveCopyDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> JSONPatchRequestMoveCopyDict:
        return super().validate(
            arg,
            configuration=configuration,
        )

