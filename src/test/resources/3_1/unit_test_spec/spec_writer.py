import dataclasses
import re
import json
import pathlib
import typing

import yaml

"""
This file ingests json schemas from
https://github.com/json-schema-org/JSON-Schema-Test-Suite/tree/main/tests
and writes those test schemas and test cases into a sample openapi spec document
That spec document can then be used to write clients or server stubs which
can contain autogenerated tests that use the json schema test cases

The python-experimental client is the first user of this test spec.

TODO:
- [DONE] load json file and write it into components/schemas
- [DONE] ensure that examples are being written there
- [DONE] add recursive casting of test examples to ObjectWithTypeBooleans
- [DONE] move processing to defaultCodegen
- [DONE] turn tests on
- add endpoints with those components in:
- request body
- response body
- all parameter types
- add main spec that uses type spec
"""

@dataclasses.dataclass
class JsonSchemaTestCase:
    description: str
    data: typing.Union[str, int, float, bool, None, list, dict]
    valid: bool
    comment: typing.Optional[str] = None

JsonSchemaDict = typing.TypedDict(
    'JsonSchema',
    {
        'additionalProperties': 'JsonSchema',
        'allOf': typing.List['JsonSchema'],
        'anyOf': typing.List['JsonSchema'],
        'const': typing.Any,
        'default': typing.Any,
        'enum': typing.List[typing.Any],
        'exclusiveMaximum': typing.Union[int, float],
        'exclusiveMinimum': typing.Union[int, float],
        'format': str,
        'items': 'JsonSchema',
        'maximum': typing.Union[int, float],
        'maxItems': int,
        'maxLength': int,
        'maxProperties': int,
        'minimum': typing.Union[int, float],
        'minItems': int,
        'minLength': int,
        'minProperties': int,
        'multipleOf': typing.Union[int, float],
        'not': 'JsonSchema',
        'oneOf': typing.List['JsonSchema'],
        'pattern': str,
        'properties': typing.Dict[str, 'JsonSchema'],
        '$ref': str,
        'required': typing.List[str],
        'type': str,
        'uniqueItems': bool,
    },
    total=False
)

JsonSchema = typing.Union['JsonSchemaDict', bool]

@dataclasses.dataclass
class JsonSchemaTestSchema:
    description: str
    schema: JsonSchema
    tests: typing.List[JsonSchemaTestCase]
    comment: typing.Optional[str] = None


class ExclusionReason:
    v303_does_not_support_array_of_types = 'v3.0.3 does not support type with array of values'
    v303_requires_array_have_items = 'v3.0.3 requires that items MUST be present if the type is array'
    v303_does_not_support_additionalItems = 'v3.0.3 does not support the additionalItems keyword'
    bug_does_not_support_boolean_schemas_in_location = 'v3.1.0 does not support boolean schemas in location, https://github.com/swagger-api/swagger-parser/issues/1770'
    v303_does_not_support_contains = 'v3.0.3 does not support the contains keyword'
    bug_does_not_support_definitions = 'swagger-parser does not support the $defs keyword, https://github.com/swagger-api/swagger-parser/issues/1970'
    v303_does_not_support_dependencies = 'v3.0.3 does not support the dependencies keyword'
    swagger_parser_enum_type_bug = "swagger-parser has a bug where schema type is incorrectly set for an enum, https://github.com/swagger-api/swagger-parser/issues/1761"
    swagger_parser_validation_missing_bug = 'swagger-parser has a bug where validations are unset, https://github.com/swagger-api/swagger-parser/issues/1762'
    swagger_parser_items_type_bug = "swagger-parser has a bug where schema type is incorrectly set with items, https://github.com/swagger-api/swagger-parser/issues/1763"
    v303_does_not_support_id = 'v3.0.3 does not support the $id keyword'
    v303_does_not_support_propertyNames = 'v3.0.3 does not support the propertyNames keyword'
    v303_does_not_support_items_schema_array = 'v3.0.3 does not support an array of schemas for items'
    swagger_parser_exception = 'swagger-parser threw and exception for this test case'
    ref_location_not_the_same_for_json_and_openapi = 'the location referenced is not the same going from json schema to openapi'
    ref_to_adjacent_property_bug = 'Refing an adjacent property does not work, issue at https://github.com/OpenAPITools/openapi-generator/issues/12729'
    swagger_parser_anytype_bug = 'Swagger parser sets type incorrectly for this anyType schema https://github.com/swagger-api/swagger-parser/issues/1603'
    component_ref_component_bug = 'A component refing another component does not work, issue at https://github.com/OpenAPITools/openapi-generator/issues/12730'
    not_running_the_localhost_server = 'the openapo-generator is not running the localhost server needed to serve remoteRef files'
    v303_requires_that_the_default_value_is_an_allowed_type = 'v3.0.3 requires that the default value is an allowed type per the schema'
    ref_not_resolved = 'ref not resolved, TODO resolve only remote refs'
    bug_max_items_missing = 'swagger-parser has a bug where maxItems is omitted: https://github.com/swagger-api/swagger-parser/issues/1974'
    bug_with_non_string_const_values = 'swagger-parser const bug: https://github.com/swagger-api/swagger-parser/issues/1975'
    bug_dependent_required_values_incorrect = 'swagger parser bug where dependentRequired values are incorrect https://github.com/swagger-api/swagger-parser/issues/1978'
    bug_max_contains_lacks_float_value = 'swagger-parser bug where float values for maxContains are omitted https://github.com/swagger-api/swagger-parser/issues/1979'
    bug_type_set_for_any_type = 'swagger-parser bug where type is set for any type schema: https://github.com/swagger-api/swagger-parser/issues/1964'

