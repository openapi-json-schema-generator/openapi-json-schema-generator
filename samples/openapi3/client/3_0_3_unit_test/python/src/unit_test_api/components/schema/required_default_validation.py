# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *

DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]
Foo: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "foo": typing.Type[Foo],
    }
)
DictInput2 = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            Foo[
                schemas.INPUT_BASE_TYPES
            ],
            dict,
            frozendict.frozendict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ],
        schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ]
]


class RequiredDefaultValidation(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        # any type
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo"]) -> Foo[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
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

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[None, schemas.NoneClass],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> RequiredDefaultValidation[schemas.NoneClass]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[bool, schemas.BoolClass],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> RequiredDefaultValidation[schemas.BoolClass]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[decimal.Decimal, float, int],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> RequiredDefaultValidation[decimal.Decimal]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> RequiredDefaultValidation[str]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Sequence[schemas.INPUT_TYPES_ALL_INCL_SCHEMA],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> RequiredDefaultValidation[tuple]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[
            DictInput2,
            RequiredDefaultValidation[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> RequiredDefaultValidation[frozendict.frozendict]: ...

    @typing.overload
    def __new__(
        cls,
        arg: bytes,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> RequiredDefaultValidation[bytes]: ...

    @typing.overload
    def __new__(
        cls,
        arg: io.FileIO,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> RequiredDefaultValidation[schemas.FileIO]: ...

    def __new__(
        cls,
        arg: schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ):
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )

