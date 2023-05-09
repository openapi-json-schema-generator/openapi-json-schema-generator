# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.schema_imports import *


class Schema(
    schemas.DictSchema
):


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "byte",
            "double",
            "number",
            "pattern_without_delimiter",
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
            
            
            class Int32(
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
            
            
            class _Float(
                schemas.Float32Schema
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'float'
                    inclusive_maximum = 987.6
            
            
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
            
            
            class PatternWithoutDelimiter(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    regex={
                        'pattern': r'^[A-Z].*',  # noqa: E501
                    }
            Byte = schemas.StrSchema
            Binary = schemas.BinarySchema
            Date = schemas.DateSchema
            
            
            class DateTime(
                schemas.DateTimeSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    format = 'date-time'
            
            
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
            Callback = schemas.StrSchema
            __annotations__ = {
                "integer": Integer,
                "int32": Int32,
                "int64": Int64,
                "number": Number,
                "float": _Float,
                "double": Double,
                "string": String,
                "pattern_without_delimiter": PatternWithoutDelimiter,
                "byte": Byte,
                "binary": Binary,
                "date": Date,
                "dateTime": DateTime,
                "password": Password,
                "callback": Callback,
            }
    
    @property
    def byte(self) -> Schema_.Properties.Byte:
        return self.__getitem__("byte")
    
    @property
    def double(self) -> Schema_.Properties.Double:
        return self.__getitem__("double")
    
    @property
    def number(self) -> Schema_.Properties.Number:
        return self.__getitem__("number")
    
    @property
    def pattern_without_delimiter(self) -> Schema_.Properties.PatternWithoutDelimiter:
        return self.__getitem__("pattern_without_delimiter")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["byte"]) -> Schema_.Properties.Byte: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double"]) -> Schema_.Properties.Double: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> Schema_.Properties.Number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pattern_without_delimiter"]) -> Schema_.Properties.PatternWithoutDelimiter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integer"]) -> Schema_.Properties.Integer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int32"]) -> Schema_.Properties.Int32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int64"]) -> Schema_.Properties.Int64: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float"]) -> Schema_.Properties._Float: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["string"]) -> Schema_.Properties.String: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["binary"]) -> Schema_.Properties.Binary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> Schema_.Properties.Date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> Schema_.Properties.DateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> Schema_.Properties.Password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callback"]) -> Schema_.Properties.Callback: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["byte"],
            typing_extensions.Literal["double"],
            typing_extensions.Literal["number"],
            typing_extensions.Literal["pattern_without_delimiter"],
            typing_extensions.Literal["integer"],
            typing_extensions.Literal["int32"],
            typing_extensions.Literal["int64"],
            typing_extensions.Literal["float"],
            typing_extensions.Literal["string"],
            typing_extensions.Literal["binary"],
            typing_extensions.Literal["date"],
            typing_extensions.Literal["dateTime"],
            typing_extensions.Literal["password"],
            typing_extensions.Literal["callback"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        byte: typing.Union[Schema_.Properties.Byte, str],
        double: typing.Union[Schema_.Properties.Double, decimal.Decimal, int, float],
        number: typing.Union[Schema_.Properties.Number, decimal.Decimal, int, float],
        pattern_without_delimiter: typing.Union[Schema_.Properties.PatternWithoutDelimiter, str],
        integer: typing.Union[Schema_.Properties.Integer, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int32: typing.Union[Schema_.Properties.Int32, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int64: typing.Union[Schema_.Properties.Int64, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        string: typing.Union[Schema_.Properties.String, str, schemas.Unset] = schemas.unset,
        binary: typing.Union[Schema_.Properties.Binary, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        date: typing.Union[Schema_.Properties.Date, str, datetime.date, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[Schema_.Properties.DateTime, str, datetime.datetime, schemas.Unset] = schemas.unset,
        password: typing.Union[Schema_.Properties.Password, str, schemas.Unset] = schemas.unset,
        callback: typing.Union[Schema_.Properties.Callback, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'Schema':
        return super().__new__(
            cls,
            *args_,
            byte=byte,
            double=double,
            number=number,
            pattern_without_delimiter=pattern_without_delimiter,
            integer=integer,
            int32=int32,
            int64=int64,
            string=string,
            binary=binary,
            date=date,
            dateTime=dateTime,
            password=password,
            callback=callback,
            configuration_=configuration_,
            **kwargs,
        )
