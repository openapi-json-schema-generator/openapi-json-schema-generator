# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3

from petstore_api import api_client, exceptions
from . import schema


parameter_oapg = api_client.QueryParameter(
    name="enum_query_double",
    style=api_client.ParameterStyle.FORM,
    schema=schema.Schema,
    explode=True,
)
