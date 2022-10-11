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

from petstore_api.components.schema import pet_oapg


class BodySchemas:
    # body schemas
    
    
    class application_xml(
        schemas.ListSchema
    ):
    
    
        class MetaOapg:
            
            @staticmethod
            def items() -> typing.Type['pet_oapg.Pet']:
                return pet_oapg.Pet
    
        def __new__(
            cls,
            arg: typing.Union[typing.Tuple['pet_oapg.Pet'], typing.List['pet_oapg.Pet']],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'application_xml':
            return super().__new__(
                cls,
                arg,
                _configuration=_configuration,
            )
    
        def __getitem__(self, i: int) -> 'pet_oapg.Pet':
            return super().__getitem__(i)
    
    
    class application_json(
        schemas.ListSchema
    ):
    
    
        class MetaOapg:
            
            @staticmethod
            def items() -> typing.Type['pet_oapg.Pet']:
                return pet_oapg.Pet
    
        def __new__(
            cls,
            arg: typing.Union[typing.Tuple['pet_oapg.Pet'], typing.List['pet_oapg.Pet']],
            _configuration: typing.Optional[schemas.Configuration] = None,
        ) -> 'application_json':
            return super().__new__(
                cls,
                arg,
                _configuration=_configuration,
            )
    
        def __getitem__(self, i: int) -> 'pet_oapg.Pet':
            return super().__getitem__(i)
    pass


@dataclasses.dataclass
class ApiResponse(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        BodySchemas.application_xml,
        BodySchemas.application_json,
    ]
    headers: schemas.Unset = schemas.unset


response = api_client.OpenApiResponse(
    response_cls=ApiResponse,
    content={
        'application/xml': api_client.MediaType(
            schema=BodySchemas.application_xml,
        ),
        'application/json': api_client.MediaType(
            schema=BodySchemas.application_json,
        ),
    },
)
