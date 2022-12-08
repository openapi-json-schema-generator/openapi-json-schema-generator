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




class schema(
    schemas.DictSchema
):


    class MetaOapg:
        types = {frozendict.frozendict}
        additional_properties = schemas.StrSchema
    def __getitem__(self, name: str) -> MetaOapg.additional_properties
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    def get_item_oapg(self, name: typing.Union[str]) -> MetaOapg.additional_properties:
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
    ) -> 'schema':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

parameter_oapg = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=schema
        ),
    },
    required=True,
)
