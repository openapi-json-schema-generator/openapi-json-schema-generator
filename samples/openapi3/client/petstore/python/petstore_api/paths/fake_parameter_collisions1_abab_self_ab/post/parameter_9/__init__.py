# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3

from petstore_api import api_client, exceptions
from . import schema


class _9(api_client.PathParameter):
    name = "1"
    style = api_client.ParameterStyle.SIMPLE
    schema = schema.Schema
    required = True