json_schema_test_draft = 'draft2020-12'
path_to_json_schema_drafts = ('..', '..', 'JSON-Schema-Test-Suite', 'tests')
openapi_additions = 'openapi_additions'

FILEPATH_TO_EXCLUDED_CASE_AND_REASON = {
    (json_schema_test_draft, 'additionalProperties.json'): {
        "additionalProperties being false does not allow other properties": ExclusionReason.bug_type_set_for_any_type,
    },
    (json_schema_test_draft, 'allOf.json'): {
        'allOf with boolean schemas, all true': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'allOf with boolean schemas, some false': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'allOf with boolean schemas, all false': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'anyOf.json'): {
        'anyOf with boolean schemas, all true': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'anyOf with boolean schemas, some true': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'anyOf with boolean schemas, all false': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'const.json'): {
        'const with array': ExclusionReason.bug_with_non_string_const_values,
        "const with false does not match 0": ExclusionReason.bug_with_non_string_const_values,
        'const with object': ExclusionReason.bug_with_non_string_const_values,
        "const with true does not match 1": ExclusionReason.bug_with_non_string_const_values,
        'const with {"a": false} does not match {"a": 0}': ExclusionReason.bug_with_non_string_const_values,
        'const with {"a": true} does not match {"a": 1}': ExclusionReason.bug_with_non_string_const_values,
        "const with [false] does not match [0]": ExclusionReason.bug_with_non_string_const_values,
        "const with [true] does not match [1]": ExclusionReason.bug_with_non_string_const_values,
        "float and integers are equal up to 64-bit representation limits": ExclusionReason.bug_with_non_string_const_values,
        "const validation": ExclusionReason.bug_with_non_string_const_values,
        "const with 0 does not match other zero-like types": ExclusionReason.bug_with_non_string_const_values,
        "const with 1 does not match true": ExclusionReason.bug_with_non_string_const_values,
        "const with -2.0 matches integer and float types": ExclusionReason.bug_with_non_string_const_values,
        "const with null": ExclusionReason.bug_with_non_string_const_values,
    },
    (json_schema_test_draft, 'contains.json'): {
        "contains keyword with boolean schema false": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "contains with false if subschema": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "contains keyword with boolean schema true": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "contains keyword with const keyword": ExclusionReason.bug_with_non_string_const_values,
    },
    (json_schema_test_draft, 'default.json'): {
        'invalid type for default': ExclusionReason.v303_requires_that_the_default_value_is_an_allowed_type,
    },
    (json_schema_test_draft, 'dependentRequired.json'): {
        "dependencies with escaped characters": ExclusionReason.bug_dependent_required_values_incorrect,
    },
    (json_schema_test_draft, 'dependentSchemas.json'): {
        "boolean subschemas": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'enum.json'): {
        'heterogeneous enum validation': ExclusionReason.swagger_parser_enum_type_bug,
        'heterogeneous enum-with-null validation': ExclusionReason.swagger_parser_enum_type_bug,
    },
    (json_schema_test_draft, 'items.json'): {
        'an array of schemas for items': ExclusionReason.v303_does_not_support_array_of_types,
        'items and subitems': ExclusionReason.bug_does_not_support_definitions,
        'items with boolean schema (true)': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'items with boolean schemas': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'items with boolean schema (false)': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'items with boolean schema (false)': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'a schema given for items': ExclusionReason.swagger_parser_items_type_bug,
        'prefixItems with no additional items allowed': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'maxContains.json'): {
        "maxContains with contains, value with a decimal": ExclusionReason.bug_max_contains_lacks_float_value,
        "maxContains with contains": ExclusionReason.bug_with_non_string_const_values,
        "minContains < maxContains": ExclusionReason.bug_with_non_string_const_values,
    },
    (json_schema_test_draft, 'maxItems.json'): {
        'maxItems validation with a decimal': ExclusionReason.bug_max_items_missing,
    },
    (json_schema_test_draft, 'maxLength.json'): {
        'maxLength validation with a decimal': ExclusionReason.bug_max_items_missing,
    },
    (json_schema_test_draft, 'maxProperties.json'): {
        'maxProperties validation with a decimal': ExclusionReason.bug_max_items_missing,
    },
    (json_schema_test_draft, 'minContains.json'): {
        "minContains=1 with contains": ExclusionReason.bug_with_non_string_const_values,
        "minContains=2 with contains": ExclusionReason.bug_with_non_string_const_values,
        "minContains=2 with contains with a decimal value": ExclusionReason.bug_max_contains_lacks_float_value,
        "maxContains = minContains": ExclusionReason.bug_with_non_string_const_values,
        "maxContains < minContains": ExclusionReason.bug_with_non_string_const_values,
        "minContains = 0": ExclusionReason.bug_with_non_string_const_values,
        "minContains = 0 with maxContains": ExclusionReason.bug_with_non_string_const_values,
    },
    (json_schema_test_draft, 'minItems.json'): {
        'minItems validation with a decimal': ExclusionReason.bug_max_items_missing,
    },
    (json_schema_test_draft, 'minLength.json'): {
        'minLength validation with a decimal': ExclusionReason.bug_max_items_missing,
    },
    (json_schema_test_draft, 'minProperties.json'): {
        'minProperties validation with a decimal': ExclusionReason.bug_max_items_missing,
    },
    (json_schema_test_draft, 'prefixItems.json'): {
        "prefixItems with boolean schemas": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'not.json'): {
        'not with boolean schema true': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'not with boolean schema false': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'not multiple types': ExclusionReason.v303_does_not_support_array_of_types,
        "collect annotations inside a 'not', even if collection is disabled": ExclusionReason.bug_does_not_support_boolean_schemas_in_location
    },
    (json_schema_test_draft, 'oneOf.json'): {
        'oneOf with missing optional property': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'oneOf with boolean schemas, all true': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'oneOf with boolean schemas, one true': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'oneOf with boolean schemas, more than one true': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'oneOf with boolean schemas, all false': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'patternProperties.json'): {
        "patternProperties with boolean schemas": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'properties.json'): {
        'properties with boolean schema': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'propertyNames.json'): {
        "propertyNames with boolean schema true": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "propertyNames with boolean schema false": ExclusionReason.bug_does_not_support_boolean_schemas_in_location
    },
    (json_schema_test_draft, 'ref.json'): {
        'relative refs with absolute uris and defs': ExclusionReason.v303_does_not_support_id,
        '$ref prevents a sibling $id from changing the base uri': ExclusionReason.v303_does_not_support_id,
        'property named $ref, containing an actual $ref': ExclusionReason.bug_does_not_support_definitions,
        'naive replacement of $ref with its destination is not correct': ExclusionReason.bug_does_not_support_definitions,
        'relative pointer ref to array': ExclusionReason.v303_does_not_support_items_schema_array,
        'ref overrides any sibling keywords': ExclusionReason.bug_does_not_support_definitions,
        'Location-independent identifier with base URI change in subschema': ExclusionReason.bug_does_not_support_definitions,
        'escaped pointer ref': ExclusionReason.bug_does_not_support_definitions,
        'Location-independent identifier': ExclusionReason.bug_does_not_support_definitions,
        'refs with relative uris and defs': ExclusionReason.v303_does_not_support_id,
        'Recursive references between schemas': ExclusionReason.bug_does_not_support_definitions,
        'refs with quote': ExclusionReason.bug_does_not_support_definitions,
        'refs with quote': ExclusionReason.bug_does_not_support_definitions,
        '$ref to boolean schema true': ExclusionReason.bug_does_not_support_definitions,
        'Recursive references between schemas': ExclusionReason.v303_does_not_support_id,
        'nested refs': ExclusionReason.bug_does_not_support_definitions,
        '$ref to boolean schema false': ExclusionReason.bug_does_not_support_definitions,
        'remote ref, containing refs itself': ExclusionReason.swagger_parser_exception,
        'relative pointer ref to object': ExclusionReason.ref_location_not_the_same_for_json_and_openapi,
        'root pointer ref': ExclusionReason.ref_location_not_the_same_for_json_and_openapi,
        'ref applies alongside sibling keywords': ExclusionReason.bug_does_not_support_definitions,
        'ref creates new scope when adjacent to keywords': ExclusionReason.bug_does_not_support_definitions,
        "$id must be resolved against nearest parent, not just immediate parent": ExclusionReason.bug_does_not_support_definitions,
        "order of evaluation: $id and $ref": ExclusionReason.bug_does_not_support_definitions,
        "order of evaluation: $id and $anchor and $ref": ExclusionReason.bug_does_not_support_definitions,
        'simple URN base URI with JSON pointer': ExclusionReason.bug_does_not_support_definitions,
        'URN base URI with NSS': ExclusionReason.bug_does_not_support_definitions,
        'URN base URI with r-component': ExclusionReason.bug_does_not_support_definitions,
        'URN base URI with q-component': ExclusionReason.bug_does_not_support_definitions,
        'URN base URI with f-component': ExclusionReason.ref_not_resolved,
        'URN base URI with URN and JSON pointer ref': ExclusionReason.ref_not_resolved,
        'ref to if': ExclusionReason.ref_not_resolved,
        'ref to then': ExclusionReason.ref_not_resolved,
        'ref to else': ExclusionReason.ref_not_resolved,
        "ref with absolute-path-reference": ExclusionReason.ref_not_resolved,
        "$id with file URI still resolves pointers - *nix": ExclusionReason.ref_not_resolved,
        "$id with file URI still resolves pointers - windows": ExclusionReason.ref_not_resolved,
        "empty tokens in $ref json-pointer": ExclusionReason.bug_does_not_support_definitions,
        "simple URN base URI with $ref via the URN": ExclusionReason.ref_not_resolved,
        'URN base URI with URN and anchor ref': ExclusionReason.ref_not_resolved,
        "URN ref with nested pointer ref": ExclusionReason.ref_not_resolved,
    },
    (json_schema_test_draft, 'refRemote.json'): {
        'base URI change - change folder': ExclusionReason.v303_does_not_support_id,
        'base URI change - change folder in subschema': ExclusionReason.bug_does_not_support_definitions,
        'remote ref with ref to definitions': ExclusionReason.v303_does_not_support_id,
        'root ref in remote ref': ExclusionReason.v303_does_not_support_id,
        'base URI change': ExclusionReason.v303_does_not_support_id,
        'remote ref': ExclusionReason.not_running_the_localhost_server,
        'fragment within remote ref': ExclusionReason.not_running_the_localhost_server,
        'ref within remote ref': ExclusionReason.not_running_the_localhost_server,
    },
    (json_schema_test_draft, 'uniqueItems.json'): {
        'uniqueItems with an array of items and additionalItems=false': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        'uniqueItems=false with an array of items and additionalItems=false': ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'unevaluatedItems.json'): {
        "unevaluatedItems true": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems false": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with nested unevaluatedItems": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with anyOf": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with oneOf": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with not": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with boolean schemas": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with $ref": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with items and prefixItems": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with if/then/else": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with tuple": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with uniform items": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems can see annotations from if without then and else": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "non-array instances are valid": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems and contains interact to control item dependency relationship": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems can't see inside cousins": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems depends on adjacent contains": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "item is evaluated in an uncle schema to unevaluatedItems": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with nested tuple": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with nested prefixItems and items": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedItems with nested items": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    },
    (json_schema_test_draft, 'unevaluatedProperties.json'): {
        "cousin unevaluatedProperties, true and false, false with properties": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "nested unevaluatedProperties, outer true, inner false, properties inside": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "non-object instances are valid": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties can't see inside cousins (reverse order)": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties can't see inside cousins": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "nested unevaluatedProperties, outer false, inner true, properties inside": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties can see annotations from if without then and else": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with adjacent patternProperties": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with nested properties": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "in-place applicator siblings, anyOf has unevaluated": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with boolean schemas": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "dynamic evalation inside nested refs": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties false": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with if/then/else, then not defined": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with $ref": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties true": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with if/then/else, else not defined": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties + ref inside allOf / oneOf": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "in-place applicator siblings, allOf has unevaluated": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with dependentSchemas": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "nested unevaluatedProperties, outer false, inner true, properties outside": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties + single cyclic ref": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "nested unevaluatedProperties, outer true, inner false, properties outside": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with anyOf": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with if/then/else": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with adjacent properties": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with nested patternProperties": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with nested unevaluatedProperties": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with not": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
        "unevaluatedProperties with nested additionalProperties": ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    }
}
FILEPATH_TO_EXCLUDE_REASON = {
    (json_schema_test_draft, 'boolean_schema.json'): ExclusionReason.bug_does_not_support_boolean_schemas_in_location,
    (json_schema_test_draft, 'exclusiveMaximum.json'): ExclusionReason.swagger_parser_validation_missing_bug,
    (json_schema_test_draft, 'exclusiveMinimum.json'): ExclusionReason.swagger_parser_validation_missing_bug,
    (json_schema_test_draft, 'id.json'): ExclusionReason.v303_does_not_support_id,
    (json_schema_test_draft, 'refRemote.json'): ExclusionReason.ref_not_resolved,
    (json_schema_test_draft, 'unknownKeyword.json'): ExclusionReason.bug_does_not_support_definitions,
}

