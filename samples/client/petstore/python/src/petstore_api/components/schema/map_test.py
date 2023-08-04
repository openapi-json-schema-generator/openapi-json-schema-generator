# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties2: typing_extensions.TypeAlias = schemas.StrSchema


class AdditionalPropertiesDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: str,
    ):
        used_kwargs = typing.cast(AdditionalPropertiesDictInput, kwargs)
        return AdditionalProperties.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: AdditionalPropertiesDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalPropertiesDict:
        return AdditionalProperties.validate(arg, configuration=configuration)

    
    def get_additional_property_(self, name: str) -> typing.Union[str, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
AdditionalPropertiesDictInput = typing.Mapping[
    str,
    str,
]


@dataclasses.dataclass(frozen=True)
class AdditionalProperties(
    schemas.Schema[AdditionalPropertiesDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties2] = dataclasses.field(default_factory=lambda: AdditionalProperties2) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AdditionalPropertiesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            AdditionalPropertiesDictInput,
            AdditionalPropertiesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalPropertiesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )



class MapMapOfStringDict(schemas.immutabledict[str, schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            AdditionalPropertiesDictInput,
            AdditionalPropertiesDict,
        ],
    ):
        used_kwargs = typing.cast(MapMapOfStringDictInput, kwargs)
        return MapMapOfString.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: MapMapOfStringDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapMapOfStringDict:
        return MapMapOfString.validate(arg, configuration=configuration)

    
    def get_additional_property_(self, name: str) -> typing.Union[AdditionalPropertiesDict, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            AdditionalPropertiesDict,
            val
        )
MapMapOfStringDictInput = typing.Mapping[
    str,
    typing.Union[
        AdditionalPropertiesDictInput,
        AdditionalPropertiesDict,
    ],
]


@dataclasses.dataclass(frozen=True)
class MapMapOfString(
    schemas.Schema[MapMapOfStringDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MapMapOfStringDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MapMapOfStringDictInput,
            MapMapOfStringDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapMapOfStringDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )



class AdditionalPropertiesEnums:

    @schemas.classproperty
    def UPPER(cls) -> typing_extensions.Literal["UPPER"]:
        return AdditionalProperties3.validate("UPPER")

    @schemas.classproperty
    def LOWER(cls) -> typing_extensions.Literal["lower"]:
        return AdditionalProperties3.validate("lower")


@dataclasses.dataclass(frozen=True)
class AdditionalProperties3(
    schemas.Schema[schemas.immutabledict, str]
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "UPPER": "UPPER",
            "lower": "LOWER",
        }
    )
    enums = AdditionalPropertiesEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["UPPER"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["UPPER"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["lower"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["lower"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["UPPER","lower",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "UPPER",
        "lower",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "UPPER",
                "lower",
            ],
            validated_arg
        )


class MapOfEnumStringDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing_extensions.Literal[
            "UPPER",
            "lower"
        ],
    ):
        used_kwargs = typing.cast(MapOfEnumStringDictInput, kwargs)
        return MapOfEnumString.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: MapOfEnumStringDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapOfEnumStringDict:
        return MapOfEnumString.validate(arg, configuration=configuration)

    
    def get_additional_property_(self, name: str) -> typing.Union[typing_extensions.Literal["UPPER", "lower"], schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing_extensions.Literal["UPPER", "lower"],
            val
        )
MapOfEnumStringDictInput = typing.Mapping[
    str,
    typing_extensions.Literal[
        "UPPER",
        "lower"
    ],
]


@dataclasses.dataclass(frozen=True)
class MapOfEnumString(
    schemas.Schema[MapOfEnumStringDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties3] = dataclasses.field(default_factory=lambda: AdditionalProperties3) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MapOfEnumStringDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MapOfEnumStringDictInput,
            MapOfEnumStringDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapOfEnumStringDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

AdditionalProperties4: typing_extensions.TypeAlias = schemas.BoolSchema


class DirectMapDict(schemas.immutabledict[str, bool]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: bool,
    ):
        used_kwargs = typing.cast(DirectMapDictInput, kwargs)
        return DirectMap.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: DirectMapDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DirectMapDict:
        return DirectMap.validate(arg, configuration=configuration)

    
    def get_additional_property_(self, name: str) -> typing.Union[bool, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            bool,
            val
        )
DirectMapDictInput = typing.Mapping[
    str,
    bool,
]


@dataclasses.dataclass(frozen=True)
class DirectMap(
    schemas.Schema[DirectMapDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties4] = dataclasses.field(default_factory=lambda: AdditionalProperties4) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: DirectMapDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            DirectMapDictInput,
            DirectMapDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DirectMapDict:
        return super().validate_base(
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


class MapTestDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "map_map_of_string",
        "map_of_enum_string",
        "direct_map",
        "indirect_map",
    })
    @staticmethod
    def from_dict_(
        arg: MapTestDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapTestDict:
        return MapTest.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        *,
        map_map_of_string: typing.Union[
            MapMapOfStringDictInput,
            MapMapOfStringDict,
            schemas.Unset
        ] = schemas.unset,
        map_of_enum_string: typing.Union[
            MapOfEnumStringDictInput,
            MapOfEnumStringDict,
            schemas.Unset
        ] = schemas.unset,
        direct_map: typing.Union[
            DirectMapDictInput,
            DirectMapDict,
            schemas.Unset
        ] = schemas.unset,
        indirect_map: typing.Union[
            string_boolean_map.StringBooleanMapDictInput,
            string_boolean_map.StringBooleanMapDict,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("map_map_of_string", map_map_of_string),
            ("map_of_enum_string", map_of_enum_string),
            ("direct_map", direct_map),
            ("indirect_map", indirect_map),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(MapTestDictInput, arg_)
        return MapTest.validate(used_arg_, configuration=configuration_)

    
    @property
    def map_map_of_string(self) -> typing.Union[MapMapOfStringDict, schemas.Unset]:
        val = self.get("map_map_of_string", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            MapMapOfStringDict,
            val
        )
    
    @property
    def map_of_enum_string(self) -> typing.Union[MapOfEnumStringDict, schemas.Unset]:
        val = self.get("map_of_enum_string", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            MapOfEnumStringDict,
            val
        )
    
    @property
    def direct_map(self) -> typing.Union[DirectMapDict, schemas.Unset]:
        val = self.get("direct_map", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            DirectMapDict,
            val
        )
    
    @property
    def indirect_map(self) -> typing.Union[string_boolean_map.StringBooleanMapDict, schemas.Unset]:
        val = self.get("indirect_map", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            string_boolean_map.StringBooleanMapDict,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
MapTestDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class MapTest(
    schemas.Schema[MapTestDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MapTestDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MapTestDictInput,
            MapTestDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapTestDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

