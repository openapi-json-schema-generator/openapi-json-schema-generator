# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class Cultivar(
    schemas.StrSchema[schemas.T]
):


    class Schema_:
        types = {
            str,
        }
        regex={
            'pattern': r'^[a-zA-Z\s]*$',  # noqa: E501
        }


class Origin(
    schemas.StrSchema[schemas.T]
):


    class Schema_:
        types = {
            str,
        }
        regex={
            'pattern': r'^[A-Z\s]*$',  # noqa: E501
            'flags': re.I,
        }


class Apple(
    schemas.NoneBase,
    schemas.DictBase,
    schemas.Schema[schemas.T],
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types = {
            schemas.NoneClass,
            frozendict.frozendict,
        }
        required = {
            "cultivar",
        }
        properties: AppleProperties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(AppleProperties)) # type: ignore

    
    @property
    def cultivar(self) -> Cultivar[str]:
        return self.__getitem__("cultivar")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cultivar"]) -> Cultivar[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin"]) -> Origin[str]: ...
    
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
            typing_extensions.Literal["cultivar"],
            typing_extensions.Literal["origin"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[
            None,
            dict,
            frozendict.frozendict
        ],
        origin: typing.Union[
            Origin[str],
            schemas.Unset,
            str
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            dict,
            frozendict.frozendict,
            list,
            tuple,
            decimal.Decimal,
            float,
            int,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            bool,
            None,
            bytes,
            io.FileIO,
            io.BufferedReader,
            schemas.Schema
        ],
    ) -> Apple[
        typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]
    ]:
        inst = super().__new__(
            cls,
            *args_,
            origin=origin,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            Apple[
                typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]
            ],
            inst
        )
        return inst

AppleProperties = typing_extensions.TypedDict(
    'AppleProperties',
    {
        "cultivar": typing.Type[Cultivar],
        "origin": typing.Type[Origin],
    }
)
