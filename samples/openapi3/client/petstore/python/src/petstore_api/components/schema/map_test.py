# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

AdditionalProperties2: typing_extensions.TypeAlias = schemas.StrSchema[U]
DictInput = typing.Mapping[
    str,
    typing.Union[
        AdditionalProperties2[str],
        str
    ],
]


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
        arg: typing.Union[
            DictInput,
            AdditionalProperties[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalProperties[frozendict.frozendict]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )

DictInput2 = typing.Mapping[
    str,
    typing.Union[
        AdditionalProperties[frozendict.frozendict],
        dict,
        frozendict.frozendict
    ],
]


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
        arg: typing.Union[
            DictInput2,
            MapMapOfString[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> MapMapOfString[frozendict.frozendict]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )



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
DictInput3 = typing.Mapping[
    str,
    typing.Union[
        AdditionalProperties3[str],
        str
    ],
]


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
        arg: typing.Union[
            DictInput3,
            MapOfEnumString[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> MapOfEnumString[frozendict.frozendict]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )

AdditionalProperties4: typing_extensions.TypeAlias = schemas.BoolSchema[U]
DictInput4 = typing.Mapping[
    str,
    typing.Union[
        AdditionalProperties4[schemas.BoolClass],
        bool
    ],
]


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
        arg: typing.Union[
            DictInput4,
            DirectMap[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> DirectMap[frozendict.frozendict]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )



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
        arg: typing.Union[
            DictInput5,
            MapTest[frozendict.frozendict],
        ],
        configuration: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> MapTest[frozendict.frozendict]:
        return super().__new__(
            cls,
            arg,
            configuration=configuration,
        )


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
DictInput5 = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            MapMapOfString[frozendict.frozendict],
            dict,
            frozendict.frozendict
        ],
        typing.Union[
            MapOfEnumString[frozendict.frozendict],
            dict,
            frozendict.frozendict
        ],
        typing.Union[
            DirectMap[frozendict.frozendict],
            dict,
            frozendict.frozendict
        ],
        typing.Union[
            string_boolean_map.StringBooleanMap[frozendict.frozendict],
            dict,
            frozendict.frozendict
        ],
        schemas.INPUT_TYPES_ALL_INCL_SCHEMA
    ]
]
