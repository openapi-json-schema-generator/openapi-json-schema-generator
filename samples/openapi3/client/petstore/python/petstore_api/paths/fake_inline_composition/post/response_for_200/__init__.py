import dataclasses
import urllib3

from petstore_api import api_client
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

# body schemas


class application_json(
    schemas.ComposedSchema,
):


    class MetaOapg(schemas.JsonSchemaValidator):
        types = None
        
        class all_of:
            
            
            class all_of_0(
                schemas.StrSchema
            ):
            
            
                class MetaOapg(schemas.JsonSchemaValidator):
                    types = {
                        str,
                    }
                    min_length = 1
            classes = [
                all_of_0,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'application_json':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )


class multipart_form_data(
    schemas.DictSchema
):


    class MetaOapg(schemas.JsonSchemaValidator):
        types = {frozendict.frozendict}
        
        class properties:
            
            
            class someProp(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg(schemas.JsonSchemaValidator):
                    types = None
                    
                    class all_of:
                        
                        
                        class all_of_0(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg(schemas.JsonSchemaValidator):
                                types = {
                                    str,
                                }
                                min_length = 1
                        classes = [
                            all_of_0,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'someProp':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "someProp": someProp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someProp"]) -> MetaOapg.properties.someProp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["someProp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["someProp"]) -> typing.Union[MetaOapg.properties.someProp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["someProp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        someProp: typing.Union[MetaOapg.properties.someProp, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'multipart_form_data':
        return super().__new__(
            cls,
            *_args,
            someProp=someProp,
            _configuration=_configuration,
            **kwargs,
        )


@dataclasses.dataclass
class ApiResponse(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        application_json,
        multipart_form_data,
    ]
    headers: schemas.Unset = schemas.unset


response = api_client.OpenApiResponse(
    response_cls=ApiResponse,
    content={
        'application/json': api_client.MediaType(
            schema=application_json,
        ),
        'multipart/form-data': api_client.MediaType(
            schema=multipart_form_data,
        ),
    },
)
