# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

Discriminator: typing_extensions.TypeAlias = schemas.StrSchema[U]
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "discriminator": typing.Type[Discriminator],
    }
)

class AbstractStepMessage(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    Abstract Step
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            frozendict.frozendict,
        })
        required: typing.FrozenSet[str] = frozenset({
            "description",
            "discriminator",
            "sequenceNumber",
        })
        discriminator: typing.Mapping[str, typing.Mapping[str, typing.Type[schemas.Schema]]] = dataclasses.field(
            default_factory=lambda: {
                'discriminator': {
                    'AbstractStepMessage': AbstractStepMessage,
                }
            }
        )
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
        any_of: AnyOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AnyOf)) # type: ignore

    
    @property
    def description(self) -> schemas.AnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]:
        return self.__getitem__("description")
    
    @property
    def discriminator(self) -> Discriminator[str]:
        return self.__getitem__("discriminator")
    
    @property
    def sequenceNumber(self) -> schemas.AnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]:
        return self.__getitem__("sequenceNumber")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> schemas.AnyTypeSchema[typing.Union[
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
    def __getitem__(self, name: typing_extensions.Literal["discriminator"]) -> Discriminator[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequenceNumber"]) -> schemas.AnyTypeSchema[typing.Union[
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
            typing_extensions.Literal["description"],
            typing_extensions.Literal["discriminator"],
            typing_extensions.Literal["sequenceNumber"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        description: typing.Union[
            schemas.AnyTypeSchema[typing.Union[
                frozendict.frozendict,
                str,
                decimal.Decimal,
                schemas.BoolClass,
                schemas.NoneClass,
                tuple,
                bytes,
                schemas.FileIO
            ]],
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
        discriminator: typing.Union[
            Discriminator[str],
            str
        ],
        sequenceNumber: typing.Union[
            schemas.AnyTypeSchema[typing.Union[
                frozendict.frozendict,
                str,
                decimal.Decimal,
                schemas.BoolClass,
                schemas.NoneClass,
                tuple,
                bytes,
                schemas.FileIO
            ]],
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
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ) -> AbstractStepMessage[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            description=description,
            discriminator=discriminator,
            sequenceNumber=sequenceNumber,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            AbstractStepMessage[frozendict.frozendict],
            inst
        )
        return inst

AnyOf = typing.Tuple[
    typing.Type[AbstractStepMessage],
]