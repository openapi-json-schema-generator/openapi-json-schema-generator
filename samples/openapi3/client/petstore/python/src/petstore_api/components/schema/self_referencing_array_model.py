# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class SelfReferencingArrayModel(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {tuple}
        
        @staticmethod
        def items() -> typing.Type['SelfReferencingArrayModel']:
            return SelfReferencingArrayModel

    def __new__(
        cls,
        arg_: typing.Union[
            typing.Tuple[
                typing.Union['SelfReferencingArrayModel', list, tuple], ...
            ],
            typing.List[
                typing.Union['SelfReferencingArrayModel', list, tuple]
            ],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'SelfReferencingArrayModel':
        return super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )

    def __getitem__(self, i: int) -> 'SelfReferencingArrayModel':
        return super().__getitem__(i)
