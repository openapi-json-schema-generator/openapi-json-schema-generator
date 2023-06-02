# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

AdditionalProperties: typing_extensions.TypeAlias = schemas.StrSchema[U]


class MapProperty(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties[str]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            AdditionalProperties[str],
            str
        ],
    ) -> MapProperty[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            MapProperty[frozendict.frozendict],
            inst
        )
        return inst

AdditionalProperties: typing_extensions.TypeAlias = schemas.StrSchema[U]


class AdditionalProperties(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties[str]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            AdditionalProperties[str],
            str
        ],
    ) -> AdditionalProperties[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            AdditionalProperties[frozendict.frozendict],
            inst
        )
        return inst



class MapOfMapProperty(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties[frozendict.frozendict]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            AdditionalProperties[frozendict.frozendict],
            dict,
            frozendict.frozendict
        ],
    ) -> MapOfMapProperty[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            MapOfMapProperty[frozendict.frozendict],
            inst
        )
        return inst

Anytype1: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]
MapWithUndeclaredPropertiesAnytype1: typing_extensions.TypeAlias = schemas.DictSchema[U]
MapWithUndeclaredPropertiesAnytype2: typing_extensions.TypeAlias = schemas.DictSchema[U]
AdditionalProperties: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]


class MapWithUndeclaredPropertiesAnytype3(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            AdditionalProperties[typing.Union[
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
    ) -> MapWithUndeclaredPropertiesAnytype3[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            MapWithUndeclaredPropertiesAnytype3[frozendict.frozendict],
            inst
        )
        return inst

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema[U]


class EmptyMap(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> EmptyMap[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            EmptyMap[frozendict.frozendict],
            inst
        )
        return inst

AdditionalProperties: typing_extensions.TypeAlias = schemas.StrSchema[U]


class MapWithUndeclaredPropertiesString(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties[str]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            AdditionalProperties[str],
            str
        ],
    ) -> MapWithUndeclaredPropertiesString[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            MapWithUndeclaredPropertiesString[frozendict.frozendict],
            inst
        )
        return inst



class AdditionalPropertiesClass(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        properties: AdditionalPropertiesClassProperties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(AdditionalPropertiesClassProperties)) # type: ignore
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_property"]) -> MapProperty[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_of_map_property"]) -> MapOfMapProperty[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anytype_1"]) -> Anytype1[typing.Union[
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
    def __getitem__(self, name: typing_extensions.Literal["map_with_undeclared_properties_anytype_1"]) -> MapWithUndeclaredPropertiesAnytype1[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_with_undeclared_properties_anytype_2"]) -> MapWithUndeclaredPropertiesAnytype2[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_with_undeclared_properties_anytype_3"]) -> MapWithUndeclaredPropertiesAnytype3[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["empty_map"]) -> EmptyMap[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_with_undeclared_properties_string"]) -> MapWithUndeclaredPropertiesString[frozendict.frozendict]: ...
    
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
            typing_extensions.Literal["map_property"],
            typing_extensions.Literal["map_of_map_property"],
            typing_extensions.Literal["anytype_1"],
            typing_extensions.Literal["map_with_undeclared_properties_anytype_1"],
            typing_extensions.Literal["map_with_undeclared_properties_anytype_2"],
            typing_extensions.Literal["map_with_undeclared_properties_anytype_3"],
            typing_extensions.Literal["empty_map"],
            typing_extensions.Literal["map_with_undeclared_properties_string"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        map_property: typing.Union[
            MapProperty[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        map_of_map_property: typing.Union[
            MapOfMapProperty[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        anytype_1: typing.Union[
            Anytype1[typing.Union[
                frozendict.frozendict,
                str,
                decimal.Decimal,
                schemas.BoolClass,
                schemas.NoneClass,
                tuple,
                bytes,
                schemas.FileIO
            ]],
            schemas.Unset,
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
        ] = schemas.unset,
        map_with_undeclared_properties_anytype_1: typing.Union[
            MapWithUndeclaredPropertiesAnytype1[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        map_with_undeclared_properties_anytype_2: typing.Union[
            MapWithUndeclaredPropertiesAnytype2[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        map_with_undeclared_properties_anytype_3: typing.Union[
            MapWithUndeclaredPropertiesAnytype3[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        empty_map: typing.Union[
            EmptyMap[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        map_with_undeclared_properties_string: typing.Union[
            MapWithUndeclaredPropertiesString[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
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
    ) -> AdditionalPropertiesClass[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            map_property=map_property,
            map_of_map_property=map_of_map_property,
            anytype_1=anytype_1,
            map_with_undeclared_properties_anytype_1=map_with_undeclared_properties_anytype_1,
            map_with_undeclared_properties_anytype_2=map_with_undeclared_properties_anytype_2,
            map_with_undeclared_properties_anytype_3=map_with_undeclared_properties_anytype_3,
            empty_map=empty_map,
            map_with_undeclared_properties_string=map_with_undeclared_properties_string,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            AdditionalPropertiesClass[frozendict.frozendict],
            inst
        )
        return inst

AdditionalPropertiesClassProperties = typing_extensions.TypedDict(
    'AdditionalPropertiesClassProperties',
    {
        "map_property": typing.Type[MapProperty],
        "map_of_map_property": typing.Type[MapOfMapProperty],
        "anytype_1": typing.Type[Anytype1],
        "map_with_undeclared_properties_anytype_1": typing.Type[MapWithUndeclaredPropertiesAnytype1],
        "map_with_undeclared_properties_anytype_2": typing.Type[MapWithUndeclaredPropertiesAnytype2],
        "map_with_undeclared_properties_anytype_3": typing.Type[MapWithUndeclaredPropertiesAnytype3],
        "empty_map": typing.Type[EmptyMap],
        "map_with_undeclared_properties_string": typing.Type[MapWithUndeclaredPropertiesString],
    }
)
