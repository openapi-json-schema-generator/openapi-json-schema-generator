# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class ArrayTest(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class ArrayOfString(
                schemas.ListSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {tuple}
                    Items: typing_extensions.TypeAlias = schemas.StrSchema[U]
            
                def __new__(
                    cls,
                    arg_: typing.Sequence[
                        typing.Union[
                            Schema_.Items[str],
                            str
                        ]
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> ArrayTest.Schema_.Properties.ArrayOfString[tuple]:
                    inst = super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        ArrayTest.Schema_.Properties.ArrayOfString[tuple],
                        inst
                    )
                    return inst
            
                def __getitem__(self, name: int) -> Schema_.Items[str]:
                    return super().__getitem__(name)
            
            
            class ArrayArrayOfInteger(
                schemas.ListSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    
                    class Items(
                        schemas.ListSchema[schemas.T]
                    ):
                    
                    
                        class Schema_:
                            types = {tuple}
                            Items: typing_extensions.TypeAlias = schemas.Int64Schema[U]
                    
                        def __new__(
                            cls,
                            arg_: typing.Sequence[
                                typing.Union[
                                    Schema_.Items[decimal.Decimal],
                                    decimal.Decimal,
                                    int
                                ]
                            ],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                        ) -> ArrayTest.Schema_.Properties.ArrayArrayOfInteger.Schema_.Items[tuple]:
                            inst = super().__new__(
                                cls,
                                arg_,
                                configuration_=configuration_,
                            )
                            inst = typing.cast(
                                ArrayTest.Schema_.Properties.ArrayArrayOfInteger.Schema_.Items[tuple],
                                inst
                            )
                            return inst
                    
                        def __getitem__(self, name: int) -> Schema_.Items[decimal.Decimal]:
                            return super().__getitem__(name)
            
                def __new__(
                    cls,
                    arg_: typing.Sequence[
                        typing.Union[
                            Schema_.Items[tuple],
                            list,
                            tuple
                        ]
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> ArrayTest.Schema_.Properties.ArrayArrayOfInteger[tuple]:
                    inst = super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        ArrayTest.Schema_.Properties.ArrayArrayOfInteger[tuple],
                        inst
                    )
                    return inst
            
                def __getitem__(self, name: int) -> Schema_.Items[tuple]:
                    return super().__getitem__(name)
            
            
            class ArrayArrayOfModel(
                schemas.ListSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    
                    class Items(
                        schemas.ListSchema[schemas.T]
                    ):
                    
                    
                        class Schema_:
                            types = {tuple}
                            
                            @staticmethod
                            def items() -> typing.Type[read_only_first.ReadOnlyFirst]:
                                return read_only_first.ReadOnlyFirst
                    
                        def __new__(
                            cls,
                            arg_: typing.Sequence[
                                typing.Union[
                                    read_only_first.ReadOnlyFirst[frozendict.frozendict],
                                    dict,
                                    frozendict.frozendict
                                ]
                            ],
                            configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                        ) -> ArrayTest.Schema_.Properties.ArrayArrayOfModel.Schema_.Items[tuple]:
                            inst = super().__new__(
                                cls,
                                arg_,
                                configuration_=configuration_,
                            )
                            inst = typing.cast(
                                ArrayTest.Schema_.Properties.ArrayArrayOfModel.Schema_.Items[tuple],
                                inst
                            )
                            return inst
                    
                        def __getitem__(self, name: int) -> read_only_first.ReadOnlyFirst[frozendict.frozendict]:
                            return super().__getitem__(name)
            
                def __new__(
                    cls,
                    arg_: typing.Sequence[
                        typing.Union[
                            Schema_.Items[tuple],
                            list,
                            tuple
                        ]
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> ArrayTest.Schema_.Properties.ArrayArrayOfModel[tuple]:
                    inst = super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        ArrayTest.Schema_.Properties.ArrayArrayOfModel[tuple],
                        inst
                    )
                    return inst
            
                def __getitem__(self, name: int) -> Schema_.Items[tuple]:
                    return super().__getitem__(name)
            __annotations__ = {
                "array_of_string": ArrayOfString,
                "array_array_of_integer": ArrayArrayOfInteger,
                "array_array_of_model": ArrayArrayOfModel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_of_string"]) -> Schema_.Properties.ArrayOfString[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_array_of_integer"]) -> Schema_.Properties.ArrayArrayOfInteger[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_array_of_model"]) -> Schema_.Properties.ArrayArrayOfModel[tuple]: ...
    
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
            typing_extensions.Literal["array_of_string"],
            typing_extensions.Literal["array_array_of_integer"],
            typing_extensions.Literal["array_array_of_model"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        array_of_string: typing.Union[
            Schema_.Properties.ArrayOfString[tuple],
            schemas.Unset,
            list,
            tuple
        ] = schemas.unset,
        array_array_of_integer: typing.Union[
            Schema_.Properties.ArrayArrayOfInteger[tuple],
            schemas.Unset,
            list,
            tuple
        ] = schemas.unset,
        array_array_of_model: typing.Union[
            Schema_.Properties.ArrayArrayOfModel[tuple],
            schemas.Unset,
            list,
            tuple
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> ArrayTest[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            array_of_string=array_of_string,
            array_array_of_integer=array_array_of_integer,
            array_array_of_model=array_array_of_model,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            ArrayTest[frozendict.frozendict],
            inst
        )
        return inst

from petstore_api.components.schema import read_only_first
