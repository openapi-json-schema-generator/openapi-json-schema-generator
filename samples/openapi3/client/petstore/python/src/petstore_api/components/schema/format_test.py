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


class FormatTest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "byte",
            "date",
            "number",
            "password",
        }
        
        class Properties:
            
            
            class Integer(
                schemas.IntSchema
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'int'
                    inclusive_maximum = 100
                    inclusive_minimum = 10
                    multiple_of = 2
            Int32 = schemas.Int32Schema
            
            
            class Int32withValidations(
                schemas.Int32Schema
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'int32'
                    inclusive_maximum = 200
                    inclusive_minimum = 20
            Int64 = schemas.Int64Schema
            
            
            class Number(
                schemas.NumberSchema
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    inclusive_maximum = 543.2
                    inclusive_minimum = 32.1
                    multiple_of = 32.5
            
            
            class _Float(
                schemas.Float32Schema
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'float'
                    inclusive_maximum = 987.6
                    inclusive_minimum = 54.3
            Float32 = schemas.Float32Schema
            
            
            class Double(
                schemas.Float64Schema
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'double'
                    inclusive_maximum = 123.4
                    inclusive_minimum = 67.8
            Float64 = schemas.Float64Schema
            
            
            class ArrayWithUniqueItems(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    unique_items = True
                    Items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[Schema_.Items, decimal.Decimal, int, float], ...
                        ],
                        typing.List[
                            typing.Union[Schema_.Items, decimal.Decimal, int, float]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'ArrayWithUniqueItems':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            
            
            class String(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    regex={
                        'pattern': r'[a-z]',  # noqa: E501
                        'flags': re.I,
                    }
            Byte = schemas.StrSchema
            Binary = schemas.BinarySchema
            Date = schemas.DateSchema
            DateTime = schemas.DateTimeSchema
            Uuid = schemas.UUIDSchema
            UuidNoExample = schemas.UUIDSchema
            
            
            class Password(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    format = 'password'
                    max_length = 64
                    min_length = 10
            
            
            class PatternWithDigits(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    regex={
                        'pattern': r'^\d{10}$',  # noqa: E501
                    }
            
            
            class PatternWithDigitsAndDelimiter(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    regex={
                        'pattern': r'^image_\d{1,3}$',  # noqa: E501
                        'flags': re.I,
                    }
            NoneProp = schemas.NoneSchema
            __annotations__ = {
                "integer": Integer,
                "int32": Int32,
                "int32withValidations": Int32withValidations,
                "int64": Int64,
                "number": Number,
                "float": _Float,
                "float32": Float32,
                "double": Double,
                "float64": Float64,
                "arrayWithUniqueItems": ArrayWithUniqueItems,
                "string": String,
                "byte": Byte,
                "binary": Binary,
                "date": Date,
                "dateTime": DateTime,
                "uuid": Uuid,
                "uuidNoExample": UuidNoExample,
                "password": Password,
                "pattern_with_digits": PatternWithDigits,
                "pattern_with_digits_and_delimiter": PatternWithDigitsAndDelimiter,
                "noneProp": NoneProp,
            }
    
    byte: Schema_.Properties.Byte
    date: Schema_.Properties.Date
    number: Schema_.Properties.Number
    password: Schema_.Properties.Password
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["byte"]) -> Schema_.Properties.Byte: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> Schema_.Properties.Date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> Schema_.Properties.Number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> Schema_.Properties.Password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integer"]) -> Schema_.Properties.Integer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int32"]) -> Schema_.Properties.Int32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int32withValidations"]) -> Schema_.Properties.Int32withValidations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int64"]) -> Schema_.Properties.Int64: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float"]) -> Schema_.Properties._Float: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float32"]) -> Schema_.Properties.Float32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double"]) -> Schema_.Properties.Double: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float64"]) -> Schema_.Properties.Float64: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arrayWithUniqueItems"]) -> Schema_.Properties.ArrayWithUniqueItems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["string"]) -> Schema_.Properties.String: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["binary"]) -> Schema_.Properties.Binary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> Schema_.Properties.DateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> Schema_.Properties.Uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuidNoExample"]) -> Schema_.Properties.UuidNoExample: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pattern_with_digits"]) -> Schema_.Properties.PatternWithDigits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pattern_with_digits_and_delimiter"]) -> Schema_.Properties.PatternWithDigitsAndDelimiter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["noneProp"]) -> Schema_.Properties.NoneProp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["byte"],
            typing_extensions.Literal["date"],
            typing_extensions.Literal["number"],
            typing_extensions.Literal["password"],
            typing_extensions.Literal["integer"],
            typing_extensions.Literal["int32"],
            typing_extensions.Literal["int32withValidations"],
            typing_extensions.Literal["int64"],
            typing_extensions.Literal["float"],
            typing_extensions.Literal["float32"],
            typing_extensions.Literal["double"],
            typing_extensions.Literal["float64"],
            typing_extensions.Literal["arrayWithUniqueItems"],
            typing_extensions.Literal["string"],
            typing_extensions.Literal["binary"],
            typing_extensions.Literal["dateTime"],
            typing_extensions.Literal["uuid"],
            typing_extensions.Literal["uuidNoExample"],
            typing_extensions.Literal["pattern_with_digits"],
            typing_extensions.Literal["pattern_with_digits_and_delimiter"],
            typing_extensions.Literal["noneProp"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["byte"]) -> Schema_.Properties.Byte: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["date"]) -> Schema_.Properties.Date: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["number"]) -> Schema_.Properties.Number: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["password"]) -> Schema_.Properties.Password: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["integer"]) -> typing.Union[Schema_.Properties.Integer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["int32"]) -> typing.Union[Schema_.Properties.Int32, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["int32withValidations"]) -> typing.Union[Schema_.Properties.Int32withValidations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["int64"]) -> typing.Union[Schema_.Properties.Int64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["float"]) -> typing.Union[Schema_.Properties._Float, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["float32"]) -> typing.Union[Schema_.Properties.Float32, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["double"]) -> typing.Union[Schema_.Properties.Double, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["float64"]) -> typing.Union[Schema_.Properties.Float64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["arrayWithUniqueItems"]) -> typing.Union[Schema_.Properties.ArrayWithUniqueItems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["string"]) -> typing.Union[Schema_.Properties.String, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["binary"]) -> typing.Union[Schema_.Properties.Binary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["dateTime"]) -> typing.Union[Schema_.Properties.DateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[Schema_.Properties.Uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["uuidNoExample"]) -> typing.Union[Schema_.Properties.UuidNoExample, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["pattern_with_digits"]) -> typing.Union[Schema_.Properties.PatternWithDigits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["pattern_with_digits_and_delimiter"]) -> typing.Union[Schema_.Properties.PatternWithDigitsAndDelimiter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["noneProp"]) -> typing.Union[Schema_.Properties.NoneProp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["byte"],
            typing_extensions.Literal["date"],
            typing_extensions.Literal["number"],
            typing_extensions.Literal["password"],
            typing_extensions.Literal["integer"],
            typing_extensions.Literal["int32"],
            typing_extensions.Literal["int32withValidations"],
            typing_extensions.Literal["int64"],
            typing_extensions.Literal["float"],
            typing_extensions.Literal["float32"],
            typing_extensions.Literal["double"],
            typing_extensions.Literal["float64"],
            typing_extensions.Literal["arrayWithUniqueItems"],
            typing_extensions.Literal["string"],
            typing_extensions.Literal["binary"],
            typing_extensions.Literal["dateTime"],
            typing_extensions.Literal["uuid"],
            typing_extensions.Literal["uuidNoExample"],
            typing_extensions.Literal["pattern_with_digits"],
            typing_extensions.Literal["pattern_with_digits_and_delimiter"],
            typing_extensions.Literal["noneProp"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        byte: typing.Union[Schema_.Properties.Byte, str],
        date: typing.Union[Schema_.Properties.Date, str, datetime.date],
        number: typing.Union[Schema_.Properties.Number, decimal.Decimal, int, float],
        password: typing.Union[Schema_.Properties.Password, str],
        integer: typing.Union[Schema_.Properties.Integer, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int32: typing.Union[Schema_.Properties.Int32, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int32withValidations: typing.Union[Schema_.Properties.Int32withValidations, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int64: typing.Union[Schema_.Properties.Int64, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        float32: typing.Union[Schema_.Properties.Float32, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        double: typing.Union[Schema_.Properties.Double, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        float64: typing.Union[Schema_.Properties.Float64, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        arrayWithUniqueItems: typing.Union[Schema_.Properties.ArrayWithUniqueItems, list, tuple, schemas.Unset] = schemas.unset,
        string: typing.Union[Schema_.Properties.String, str, schemas.Unset] = schemas.unset,
        binary: typing.Union[Schema_.Properties.Binary, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[Schema_.Properties.DateTime, str, datetime.datetime, schemas.Unset] = schemas.unset,
        uuid: typing.Union[Schema_.Properties.Uuid, str, uuid.UUID, schemas.Unset] = schemas.unset,
        uuidNoExample: typing.Union[Schema_.Properties.UuidNoExample, str, uuid.UUID, schemas.Unset] = schemas.unset,
        pattern_with_digits: typing.Union[Schema_.Properties.PatternWithDigits, str, schemas.Unset] = schemas.unset,
        pattern_with_digits_and_delimiter: typing.Union[Schema_.Properties.PatternWithDigitsAndDelimiter, str, schemas.Unset] = schemas.unset,
        noneProp: typing.Union[Schema_.Properties.NoneProp, None, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'FormatTest':
        return super().__new__(
            cls,
            *args_,
            byte=byte,
            date=date,
            number=number,
            password=password,
            integer=integer,
            int32=int32,
            int32withValidations=int32withValidations,
            int64=int64,
            float32=float32,
            double=double,
            float64=float64,
            arrayWithUniqueItems=arrayWithUniqueItems,
            string=string,
            binary=binary,
            dateTime=dateTime,
            uuid=uuid,
            uuidNoExample=uuidNoExample,
            pattern_with_digits=pattern_with_digits,
            pattern_with_digits_and_delimiter=pattern_with_digits_and_delimiter,
            noneProp=noneProp,
            configuration_=configuration_,
            **kwargs,
        )
