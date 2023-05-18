# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class AdditionalPropertiesClass(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class MapProperty(
                schemas.DictSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    AdditionalProperties: typing_extensions.TypeAlias = schemas.StrSchema[U]
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties[str]:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, str],
                ) -> AdditionalPropertiesClass.Schema_.Properties.MapProperty[frozendict.frozendict]:
                    inst = super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
                    inst = typing.cast(
                        AdditionalPropertiesClass.Schema_.Properties.MapProperty[frozendict.frozendict],
                        inst
                    )
                    return inst
            
            
            class MapOfMapProperty(
                schemas.DictSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    
                    
                    class AdditionalProperties(
                        schemas.DictSchema[schemas.T]
                    ):
                    
                    
                        class Schema_:
                            types = {frozendict.frozendict}
                            AdditionalProperties: typing_extensions.TypeAlias = schemas.StrSchema[U]
                        
                        def __getitem__(self, name: str) -> Schema_.AdditionalProperties[str]:
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                    
                        def __new__(
                            cls,
                            *args_: typing.Union[dict, frozendict.frozendict],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                            **kwargs: typing.Union[Schema_.AdditionalProperties, str],
                        ) -> AdditionalPropertiesClass.Schema_.Properties.MapOfMapProperty.Schema_.AdditionalProperties[frozendict.frozendict]:
                            inst = super().__new__(
                                cls,
                                *args_,
                                configuration_=configuration_,
                                **kwargs,
                            )
                            inst = typing.cast(
                                AdditionalPropertiesClass.Schema_.Properties.MapOfMapProperty.Schema_.AdditionalProperties[frozendict.frozendict],
                                inst
                            )
                            return inst
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties[frozendict.frozendict]:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict],
                ) -> AdditionalPropertiesClass.Schema_.Properties.MapOfMapProperty[frozendict.frozendict]:
                    inst = super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
                    inst = typing.cast(
                        AdditionalPropertiesClass.Schema_.Properties.MapOfMapProperty[frozendict.frozendict],
                        inst
                    )
                    return inst
            Anytype1: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]
            MapWithUndeclaredPropertiesAnytype1: typing_extensions.TypeAlias = schemas.DictSchema[U]
            MapWithUndeclaredPropertiesAnytype2: typing_extensions.TypeAlias = schemas.DictSchema[U]
            
            
            class MapWithUndeclaredPropertiesAnytype3(
                schemas.DictSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    AdditionalProperties: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties[typing.Union[
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
                    **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
                ) -> AdditionalPropertiesClass.Schema_.Properties.MapWithUndeclaredPropertiesAnytype3[frozendict.frozendict]:
                    inst = super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
                    inst = typing.cast(
                        AdditionalPropertiesClass.Schema_.Properties.MapWithUndeclaredPropertiesAnytype3[frozendict.frozendict],
                        inst
                    )
                    return inst
            
            
            class EmptyMap(
                schemas.DictSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema[U]
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> AdditionalPropertiesClass.Schema_.Properties.EmptyMap[frozendict.frozendict]:
                    inst = super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        AdditionalPropertiesClass.Schema_.Properties.EmptyMap[frozendict.frozendict],
                        inst
                    )
                    return inst
            
            
            class MapWithUndeclaredPropertiesString(
                schemas.DictSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    AdditionalProperties: typing_extensions.TypeAlias = schemas.StrSchema[U]
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties[str]:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, str],
                ) -> AdditionalPropertiesClass.Schema_.Properties.MapWithUndeclaredPropertiesString[frozendict.frozendict]:
                    inst = super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
                    inst = typing.cast(
                        AdditionalPropertiesClass.Schema_.Properties.MapWithUndeclaredPropertiesString[frozendict.frozendict],
                        inst
                    )
                    return inst
            __annotations__ = {
                "map_property": MapProperty,
                "map_of_map_property": MapOfMapProperty,
                "anytype_1": Anytype1,
                "map_with_undeclared_properties_anytype_1": MapWithUndeclaredPropertiesAnytype1,
                "map_with_undeclared_properties_anytype_2": MapWithUndeclaredPropertiesAnytype2,
                "map_with_undeclared_properties_anytype_3": MapWithUndeclaredPropertiesAnytype3,
                "empty_map": EmptyMap,
                "map_with_undeclared_properties_string": MapWithUndeclaredPropertiesString,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_property"]) -> Schema_.Properties.MapProperty[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_of_map_property"]) -> Schema_.Properties.MapOfMapProperty[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anytype_1"]) -> Schema_.Properties.Anytype1[typing.Union[
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
    def __getitem__(self, name: typing_extensions.Literal["map_with_undeclared_properties_anytype_1"]) -> Schema_.Properties.MapWithUndeclaredPropertiesAnytype1[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_with_undeclared_properties_anytype_2"]) -> Schema_.Properties.MapWithUndeclaredPropertiesAnytype2[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_with_undeclared_properties_anytype_3"]) -> Schema_.Properties.MapWithUndeclaredPropertiesAnytype3[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["empty_map"]) -> Schema_.Properties.EmptyMap[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_with_undeclared_properties_string"]) -> Schema_.Properties.MapWithUndeclaredPropertiesString[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema[typing.Union[
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
        map_property: typing.Union[Schema_.Properties.MapProperty, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        map_of_map_property: typing.Union[Schema_.Properties.MapOfMapProperty, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        anytype_1: typing.Union[Schema_.Properties.Anytype1, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        map_with_undeclared_properties_anytype_1: typing.Union[Schema_.Properties.MapWithUndeclaredPropertiesAnytype1, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        map_with_undeclared_properties_anytype_2: typing.Union[Schema_.Properties.MapWithUndeclaredPropertiesAnytype2, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        map_with_undeclared_properties_anytype_3: typing.Union[Schema_.Properties.MapWithUndeclaredPropertiesAnytype3, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        empty_map: typing.Union[Schema_.Properties.EmptyMap, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        map_with_undeclared_properties_string: typing.Union[Schema_.Properties.MapWithUndeclaredPropertiesString, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
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
