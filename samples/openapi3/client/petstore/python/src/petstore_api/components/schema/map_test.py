# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class MapTest(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class MapMapOfString(
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
                        ) -> MapTest.Schema_.Properties.MapMapOfString.Schema_.AdditionalProperties[frozendict.frozendict]:
                            return super().__new__(
                                cls,
                                *args_,
                                configuration_=configuration_,
                                **kwargs,
                            )
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties[frozendict.frozendict]:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict],
                ) -> MapTest.Schema_.Properties.MapMapOfString[frozendict.frozendict]:
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            
            
            class MapOfEnumString(
                schemas.DictSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    
                    
                    class AdditionalProperties(
                        schemas.StrSchema[schemas.T]
                    ):
                    
                    
                        class Schema_:
                            types = {
                                str,
                            }
                            enum_value_to_name = {
                                "UPPER": "UPPER",
                                "lower": "LOWER",
                            }
                        
                        @schemas.classproperty
                        def UPPER(cls):
                            return cls("UPPER")
                        
                        @schemas.classproperty
                        def LOWER(cls):
                            return cls("lower")
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties[str]:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, str],
                ) -> MapTest.Schema_.Properties.MapOfEnumString[frozendict.frozendict]:
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            
            
            class DirectMap(
                schemas.DictSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    AdditionalProperties: typing_extensions.TypeAlias = schemas.BoolSchema[U]
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties[schemas.BoolClass]:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, bool],
                ) -> MapTest.Schema_.Properties.DirectMap[frozendict.frozendict]:
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
        
            @staticmethod
            def indirect_map() -> typing.Type['string_boolean_map.StringBooleanMap']:
                return string_boolean_map.StringBooleanMap
            __annotations__ = {
                "map_map_of_string": MapMapOfString,
                "map_of_enum_string": MapOfEnumString,
                "direct_map": DirectMap,
                "indirect_map": indirect_map,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_map_of_string"]) -> Schema_.Properties.MapMapOfString[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_of_enum_string"]) -> Schema_.Properties.MapOfEnumString[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direct_map"]) -> Schema_.Properties.DirectMap[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["indirect_map"]) -> string_boolean_map.StringBooleanMap[frozendict.frozendict]: ...
    
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
        *args_: typing.Union[dict, frozendict.frozendict],
        map_map_of_string: typing.Union[Schema_.Properties.MapMapOfString, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        map_of_enum_string: typing.Union[Schema_.Properties.MapOfEnumString, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        direct_map: typing.Union[Schema_.Properties.DirectMap, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        indirect_map: typing.Union['string_boolean_map.StringBooleanMap', dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> MapTest[frozendict.frozendict]:
        return super().__new__(
            cls,
            *args_,
            map_map_of_string=map_map_of_string,
            map_of_enum_string=map_of_enum_string,
            direct_map=direct_map,
            indirect_map=indirect_map,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import string_boolean_map
