# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3

from petstore_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401




class application_x_www_form_urlencoded(
    schemas.DictSchema
):


    class MetaOapg:
        types = {frozendict.frozendict}
        required = {
            "byte",
            "double",
            "number",
            "pattern_without_delimiter",
        }
        
        class properties:
            
            
            class integer(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'int'
                    inclusive_maximum = 100
                    inclusive_minimum = 10
            
            
            class int32(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'int32'
                    inclusive_maximum = 200
                    inclusive_minimum = 20
            int64 = schemas.Int64Schema
            
            
            class number(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    types = {
                        decimal.Decimal,
                    }
                    inclusive_maximum = 543.2
                    inclusive_minimum = 32.1
            
            
            class _float(
                schemas.Float32Schema
            ):
            
            
                class MetaOapg:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'float'
                    inclusive_maximum = 987.6
            
            
            class double(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'double'
                    inclusive_maximum = 123.4
                    inclusive_minimum = 67.8
            
            
            class string(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    types = {
                        str,
                    }
                    regex={
                        'pattern': r'[a-z]',  # noqa: E501
                        'flags': (
                            re.IGNORECASE
                        )
                    }
            
            
            class pattern_without_delimiter(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    types = {
                        str,
                    }
                    regex={
                        'pattern': r'^[A-Z].*',  # noqa: E501
                    }
            byte = schemas.StrSchema
            binary = schemas.BinarySchema
            date = schemas.DateSchema
            dateTime = schemas.DateTimeSchema
            
            
            class password(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    types = {
                        str,
                    }
                    format = 'password'
                    max_length = 64
                    min_length = 10
            callback = schemas.StrSchema
            __annotations__ = {
                "integer": integer,
                "int32": int32,
                "int64": int64,
                "number": number,
                "float": _float,
                "double": double,
                "string": string,
                "pattern_without_delimiter": pattern_without_delimiter,
                "byte": byte,
                "binary": binary,
                "date": date,
                "dateTime": dateTime,
                "password": password,
                "callback": callback,
            }
    
    byte: MetaOapg.properties.byte
    double: MetaOapg.properties.double
    number: MetaOapg.properties.number
    pattern_without_delimiter: MetaOapg.properties.pattern_without_delimiter
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integer"]) -> MetaOapg.properties.integer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int32"]) -> MetaOapg.properties.int32: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int64"]) -> MetaOapg.properties.int64: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float"]) -> MetaOapg.properties._float: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double"]) -> MetaOapg.properties.double: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["string"]) -> MetaOapg.properties.string: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pattern_without_delimiter"]) -> MetaOapg.properties.pattern_without_delimiter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["byte"]) -> MetaOapg.properties.byte: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["binary"]) -> MetaOapg.properties.binary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> MetaOapg.properties.dateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callback"]) -> MetaOapg.properties.callback: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["integer", "int32", "int64", "number", "float", "double", "string", "pattern_without_delimiter", "byte", "binary", "date", "dateTime", "password", "callback", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["integer"]) -> typing.Union[MetaOapg.properties.integer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["int32"]) -> typing.Union[MetaOapg.properties.int32, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["int64"]) -> typing.Union[MetaOapg.properties.int64, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["float"]) -> typing.Union[MetaOapg.properties._float, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["double"]) -> MetaOapg.properties.double: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["string"]) -> typing.Union[MetaOapg.properties.string, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pattern_without_delimiter"]) -> MetaOapg.properties.pattern_without_delimiter: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["byte"]) -> MetaOapg.properties.byte: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["binary"]) -> typing.Union[MetaOapg.properties.binary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTime"]) -> typing.Union[MetaOapg.properties.dateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callback"]) -> typing.Union[MetaOapg.properties.callback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["integer", "int32", "int64", "number", "float", "double", "string", "pattern_without_delimiter", "byte", "binary", "date", "dateTime", "password", "callback", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        byte: typing.Union[MetaOapg.properties.byte, str, ],
        double: typing.Union[MetaOapg.properties.double, decimal.Decimal, int, float, ],
        number: typing.Union[MetaOapg.properties.number, decimal.Decimal, int, float, ],
        pattern_without_delimiter: typing.Union[MetaOapg.properties.pattern_without_delimiter, str, ],
        integer: typing.Union[MetaOapg.properties.integer, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int32: typing.Union[MetaOapg.properties.int32, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        int64: typing.Union[MetaOapg.properties.int64, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        string: typing.Union[MetaOapg.properties.string, str, schemas.Unset] = schemas.unset,
        binary: typing.Union[MetaOapg.properties.binary, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, date, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[MetaOapg.properties.dateTime, str, datetime, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        callback: typing.Union[MetaOapg.properties.callback, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'application_x_www_form_urlencoded':
        return super().__new__(
            cls,
            *_args,
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
            _configuration=_configuration,
            **kwargs,
        )

parameter_oapg = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=application_x_www_form_urlencoded
        ),
    },
)
