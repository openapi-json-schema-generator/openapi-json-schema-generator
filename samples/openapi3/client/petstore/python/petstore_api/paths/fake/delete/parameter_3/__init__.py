# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3

from petstore_api import api_client, exceptions
from . import schema


class _3(api_client.QueryParameter):
    name = "string_group"
    style = api_client.ParameterStyle.FORM,
    schema = schema.Schema
    explode = True