JSON_SCHEMA_TEST_FILE_TO_FOLDERS = {
    'additionalProperties.json': (json_schema_test_draft,),
    'allOf.json': (json_schema_test_draft,),
    'anyOf.json': (json_schema_test_draft,),
    'boolean_schema.json': (json_schema_test_draft,),
    'const.json': (json_schema_test_draft,),
    'contains.json': (json_schema_test_draft,),
#     'default.json': (json_schema_test_draft,),
#     'defs.json': (json_schema_test_draft,),
    'dependentRequired.json': (json_schema_test_draft,),
    'dependentSchemas.json': (json_schema_test_draft,),
    'enum.json': (json_schema_test_draft,),
    'exclusiveMaximum.json': (json_schema_test_draft,),
    'exclusiveMinimum.json': (json_schema_test_draft,),
    'format.json': (json_schema_test_draft,),
#     'id.json': (json_schema_test_draft,),
#     'infinite-loop-detection.json': (json_schema_test_draft,),  # activate after fixing this
    'items.json': (json_schema_test_draft,),
    'maxContains.json': (json_schema_test_draft,),
    'maximum.json': (json_schema_test_draft,),
    'maxItems.json': (json_schema_test_draft,),
    'maxLength.json': (json_schema_test_draft,),
    'maxProperties.json': (json_schema_test_draft,),
    'minimum.json': (json_schema_test_draft,),
    'minContains.json': (json_schema_test_draft,),
    'minItems.json': (json_schema_test_draft,),
    'minLength.json': (json_schema_test_draft,),
    'minProperties.json': (json_schema_test_draft,),
    'multipleOf.json': (json_schema_test_draft,),
    'not.json': (json_schema_test_draft,),
    'oneOf.json': (json_schema_test_draft,),
    'pattern.json': (json_schema_test_draft,),
    'patternProperties.json': (json_schema_test_draft,),
    'prefixItems.json': (json_schema_test_draft,),
    'properties.json': (json_schema_test_draft,),
    'propertyNames.json': (json_schema_test_draft,),
    'ref.json': (json_schema_test_draft,),
    'refRemote.json': (json_schema_test_draft,),
    'required.json': (json_schema_test_draft,),
    'type.json': (json_schema_test_draft,),
    'unevaluatedItems.json': (json_schema_test_draft,),
    'unevaluatedProperties.json': (json_schema_test_draft,),
    'uniqueItems.json': (json_schema_test_draft,),
    # 'unknownKeyword.json': (json_schema_test_draft,),
}

