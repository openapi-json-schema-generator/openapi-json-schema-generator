# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from unit_test_api.components.schema.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from unit_test_api.components.schema.additionalproperties_are_allowed_by_default import AdditionalpropertiesAreAllowedByDefault
from unit_test_api.components.schema.additionalproperties_can_exist_by_itself import AdditionalpropertiesCanExistByItself
from unit_test_api.components.schema.additionalproperties_does_not_look_in_applicators import AdditionalpropertiesDoesNotLookInApplicators
from unit_test_api.components.schema.additionalproperties_with_null_valued_instance_properties import AdditionalpropertiesWithNullValuedInstanceProperties
from unit_test_api.components.schema.additionalproperties_with_schema import AdditionalpropertiesWithSchema
from unit_test_api.components.schema.allof import Allof
from unit_test_api.components.schema.allof_combined_with_anyof_oneof import AllofCombinedWithAnyofOneof
from unit_test_api.components.schema.allof_simple_types import AllofSimpleTypes
from unit_test_api.components.schema.allof_with_base_schema import AllofWithBaseSchema
from unit_test_api.components.schema.allof_with_one_empty_schema import AllofWithOneEmptySchema
from unit_test_api.components.schema.allof_with_the_first_empty_schema import AllofWithTheFirstEmptySchema
from unit_test_api.components.schema.allof_with_the_last_empty_schema import AllofWithTheLastEmptySchema
from unit_test_api.components.schema.allof_with_two_empty_schemas import AllofWithTwoEmptySchemas
from unit_test_api.components.schema.anyof import Anyof
from unit_test_api.components.schema.anyof_complex_types import AnyofComplexTypes
from unit_test_api.components.schema.anyof_with_base_schema import AnyofWithBaseSchema
from unit_test_api.components.schema.anyof_with_one_empty_schema import AnyofWithOneEmptySchema
from unit_test_api.components.schema.date_format import DateFormat
from unit_test_api.components.schema.date_time_format import DateTimeFormat
from unit_test_api.components.schema.duration_format import DurationFormat
from unit_test_api.components.schema.email_format import EmailFormat
from unit_test_api.components.schema.enum_with0_does_not_match_false import EnumWith0DoesNotMatchFalse
from unit_test_api.components.schema.enum_with1_does_not_match_true import EnumWith1DoesNotMatchTrue
from unit_test_api.components.schema.enum_with_escaped_characters import EnumWithEscapedCharacters
from unit_test_api.components.schema.enum_with_false_does_not_match0 import EnumWithFalseDoesNotMatch0
from unit_test_api.components.schema.enum_with_true_does_not_match1 import EnumWithTrueDoesNotMatch1
from unit_test_api.components.schema.enums_in_properties import EnumsInProperties
from unit_test_api.components.schema.hostname_format import HostnameFormat
from unit_test_api.components.schema.idn_email_format import IdnEmailFormat
from unit_test_api.components.schema.idn_hostname_format import IdnHostnameFormat
from unit_test_api.components.schema.ipv4_format import Ipv4Format
from unit_test_api.components.schema.ipv6_format import Ipv6Format
from unit_test_api.components.schema.iri_format import IriFormat
from unit_test_api.components.schema.iri_reference_format import IriReferenceFormat
from unit_test_api.components.schema.items_does_not_look_in_applicators_valid_case import ItemsDoesNotLookInApplicatorsValidCase
from unit_test_api.components.schema.items_with_null_instance_elements import ItemsWithNullInstanceElements
from unit_test_api.components.schema.json_pointer_format import JsonPointerFormat
from unit_test_api.components.schema.maximum_validation import MaximumValidation
from unit_test_api.components.schema.maximum_validation_with_unsigned_integer import MaximumValidationWithUnsignedInteger
from unit_test_api.components.schema.maxitems_validation import MaxitemsValidation
from unit_test_api.components.schema.maxitems_validation_with_a_decimal import MaxitemsValidationWithADecimal
from unit_test_api.components.schema.maxlength_validation import MaxlengthValidation
from unit_test_api.components.schema.maxlength_validation_with_a_decimal import MaxlengthValidationWithADecimal
from unit_test_api.components.schema.maxproperties0_means_the_object_is_empty import Maxproperties0MeansTheObjectIsEmpty
from unit_test_api.components.schema.maxproperties_validation import MaxpropertiesValidation
from unit_test_api.components.schema.maxproperties_validation_with_a_decimal import MaxpropertiesValidationWithADecimal
from unit_test_api.components.schema.nested_allof_to_check_validation_semantics import NestedAllofToCheckValidationSemantics
from unit_test_api.components.schema.nested_anyof_to_check_validation_semantics import NestedAnyofToCheckValidationSemantics
from unit_test_api.components.schema.nested_items import NestedItems
from unit_test_api.components.schema.nested_oneof_to_check_validation_semantics import NestedOneofToCheckValidationSemantics
from unit_test_api.components.schema.nul_characters_in_strings import NulCharactersInStrings
from unit_test_api.components.schema.oneof import Oneof
from unit_test_api.components.schema.oneof_complex_types import OneofComplexTypes
from unit_test_api.components.schema.oneof_with_base_schema import OneofWithBaseSchema
from unit_test_api.components.schema.oneof_with_empty_schema import OneofWithEmptySchema
from unit_test_api.components.schema.oneof_with_required import OneofWithRequired
from unit_test_api.components.schema.prefixitems_validation_adjusts_the_starting_index_for_items import PrefixitemsValidationAdjustsTheStartingIndexForItems
from unit_test_api.components.schema.regex_format import RegexFormat
from unit_test_api.components.schema.relative_json_pointer_format import RelativeJsonPointerFormat
from unit_test_api.components.schema.simple_enum_validation import SimpleEnumValidation
from unit_test_api.components.schema.time_format import TimeFormat
from unit_test_api.components.schema.uri_format import UriFormat
from unit_test_api.components.schema.uri_reference_format import UriReferenceFormat
from unit_test_api.components.schema.uri_template_format import UriTemplateFormat
from unit_test_api.components.schema.uuid_format import UuidFormat
