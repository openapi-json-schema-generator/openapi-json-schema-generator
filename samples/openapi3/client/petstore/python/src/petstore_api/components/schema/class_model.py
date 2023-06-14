# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

_Class: typing_extensions.TypeAlias = schemas.StrSchema[U]
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "_class": typing.Type[_Class],
    }
)
DictInput = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            _Class[str],
            str
        ],
        schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ]
]


class ClassModel(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    Model for testing model with "_class" property
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        # any type
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_class"]) -> _Class[str]: ...
    
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
            typing_extensions.Literal["_class"],
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
    ) -> ClassModel[schemas.NoneClass]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[bool, schemas.BoolClass],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ClassModel[schemas.BoolClass]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[decimal.Decimal, float, int],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ClassModel[decimal.Decimal]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ClassModel[str]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Sequence[
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ClassModel[tuple]: ...

    @typing.overload
    def __new__(
        cls,
        arg: typing.Union[
            DictInput,
            ClassModel[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ClassModel[frozendict.frozendict]: ...

    @typing.overload
    def __new__(
        cls,
        arg: bytes,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ClassModel[bytes]: ...

    @typing.overload
    def __new__(
        cls,
        arg: io.FileIO,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ClassModel[schemas.FileIO]: ...

    def __new__(
        cls,
        arg: schemas.INPUT_TYPES_ALL_INCL_SCHEMA,
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ):
        inst = super().__new__(
            cls,
            arg,
            configuration=configuration,
        )
        inst = typing.cast(
            ClassModel[
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