file_name_to_tag_name = {
    'ref': '$ref',
    'id': '$id',
    'refRemote': '$ref',
    'unknownKeyword': None
}

def get_json_schema_test_schemas(file_path: typing.Tuple[str]) -> typing.List[JsonSchemaTestSchema]:
    json_schema_test_schemas = []
    filename = file_path[-1]
    exclude_file_reason = FILEPATH_TO_EXCLUDE_REASON.get(file_path)
    if exclude_file_reason:
        print(f'Excluding {file_path} because {exclude_file_reason}')
        return
    excluded_case_to_reason = FILEPATH_TO_EXCLUDED_CASE_AND_REASON.get(file_path, {})
    full_path = path_to_json_schema_drafts + file_path
    path = pathlib.PurePath(*full_path)
    with open(path) as json_file:
        test_schema_dicts = json.load(json_file)
        for test_schema_dict in test_schema_dicts:
            test_schema_dict['tests'] = [JsonSchemaTestCase(**t) for t in test_schema_dict['tests']]
            json_schema_test_schema = JsonSchemaTestSchema(**test_schema_dict)
            test_case_desc = json_schema_test_schema.description
            excluded_reason = excluded_case_to_reason.get(test_case_desc)
            if excluded_reason:
                print(f'Excluding {test_case_desc} because {excluded_reason}')
                continue

            json_schema_test_schemas.append(json_schema_test_schema)

    return json_schema_test_schemas

