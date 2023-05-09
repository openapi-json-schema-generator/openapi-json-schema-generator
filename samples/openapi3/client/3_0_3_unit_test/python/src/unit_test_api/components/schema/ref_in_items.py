# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from unit_test_api.shared_imports.schema_imports import *


class RefInItems(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {tuple}
        
        @staticmethod
        def items() -> typing.Type['property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference']:
            return property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference

    def __new__(
        cls,
        arg_: typing.Union[
            typing.Tuple[
                typing.Union['property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference', dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader], ...
            ],
            typing.List[
                typing.Union['property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference', dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader]
            ],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'RefInItems':
        return super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )

    def __getitem__(self, i: int) -> 'property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference':
        return super().__getitem__(i)

from unit_test_api.components.schema import property_named_ref_that_is_not_a_reference
