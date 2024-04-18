# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import typing

from unit_test_api import exceptions


PYTHON_KEYWORD_TO_JSON_SCHEMA_KEYWORD = {
    'additional_properties': 'additionalProperties',
    'all_of': 'allOf',
    'any_of': 'anyOf',
    'const_value_to_name': 'const',
    'contains': 'contains',
    'dependent_required': 'dependentRequired',
    'dependent_schemas': 'dependentSchemas',
    'discriminator': 'discriminator',
    # default omitted because it has no validation impact
    'else_': 'else',
    'enum_value_to_name': 'enum',
    'exclusive_maximum': 'exclusiveMaximum',
    'exclusive_minimum': 'exclusiveMinimum',
    'format': 'format',
    'if_': 'if',
    'inclusive_maximum': 'maximum',
    'inclusive_minimum': 'minimum',
    'items': 'items',
    'max_contains': 'maxContains',
    'max_items': 'maxItems',
    'max_length': 'maxLength',
    'max_properties': 'maxProperties',
    'min_contains': 'minContains',
    'min_items': 'minItems',
    'min_length': 'minLength',
    'min_properties': 'minProperties',
    'multiple_of': 'multipleOf',
    'not_': 'not',
    'one_of': 'oneOf',
    'pattern': 'pattern',
    'pattern_properties': 'patternProperties',
    'prefix_items': 'prefixItems',
    'properties': 'properties',
    'property_names': 'propertyNames',
    'required': 'required',
    'then': 'then',
    'types': 'type',
    'unique_items': 'uniqueItems',
    'unevaluated_items': 'unevaluatedItems',
    'unevaluated_properties': 'unevaluatedProperties'
}

class SchemaConfiguration:
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator

    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    Do not edit the class manually.

    :param disabled_json_schema_keywords (set): Set of
      JSON schema validation keywords to disable JSON schema structural validation
      rules. The following keywords may be specified: multipleOf, maximum,
      exclusiveMaximum, minimum, exclusiveMinimum, maxLength, minLength, pattern,
      maxItems, minItems.
      By default, the validation is performed for data generated locally by the client
      and data received from the server, independent of any validation performed by
      the server side. If the input data does not satisfy the JSON schema validation
      rules specified in the OpenAPI document, an exception is raised.
      If disabled_json_schema_keywords is set, structural validation is
      disabled. This can be useful to troubleshoot data validation problem, such as
      when the OpenAPI document validation rules do not match the actual API data
      received by the server.
    :param server_index: Index to servers configuration.
    """

    def __init__(
        self,
        disabled_json_schema_keywords = set(),
    ):
        """Constructor
        """
        self.disabled_json_schema_keywords = disabled_json_schema_keywords

    @property
    def disabled_json_schema_python_keywords(self) -> typing.Set[str]:
        return self.__disabled_json_schema_python_keywords

    @property
    def disabled_json_schema_keywords(self) -> typing.Set[str]:
        return self.__disabled_json_schema_keywords

    @disabled_json_schema_keywords.setter
    def disabled_json_schema_keywords(self, json_keywords: typing.Set[str]):
        disabled_json_schema_keywords = set()
        disabled_json_schema_python_keywords = set()
        for k in json_keywords:
            python_keywords = {key for key, val in PYTHON_KEYWORD_TO_JSON_SCHEMA_KEYWORD.items() if val == k}
            if not python_keywords:
                raise exceptions.ApiValueError(
                    "Invalid keyword: '{0}''".format(k))
            disabled_json_schema_keywords.add(k)
            disabled_json_schema_python_keywords.update(python_keywords)
        self.__disabled_json_schema_keywords = disabled_json_schema_keywords
        self.__disabled_json_schema_python_keywords = disabled_json_schema_python_keywords