openapi_version = '3.1.0'

OpenApiSchema = typing.TypedDict(
    'OpenApiSchema',
    {
        'type': str,
        'items': 'OpenApiSchema',
        'properties': typing.Dict[str, 'OpenApiSchema'],
        '$ref': str
    },
    total=False
)

JsonSchemaTestCases = typing.Dict[str, JsonSchemaTestCase]

OpenApiComponents = typing.TypedDict(
    'OpenApiComponents',
    {
        'schemas': typing.Dict[str, OpenApiSchema],
        'x-schema-test-examples': typing.Dict[str, JsonSchemaTestCases]
    }
)

OpenApiMediaType = typing.TypedDict(
    'OpenApiMediaType',
    {
        'schema': OpenApiSchema,
        'x-schema-test-examples': JsonSchemaTestCases
    },
    total=False
)

class OpenApiRequestBody(typing.TypedDict, total=False):
    description: str
    content: typing.Dict[str, OpenApiMediaType]
    required: bool

class OpenApiResponseObject(typing.TypedDict):
    description: str
    headers: typing.Optional[typing.Dict[str, typing.Any]] = None
    content: typing.Optional[typing.Dict[str, OpenApiMediaType]] = None

class OpenApiOperation(typing.TypedDict, total=False):
    tags: typing.List[str]
    summary: str
    description: str
    operationId: str
    requestBody: OpenApiRequestBody
    responses: typing.Dict[str, OpenApiResponseObject]

