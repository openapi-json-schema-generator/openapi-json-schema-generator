# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *


class TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class Alpha(
                schemas.NumberSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    inclusive_maximum = 3
                    default = 5
            __annotations__ = {
                "alpha": Alpha,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alpha"]) -> Schema_.Properties.Alpha[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.AnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["alpha"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        alpha: typing.Union[Schema_.Properties.Alpha, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            alpha=alpha,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing[frozendict.frozendict],
            inst
        )
        return inst
