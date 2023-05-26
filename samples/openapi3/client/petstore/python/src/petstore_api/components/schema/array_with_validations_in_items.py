# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class ArrayWithValidationsInItems(
    schemas.ListSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {tuple}
        max_items = 2
        
        
        class Items(
            schemas.Int64Schema[schemas.T]
        ):
        
        
            class Schema_:
                types = {
                    decimal.Decimal,
                }
                format = 'int64'
                inclusive_maximum = 7

    def __new__(
        cls,
        arg_: typing.Union[
            typing.Tuple[
                typing.Union[
                    Schema_.Items,
                    decimal.Decimal,
                    int
                ], ...
            ],
            typing.List[
                typing.Union[
                    Schema_.Items,
                    decimal.Decimal,
                    int
                ]
            ],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> ArrayWithValidationsInItems[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ArrayWithValidationsInItems[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Schema_.Items[decimal.Decimal]:
        return super().__getitem__(name)
