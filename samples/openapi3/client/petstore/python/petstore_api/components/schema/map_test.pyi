# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class MapTest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        
        class Properties:
            
            
            class MapMapOfString(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    
                    
                    class AdditionalProperties(
                        schemas.DictSchema
                    ):
                    
                    
                        class Schema_:
                            AdditionalProperties = schemas.StrSchema
                        
                        def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        def get_item_(self, name: str) -> Schema_.AdditionalProperties:
                            return super().get_item_(name)
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
                            **kwargs: typing.Union[Schema_.AdditionalProperties, str, ],
                        ) -> 'AdditionalProperties':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_(self, name: str) -> Schema_.AdditionalProperties:
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict, ],
                ) -> 'MapMapOfString':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class MapOfEnumString(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    
                    
                    class AdditionalProperties(
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def UPPER(cls):
                            return cls("UPPER")
                        
                        @schemas.classproperty
                        def LOWER(cls):
                            return cls("lower")
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_(self, name: str) -> Schema_.AdditionalProperties:
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, str, ],
                ) -> 'MapOfEnumString':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class DirectMap(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    AdditionalProperties = schemas.BoolSchema
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_(self, name: str) -> Schema_.AdditionalProperties:
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, bool, ],
                ) -> 'DirectMap':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
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
    def __getitem__(self, name: typing_extensions.Literal["map_map_of_string"]) -> Schema_.Properties.MapMapOfString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map_of_enum_string"]) -> Schema_.Properties.MapOfEnumString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direct_map"]) -> Schema_.Properties.DirectMap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["indirect_map"]) -> 'string_boolean_map.StringBooleanMap': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
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
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["map_map_of_string"]) -> typing.Union[Schema_.Properties.MapMapOfString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["map_of_enum_string"]) -> typing.Union[Schema_.Properties.MapOfEnumString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["direct_map"]) -> typing.Union[Schema_.Properties.DirectMap, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["indirect_map"]) -> typing.Union['string_boolean_map.StringBooleanMap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["map_map_of_string"],
            typing_extensions.Literal["map_of_enum_string"],
            typing_extensions.Literal["direct_map"],
            typing_extensions.Literal["indirect_map"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        map_map_of_string: typing.Union[Schema_.Properties.MapMapOfString, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        map_of_enum_string: typing.Union[Schema_.Properties.MapOfEnumString, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        direct_map: typing.Union[Schema_.Properties.DirectMap, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        indirect_map: typing.Union['string_boolean_map.StringBooleanMap', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'MapTest':
        return super().__new__(
            cls,
            *_args,
            map_map_of_string=map_map_of_string,
            map_of_enum_string=map_of_enum_string,
            direct_map=direct_map,
            indirect_map=indirect_map,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import string_boolean_map
