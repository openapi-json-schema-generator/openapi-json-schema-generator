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
AdditionalProperties2: typing_extensions.TypeAlias = schemas.StrSchema[U]
"""todo define mapping here"""


class AdditionalProperties(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties2] = dataclasses.field(default_factory=lambda: AdditionalProperties2) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties2[str]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg_: typing.Mapping[
            str,
            typing.Union[
                AdditionalProperties2[str],
                str
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalProperties[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            AdditionalProperties[frozendict.frozendict],
            inst
        )
        return inst

"""todo define mapping here"""


class MapMapOfString(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties[frozendict.frozendict]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg_: typing.Mapping[
            str,
            typing.Union[
                AdditionalProperties[frozendict.frozendict],
                dict,
                frozendict.frozendict
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> MapMapOfString[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            MapMapOfString[frozendict.frozendict],
            inst
        )
        return inst

"""todo define mapping here"""


class AdditionalProperties3(
    schemas.StrSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "UPPER": "UPPER",
                "lower": "LOWER",
            }
        )
    
    @schemas.classproperty
    def UPPER(cls) -> AdditionalProperties3[str]:
        return cls("UPPER") # type: ignore
    
    @schemas.classproperty
    def LOWER(cls) -> AdditionalProperties3[str]:
        return cls("lower") # type: ignore
"""todo define mapping here"""


class MapOfEnumString(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties3] = dataclasses.field(default_factory=lambda: AdditionalProperties3) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties3[str]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg_: typing.Mapping[
            str,
            typing.Union[
                AdditionalProperties3[str],
                str
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> MapOfEnumString[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            MapOfEnumString[frozendict.frozendict],
            inst
        )
        return inst

"""todo define mapping here"""
AdditionalProperties4: typing_extensions.TypeAlias = schemas.BoolSchema[U]
"""todo define mapping here"""


class DirectMap(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties4] = dataclasses.field(default_factory=lambda: AdditionalProperties4) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties4[schemas.BoolClass]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg_: typing.Mapping[
            str,
            typing.Union[
                AdditionalProperties4[schemas.BoolClass],
                bool
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> DirectMap[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            DirectMap[frozendict.frozendict],
            inst
        )
        return inst

"""todo define mapping here"""
"""todo define mapping here"""


class MapTest(
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
    def __getitem__(self, name: typing_extensions.Literal["map_map_of_string"]) -> MapMapOfString[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_of_enum_string"]) -> MapOfEnumString[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direct_map"]) -> DirectMap[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["indirect_map"]) -> string_boolean_map.StringBooleanMap[frozendict.frozendict]: ...
    
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
            typing_extensions.Literal["map_map_of_string"],
            typing_extensions.Literal["map_of_enum_string"],
            typing_extensions.Literal["direct_map"],
            typing_extensions.Literal["indirect_map"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg_: typing.Union[
            DictInput,
            MapTest[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> MapTest[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            MapTest[frozendict.frozendict],
            inst
        )
        return inst


from petstore_api.components.schema import string_boolean_map
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "map_map_of_string": typing.Type[MapMapOfString],
        "map_of_enum_string": typing.Type[MapOfEnumString],
        "direct_map": typing.Type[DirectMap],
        "indirect_map": typing.Type[string_boolean_map.StringBooleanMap],
    }
)
