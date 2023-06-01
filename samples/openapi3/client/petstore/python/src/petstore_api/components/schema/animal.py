# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

ClassName: typing_extensions.TypeAlias = schemas.StrSchema[U]


class Color(
    schemas.StrSchema[schemas.T]
):


    class Schema_:
        types = {
            str,
        }
        default = "red"


class Animal(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "className",
        }
        
        @staticmethod
        def discriminator():
            return {
                'className': {
                    'Cat': cat.Cat,
                    'Dog': dog.Dog,
                }
            }
        properties: AnimalProperties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(AnimalProperties)) # type: ignore
    
    @property
    def className(self) -> ClassName[str]:
        return self.__getitem__("className")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["className"]) -> ClassName[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> Color[str]: ...
    
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
            typing_extensions.Literal["className"],
            typing_extensions.Literal["color"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        className: typing.Union[
            ClassName[str],
            str
        ],
        color: typing.Union[
            Color[str],
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
    ) -> Animal[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            className=className,
            color=color,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            Animal[frozendict.frozendict],
            inst
        )
        return inst


from petstore_api.components.schema import cat
from petstore_api.components.schema import dog
AnimalProperties = typing.TypedDict(
    'AnimalProperties',
    {
        "className": ClassName,
        "color": Color,
    }
)
