# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *

Foo: typing_extensions.TypeAlias = schemas.StrSchema[U]
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "foo": typing.Type[Foo],
    }
)


class _Not(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo"]) -> Foo[str]: ...
    
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
            typing_extensions.Literal["foo"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        foo: typing.Union[
            Foo[str],
            schemas.Unset,
            str
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ) -> _Not[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            foo=foo,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            _Not[frozendict.frozendict],
            inst
        )
        return inst



class NotMoreComplexSchema(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        # any type
        not_: typing.Type[_Not] = dataclasses.field(default_factory=lambda: _Not) # type: ignore


    def __new__(
        cls,
        *args_: schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ) -> NotMoreComplexSchema[
        typing.Union[
            frozendict.frozendict,
            str,
            decimal.Decimal,
            schemas.BoolClass,
            schemas.NoneClass,
            tuple,
            bytes,
            schemas.FileIO
        ]
    ]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            NotMoreComplexSchema[
                typing.Union[
                    frozendict.frozendict,
                    str,
                    decimal.Decimal,
                    schemas.BoolClass,
                    schemas.NoneClass,
                    tuple,
                    bytes,
                    schemas.FileIO
                ]
            ],
            inst
        )
        return inst

