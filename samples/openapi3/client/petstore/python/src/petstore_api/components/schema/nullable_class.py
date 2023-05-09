# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class NullableClass(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class IntegerProp(
                schemas.NoneBase,
                schemas.IntBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        decimal.Decimal,
                    }
                    format = 'int'
            
            
                def __new__(
                    cls,
                    arg_: typing.Union[None, decimal.Decimal, int],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.IntegerProp':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
            
            
            class NumberProp(
                schemas.NoneBase,
                schemas.NumberBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        decimal.Decimal,
                    }
            
            
                def __new__(
                    cls,
                    arg_: typing.Union[None, decimal.Decimal, int, float],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.NumberProp':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
            
            
            class BooleanProp(
                schemas.NoneBase,
                schemas.BoolBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        schemas.BoolClass,
                    }
            
            
                def __new__(
                    cls,
                    arg_: typing.Union[None, bool],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.BooleanProp':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
            
            
            class StringProp(
                schemas.NoneBase,
                schemas.StrBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        str,
                    }
            
            
                def __new__(
                    cls,
                    arg_: typing.Union[None, str],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.StringProp':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
            
            
            class DateProp(
                schemas.NoneBase,
                schemas.DateBase,
                schemas.StrBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        str,
                    }
                    format = 'date'
            
            
                def __new__(
                    cls,
                    arg_: typing.Union[None, str, datetime.date],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.DateProp':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
            
            
            class DatetimeProp(
                schemas.NoneBase,
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        str,
                    }
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    arg_: typing.Union[None, str, datetime.datetime],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.DatetimeProp':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
            
            
            class ArrayNullableProp(
                schemas.NoneBase,
                schemas.ListBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        tuple,
                    }
                    Items = schemas.DictSchema
            
            
                def __new__(
                    cls,
                    arg_: typing.Union[None, list, tuple],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.ArrayNullableProp':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
            
            
            class ArrayAndItemsNullableProp(
                schemas.NoneBase,
                schemas.ListBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        tuple,
                    }
                    
                    
                    class Items(
                        schemas.NoneBase,
                        schemas.DictBase,
                        schemas.Schema,
                        schemas.NoneFrozenDictMixin
                    ):
                    
                    
                        class Schema_:
                            types = {
                                schemas.NoneClass,
                                frozendict.frozendict,
                            }
                    
                    
                        def __new__(
                            cls,
                            *args_: typing.Union[None, dict, frozendict.frozendict],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                            **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                        ) -> 'NullableClass.Schema_.Properties.ArrayAndItemsNullableProp.Schema_.Items':
                            return super().__new__(
                                cls,
                                *args_,
                                configuration_=configuration_,
                                **kwargs,
                            )
                    
            
            
                def __new__(
                    cls,
                    arg_: typing.Union[None, list, tuple],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.ArrayAndItemsNullableProp':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
            
            
            class ArrayItemsNullable(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    
                    class Items(
                        schemas.NoneBase,
                        schemas.DictBase,
                        schemas.Schema,
                        schemas.NoneFrozenDictMixin
                    ):
                    
                    
                        class Schema_:
                            types = {
                                schemas.NoneClass,
                                frozendict.frozendict,
                            }
                    
                    
                        def __new__(
                            cls,
                            *args_: typing.Union[None, dict, frozendict.frozendict],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                            **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                        ) -> 'NullableClass.Schema_.Properties.ArrayItemsNullable.Schema_.Items':
                            return super().__new__(
                                cls,
                                *args_,
                                configuration_=configuration_,
                                **kwargs,
                            )
                    
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[Schema_.Items, None, dict, frozendict.frozendict], ...
                        ],
                        typing.List[
                            typing.Union[Schema_.Items, None, dict, frozendict.frozendict]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'NullableClass.Schema_.Properties.ArrayItemsNullable':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            
            
            class ObjectNullableProp(
                schemas.NoneBase,
                schemas.DictBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        frozendict.frozendict,
                    }
                    AdditionalProperties = schemas.DictSchema
            
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[None, dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict],
                ) -> 'NullableClass.Schema_.Properties.ObjectNullableProp':
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            
            
            
            class ObjectAndItemsNullableProp(
                schemas.NoneBase,
                schemas.DictBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class Schema_:
                    types = {
                        schemas.NoneClass,
                        frozendict.frozendict,
                    }
                    
                    
                    class AdditionalProperties(
                        schemas.NoneBase,
                        schemas.DictBase,
                        schemas.Schema,
                        schemas.NoneFrozenDictMixin
                    ):
                    
                    
                        class Schema_:
                            types = {
                                schemas.NoneClass,
                                frozendict.frozendict,
                            }
                    
                    
                        def __new__(
                            cls,
                            *args_: typing.Union[None, dict, frozendict.frozendict],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                            **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                        ) -> 'NullableClass.Schema_.Properties.ObjectAndItemsNullableProp.Schema_.AdditionalProperties':
                            return super().__new__(
                                cls,
                                *args_,
                                configuration_=configuration_,
                                **kwargs,
                            )
                    
            
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[None, dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, None, dict, frozendict.frozendict],
                ) -> 'NullableClass.Schema_.Properties.ObjectAndItemsNullableProp':
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            
            
            
            class ObjectItemsNullable(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    
                    
                    class AdditionalProperties(
                        schemas.NoneBase,
                        schemas.DictBase,
                        schemas.Schema,
                        schemas.NoneFrozenDictMixin
                    ):
                    
                    
                        class Schema_:
                            types = {
                                schemas.NoneClass,
                                frozendict.frozendict,
                            }
                    
                    
                        def __new__(
                            cls,
                            *args_: typing.Union[None, dict, frozendict.frozendict],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                            **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                        ) -> 'NullableClass.Schema_.Properties.ObjectItemsNullable.Schema_.AdditionalProperties':
                            return super().__new__(
                                cls,
                                *args_,
                                configuration_=configuration_,
                                **kwargs,
                            )
                    
                
                def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[Schema_.AdditionalProperties, None, dict, frozendict.frozendict],
                ) -> 'NullableClass.Schema_.Properties.ObjectItemsNullable':
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            __annotations__ = {
                "integer_prop": IntegerProp,
                "number_prop": NumberProp,
                "boolean_prop": BooleanProp,
                "string_prop": StringProp,
                "date_prop": DateProp,
                "datetime_prop": DatetimeProp,
                "array_nullable_prop": ArrayNullableProp,
                "array_and_items_nullable_prop": ArrayAndItemsNullableProp,
                "array_items_nullable": ArrayItemsNullable,
                "object_nullable_prop": ObjectNullableProp,
                "object_and_items_nullable_prop": ObjectAndItemsNullableProp,
                "object_items_nullable": ObjectItemsNullable,
            }
        
        
        class AdditionalProperties(
            schemas.NoneBase,
            schemas.DictBase,
            schemas.Schema,
            schemas.NoneFrozenDictMixin
        ):
        
        
            class Schema_:
                types = {
                    schemas.NoneClass,
                    frozendict.frozendict,
                }
        
        
            def __new__(
                cls,
                *args_: typing.Union[None, dict, frozendict.frozendict],
                configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
            ) -> 'NullableClass.Schema_.AdditionalProperties':
                return super().__new__(
                    cls,
                    *args_,
                    configuration_=configuration_,
                    **kwargs,
                )
        
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integer_prop"]) -> Schema_.Properties.IntegerProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number_prop"]) -> Schema_.Properties.NumberProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boolean_prop"]) -> Schema_.Properties.BooleanProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["string_prop"]) -> Schema_.Properties.StringProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_prop"]) -> Schema_.Properties.DateProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datetime_prop"]) -> Schema_.Properties.DatetimeProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_nullable_prop"]) -> Schema_.Properties.ArrayNullableProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_and_items_nullable_prop"]) -> Schema_.Properties.ArrayAndItemsNullableProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_items_nullable"]) -> Schema_.Properties.ArrayItemsNullable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_nullable_prop"]) -> Schema_.Properties.ObjectNullableProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_and_items_nullable_prop"]) -> Schema_.Properties.ObjectAndItemsNullableProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_items_nullable"]) -> Schema_.Properties.ObjectItemsNullable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> Schema_.AdditionalProperties: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["integer_prop"],
            typing_extensions.Literal["number_prop"],
            typing_extensions.Literal["boolean_prop"],
            typing_extensions.Literal["string_prop"],
            typing_extensions.Literal["date_prop"],
            typing_extensions.Literal["datetime_prop"],
            typing_extensions.Literal["array_nullable_prop"],
            typing_extensions.Literal["array_and_items_nullable_prop"],
            typing_extensions.Literal["array_items_nullable"],
            typing_extensions.Literal["object_nullable_prop"],
            typing_extensions.Literal["object_and_items_nullable_prop"],
            typing_extensions.Literal["object_items_nullable"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        integer_prop: typing.Union[Schema_.Properties.IntegerProp, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        number_prop: typing.Union[Schema_.Properties.NumberProp, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        boolean_prop: typing.Union[Schema_.Properties.BooleanProp, None, bool, schemas.Unset] = schemas.unset,
        string_prop: typing.Union[Schema_.Properties.StringProp, None, str, schemas.Unset] = schemas.unset,
        date_prop: typing.Union[Schema_.Properties.DateProp, None, str, datetime.date, schemas.Unset] = schemas.unset,
        datetime_prop: typing.Union[Schema_.Properties.DatetimeProp, None, str, datetime.datetime, schemas.Unset] = schemas.unset,
        array_nullable_prop: typing.Union[Schema_.Properties.ArrayNullableProp, None, list, tuple, schemas.Unset] = schemas.unset,
        array_and_items_nullable_prop: typing.Union[Schema_.Properties.ArrayAndItemsNullableProp, None, list, tuple, schemas.Unset] = schemas.unset,
        array_items_nullable: typing.Union[Schema_.Properties.ArrayItemsNullable, list, tuple, schemas.Unset] = schemas.unset,
        object_nullable_prop: typing.Union[Schema_.Properties.ObjectNullableProp, None, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        object_and_items_nullable_prop: typing.Union[Schema_.Properties.ObjectAndItemsNullableProp, None, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        object_items_nullable: typing.Union[Schema_.Properties.ObjectItemsNullable, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[Schema_.AdditionalProperties, None, dict, frozendict.frozendict],
    ) -> 'NullableClass':
        return super().__new__(
            cls,
            *args_,
            integer_prop=integer_prop,
            number_prop=number_prop,
            boolean_prop=boolean_prop,
            string_prop=string_prop,
            date_prop=date_prop,
            datetime_prop=datetime_prop,
            array_nullable_prop=array_nullable_prop,
            array_and_items_nullable_prop=array_and_items_nullable_prop,
            array_items_nullable=array_items_nullable,
            object_nullable_prop=object_nullable_prop,
            object_and_items_nullable_prop=object_and_items_nullable_prop,
            object_items_nullable=object_items_nullable,
            configuration_=configuration_,
            **kwargs,
        )
