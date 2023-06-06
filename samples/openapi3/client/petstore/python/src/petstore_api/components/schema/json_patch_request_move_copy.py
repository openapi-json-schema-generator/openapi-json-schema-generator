# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema[U]
_From: typing_extensions.TypeAlias = schemas.StrSchema[U]
Path: typing_extensions.TypeAlias = schemas.StrSchema[U]


class Op(
    schemas.StrSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "move": "MOVE",
                "copy": "COPY",
            }
        )
    
    @schemas.classproperty
    def MOVE(cls) -> Op[str]:
        return cls("move") # type: ignore
    
    @schemas.classproperty
    def COPY(cls) -> Op[str]:
        return cls("copy") # type: ignore
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "from": typing.Type[_From],
        "path": typing.Type[Path],
        "op": typing.Type[Op],
    }
)


class JSONPatchRequestMoveCopy(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        required: typing.FrozenSet[str] = frozenset({
            "from",
            "op",
            "path",
        })
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
    @property
    def op(self) -> Op[str]:
        return self.__getitem__("op")
    
    @property
    def path(self) -> Path[str]:
        return self.__getitem__("path")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> _From[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op"]) -> Op[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> Path[str]: ...
    
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

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        op: typing.Union[
            Op[str],
            str
        ],
        path: typing.Union[
            Path[str],
            str
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> JSONPatchRequestMoveCopy[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            op=op,
            path=path,
            configuration_=configuration_,
        )
        inst = typing.cast(
            JSONPatchRequestMoveCopy[frozendict.frozendict],
            inst
        )
        return inst

