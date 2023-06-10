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
Items: typing_extensions.TypeAlias = schemas.StrSchema[U]
"""todo define mapping here"""


class ArrayOfString(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                Items[str],
                str
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ArrayOfString[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ArrayOfString[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items[str]:
        return super().__getitem__(name)

"""todo define mapping here"""
Items3: typing_extensions.TypeAlias = schemas.Int64Schema[U]
"""todo define mapping here"""


class Items2(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items3] = dataclasses.field(default_factory=lambda: Items3) # type: ignore

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                Items3[decimal.Decimal],
                decimal.Decimal,
                int
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Items2[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Items2[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items3[decimal.Decimal]:
        return super().__getitem__(name)

"""todo define mapping here"""


class ArrayArrayOfInteger(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items2] = dataclasses.field(default_factory=lambda: Items2) # type: ignore

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                Items2[tuple],
                list,
                tuple
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ArrayArrayOfInteger[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ArrayArrayOfInteger[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items2[tuple]:
        return super().__getitem__(name)

"""todo define mapping here"""
"""todo define mapping here"""


class Items4(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[read_only_first.ReadOnlyFirst] = dataclasses.field(default_factory=lambda: read_only_first.ReadOnlyFirst) # type: ignore

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                read_only_first.ReadOnlyFirst[frozendict.frozendict],
                dict,
                frozendict.frozendict
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Items4[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Items4[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> read_only_first.ReadOnlyFirst[frozendict.frozendict]:
        return super().__getitem__(name)

"""todo define mapping here"""


class ArrayArrayOfModel(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items4] = dataclasses.field(default_factory=lambda: Items4) # type: ignore

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                Items4[tuple],
                list,
                tuple
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ArrayArrayOfModel[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ArrayArrayOfModel[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items4[tuple]:
        return super().__getitem__(name)

Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "array_of_string": typing.Type[ArrayOfString],
        "array_array_of_integer": typing.Type[ArrayArrayOfInteger],
        "array_array_of_model": typing.Type[ArrayArrayOfModel],
    }
)
"""todo define mapping here"""


class ArrayTest(
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
    def __getitem__(self, name: typing_extensions.Literal["array_of_string"]) -> ArrayOfString[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_array_of_integer"]) -> ArrayArrayOfInteger[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_array_of_model"]) -> ArrayArrayOfModel[tuple]: ...
    
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
            typing_extensions.Literal["array_of_string"],
            typing_extensions.Literal["array_array_of_integer"],
            typing_extensions.Literal["array_array_of_model"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg_: typing.Union[
            DictInput,
            ArrayTest[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ArrayTest[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ArrayTest[frozendict.frozendict],
            inst
        )
        return inst


from petstore_api.components.schema import read_only_first