class OpenApiPathItem(typing.TypedDict, total=False):
    summary: str
    description: str
    get: OpenApiOperation
    put: OpenApiOperation
    post: OpenApiOperation
    delete: OpenApiOperation
    options: OpenApiOperation
    head: OpenApiOperation
    patch: OpenApiOperation
    trace: OpenApiOperation

OpenApiPaths = typing.Dict[str, OpenApiPathItem]


@dataclasses.dataclass
class OpenApiDocumentInfo:
    title: str
    version: str
    description: typing.Optional[str] = None


@dataclasses.dataclass
class OpenApiTag:
    name: str


@dataclasses.dataclass
class OpenApiServer:
    url: str


@dataclasses.dataclass
class OpenApiDocument:
    openapi: str
    servers: typing.List[OpenApiServer]
    info: OpenApiDocumentInfo
    tags: typing.List[OpenApiTag]
    paths: OpenApiPaths
    components: OpenApiComponents


def get_new_openapi() -> OpenApiDocument:
    return OpenApiDocument(
        openapi=openapi_version,
        info=OpenApiDocumentInfo(
            title=f"openapi {openapi_version} sample spec",
            description=f"sample spec for testing openapi functionality, built from json schema tests for {json_schema_test_draft}",
            version="0.0.1"
        ),
        servers=[OpenApiServer(url='https://someserver.com/v1')],
        tags = [],
        paths={},
        components=OpenApiComponents({
            'schemas': {},
            'x-schema-test-examples': {}
        }),
    )

