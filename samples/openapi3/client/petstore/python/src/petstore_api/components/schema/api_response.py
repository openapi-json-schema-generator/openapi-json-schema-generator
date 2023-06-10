# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

"""todo define mapping here"""
Code: typing_extensions.TypeAlias = schemas.Int32Schema[U]
"""todo define mapping here"""
Type: typing_extensions.TypeAlias = schemas.StrSchema[U]
"""todo define mapping here"""
Message: typing_extensions.TypeAlias = schemas.StrSchema[U]
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "code": typing.Type[Code],
        "type": typing.Type[Type],
        "message": typing.Type[Message],
    }
)
"""todo define mapping here"""


class ApiResponse(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> Code[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> Type[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> Message[str]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.AnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["code"],
            typing_extensions.Literal["type"],
            typing_extensions.Literal["message"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg_: typing.Union[
            DictInput,
            ApiResponse[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ApiResponse[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ApiResponse[frozendict.frozendict],
            inst
        )
        return inst

