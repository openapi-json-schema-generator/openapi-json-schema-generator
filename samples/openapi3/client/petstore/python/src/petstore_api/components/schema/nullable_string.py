# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class NullableString(
    schemas.NoneBase,
    schemas.StrBase,
    schemas.Schema[schemas.T],
    schemas.NoneStrMixin
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {
            schemas.NoneClass,
            str,
        }


    def __new__(
        cls,
        arg_: typing.Union[None, str],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> NullableString[
        typing.Union[
            schemas.NoneClass,
            str
        ]
    ]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            NullableString[
                typing.Union[
                    schemas.NoneClass,
                    str
                ]
            ],
            inst
        )
        return inst