def description_to_component_name(descr: str) -> str:
    res = ''.join(descr.title().split())
    return re.sub(r'[^A-Za-z0-9 ]+', '', res)

def get_test_case_name(test: JsonSchemaTestSchema) -> str:
    res = ''.join(test.description.title().split())
    return re.sub(r'[^A-Za-z0-9 ]+', '', res)

def get_component_schemas_and_test_examples(
    json_schema_test_file: str,
    folders: typing.Tuple[str]
) -> typing.Tuple[typing.Dict[str, OpenApiSchema], typing.Dict[str, typing.Dict[str, JsonSchemaTestSchema]]]:
    component_schemas = {}
    component_name_to_test_examples = {}
    for folder in folders:
        file_path_tuple = (folder, json_schema_test_file)
        test_schemas = get_json_schema_test_schemas(file_path_tuple)
        if not test_schemas:
            continue
        for test_schema in test_schemas:
            component_name = description_to_component_name(test_schema.description)
            json_schema_keyword = json_schema_test_file[:-5]
            if json_schema_keyword == "const" and not component_name.lower().startswith("const"):
                # prefix added to prevent collision with other components
                component_name = "Const" + component_name
            if json_schema_keyword == "dependentSchemas" and not component_name.lower().startswith("dependentschemas"):
                # prefix added to prevent collision with other components
                component_name = "DependentSchemas" + component_name
            if isinstance(test_schema.schema, bool):
                component_schemas[component_name] = test_schema.schema
            else:
                component_schemas[component_name] = OpenApiSchema(**test_schema.schema)
            for test in test_schema.tests:
                if component_name not in component_name_to_test_examples:
                    component_name_to_test_examples[component_name] = {}
                test_case_name = get_test_case_name(test)
                component_name_to_test_examples[component_name][test_case_name] = test
    return component_schemas, component_name_to_test_examples

def generate_post_operation_with_request_body(
    component_name: str,
    tags: typing.List[OpenApiTag]
) -> OpenApiOperation:
    method = 'post'
    ref_schema_path = f'#/components/schemas/{component_name}'
    ref_test_example_path = f'#/components/x-schema-test-examples/{component_name}'
    media_type = OpenApiMediaType(
        {
            'schema': OpenApiSchema({'$ref': ref_schema_path}),
            'x-schema-test-examples': {'$ref': ref_test_example_path}
        }
    )
    request_body = OpenApiRequestBody(
        {
            'content': {'application/json': media_type},
            'required': True
        }
    )
    operationId = f'{method}{component_name}RequestBody'
    response_object = OpenApiResponseObject({'description': 'success'})
    return OpenApiOperation(
        {
            'operationId': operationId,
            'requestBody': request_body,
            'responses': {'200': response_object},
            'tags': [tag.name for tag in tags]
        }
    )


