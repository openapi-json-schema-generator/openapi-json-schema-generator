# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
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


class ArrayTest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        
        class Properties:
            
            
            class ArrayOfString(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    Items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[Schema_.Items, str], ...
                        ],
                        typing.List[
                            typing.Union[Schema_.Items, str]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'ArrayOfString':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            
            
            class ArrayArrayOfInteger(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    
                    class Items(
                        schemas.ListSchema
                    ):
                    
                    
                        class Schema_:
                            types = {tuple}
                            Items = schemas.Int64Schema
                    
                        def __new__(
                            cls,
                            arg_: typing.Union[
                                typing.Tuple[
                                    typing.Union[Schema_.Items, decimal.Decimal, int], ...
                                ],
                                typing.List[
                                    typing.Union[Schema_.Items, decimal.Decimal, int]
                                ],
                            ],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                        ) -> 'Items':
                            return super().__new__(
                                cls,
                                arg_,
                                configuration_=configuration_,
                            )
                    
                        def __getitem__(self, i: int) -> Schema_.Items:
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[Schema_.Items, list, tuple], ...
                        ],
                        typing.List[
                            typing.Union[Schema_.Items, list, tuple]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'ArrayArrayOfInteger':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            
            
            class ArrayArrayOfModel(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    
                    class Items(
                        schemas.ListSchema
                    ):
                    
                    
                        class Schema_:
                            types = {tuple}
                            
                            @staticmethod
                            def items() -> typing.Type['read_only_first.ReadOnlyFirst']:
                                return read_only_first.ReadOnlyFirst
                    
                        def __new__(
                            cls,
                            arg_: typing.Union[
                                typing.Tuple[
                                    typing.Union['read_only_first.ReadOnlyFirst', dict, frozendict.frozendict], ...
                                ],
                                typing.List[
                                    typing.Union['read_only_first.ReadOnlyFirst', dict, frozendict.frozendict]
                                ],
                            ],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                        ) -> 'Items':
                            return super().__new__(
                                cls,
                                arg_,
                                configuration_=configuration_,
                            )
                    
                        def __getitem__(self, i: int) -> 'read_only_first.ReadOnlyFirst':
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[Schema_.Items, list, tuple], ...
                        ],
                        typing.List[
                            typing.Union[Schema_.Items, list, tuple]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'ArrayArrayOfModel':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            __annotations__ = {
                "array_of_string": ArrayOfString,
                "array_array_of_integer": ArrayArrayOfInteger,
                "array_array_of_model": ArrayArrayOfModel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_of_string"]) -> Schema_.Properties.ArrayOfString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_array_of_integer"]) -> Schema_.Properties.ArrayArrayOfInteger: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_array_of_model"]) -> Schema_.Properties.ArrayArrayOfModel: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["array_of_string"],
            typing_extensions.Literal["array_array_of_integer"],
            typing_extensions.Literal["array_array_of_model"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["array_of_string"]) -> typing.Union[Schema_.Properties.ArrayOfString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["array_array_of_integer"]) -> typing.Union[Schema_.Properties.ArrayArrayOfInteger, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["array_array_of_model"]) -> typing.Union[Schema_.Properties.ArrayArrayOfModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["array_of_string"],
            typing_extensions.Literal["array_array_of_integer"],
            typing_extensions.Literal["array_array_of_model"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        array_of_string: typing.Union[Schema_.Properties.ArrayOfString, list, tuple, schemas.Unset] = schemas.unset,
        array_array_of_integer: typing.Union[Schema_.Properties.ArrayArrayOfInteger, list, tuple, schemas.Unset] = schemas.unset,
        array_array_of_model: typing.Union[Schema_.Properties.ArrayArrayOfModel, list, tuple, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ArrayTest':
        return super().__new__(
            cls,
            *args_,
            array_of_string=array_of_string,
            array_array_of_integer=array_array_of_integer,
            array_array_of_model=array_array_of_model,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import read_only_first