def generate_post_operation_with_response_content_schema(
    component_name: str,
    tags: typing.List[OpenApiTag]
) -> OpenApiOperation:
    method = 'post'
    ref_schema_path = f'#/components/schemas/{component_name}'
    ref_test_example_path = f'#/components/x-schema-test-examples/{component_name}'
    media_type = OpenApiMediaType(
        {
            'schema': OpenApiSchema({'$ref': ref_schema_path}),
            'x-schema-test-examples': {'$ref': ref_test_example_path}
        }
    )
    operationId = f'{method}{component_name}ResponseBodyForContentTypes'
    response_object = OpenApiResponseObject(
        {
            'description': 'success',
            'content': {'application/json': media_type}
        }
    )
    return OpenApiOperation(
        {
            'operationId': operationId,
            'responses': {'200': response_object},
            'tags': [tag.name for tag in tags]
        }
    )


def write_openapi_spec():
    openapi = get_new_openapi()
    request_body_tag = OpenApiTag(name='operation.requestBody')
    post_tag = OpenApiTag(name='path.post')
    json_tag = OpenApiTag(name='contentType_json')
    response_content_tag = OpenApiTag(name='response.content.contentType.schema')
    openapi.tags.extend([request_body_tag, post_tag, json_tag, response_content_tag])
    # write component schemas and tests
    for json_schema_test_file, folders in JSON_SCHEMA_TEST_FILE_TO_FOLDERS.items():
        component_schemas, component_name_to_test_examples = (
            get_component_schemas_and_test_examples(json_schema_test_file, folders)
        )
        if not component_schemas and not component_name_to_test_examples:
            continue
        json_schema_test_file_name = json_schema_test_file.split('.')[0]
        json_schema_tag_name = file_name_to_tag_name.get(json_schema_test_file_name, json_schema_test_file_name)
        json_schema_tag = None
        if json_schema_tag_name is not None:
            json_schema_tag = OpenApiTag(name=json_schema_tag_name)
            openapi.tags.append(json_schema_tag)
        for component_name, schema in component_schemas.items():
            if component_name in openapi.components['schemas']:
                raise ValueError(f'A component schema with name={component_name} is already defined!')
            openapi.components['schemas'][component_name] = schema
        for component_name, test_examples in component_name_to_test_examples.items():
            if component_name in openapi.components['x-schema-test-examples']:
                raise ValueError('A component schema test example map with that name is already defined!')
            openapi.components['x-schema-test-examples'][component_name] = test_examples

            request_body_tag_list = [request_body_tag, post_tag, json_tag]
            if json_schema_tag is not None:
                request_body_tag_list.append(json_schema_tag)

            operation = generate_post_operation_with_request_body(component_name, request_body_tag_list)
            path_item = OpenApiPathItem(post=operation)
            openapi.paths[f'/requestBody/{operation["operationId"]}'] = path_item

            # todo add put and patch with paths requestBody/someIdentifier

            response_body_tag_list = [response_content_tag, post_tag, json_tag]
            if json_schema_tag is not None:
                response_body_tag_list.append(json_schema_tag)
            operation = generate_post_operation_with_response_content_schema(component_name, response_body_tag_list)
            path_item = OpenApiPathItem(post=operation)
            openapi.paths[f'/responseBody/{operation["operationId"]}'] = path_item
#     print(
#         yaml.dump(
#             dataclasses.asdict(openapi),
#             sort_keys=False
#         )
#     )
    spec_out = '3_1_0_unit_test_spec.yaml'
    with open(spec_out, 'w') as yaml_out:
        yaml_out.write(
            yaml.dump(
                dataclasses.asdict(openapi),
                sort_keys=False
            )
        )
    print(f'spec written to {spec_out}')


write_openapi_spec()