# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from unit_test_api.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    REQUEST_BODY_POST_ADDITIONALPROPERTIES_ALLOWS_ASCHEMA_WHICH_SHOULD_VALIDATE_REQUEST_BODY = "/requestBody/postAdditionalpropertiesAllowsASchemaWhichShouldValidateRequestBody"
    RESPONSE_BODY_POST_ADDITIONALPROPERTIES_ALLOWS_ASCHEMA_WHICH_SHOULD_VALIDATE_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAdditionalpropertiesAllowsASchemaWhichShouldValidateResponseBodyForContentTypes"
    REQUEST_BODY_POST_ADDITIONALPROPERTIES_CAN_EXIST_BY_ITSELF_REQUEST_BODY = "/requestBody/postAdditionalpropertiesCanExistByItselfRequestBody"
    RESPONSE_BODY_POST_ADDITIONALPROPERTIES_CAN_EXIST_BY_ITSELF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAdditionalpropertiesCanExistByItselfResponseBodyForContentTypes"
    REQUEST_BODY_POST_ADDITIONALPROPERTIES_ARE_ALLOWED_BY_DEFAULT_REQUEST_BODY = "/requestBody/postAdditionalpropertiesAreAllowedByDefaultRequestBody"
    RESPONSE_BODY_POST_ADDITIONALPROPERTIES_ARE_ALLOWED_BY_DEFAULT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAdditionalpropertiesAreAllowedByDefaultResponseBodyForContentTypes"
    REQUEST_BODY_POST_ADDITIONALPROPERTIES_SHOULD_NOT_LOOK_IN_APPLICATORS_REQUEST_BODY = "/requestBody/postAdditionalpropertiesShouldNotLookInApplicatorsRequestBody"
    RESPONSE_BODY_POST_ADDITIONALPROPERTIES_SHOULD_NOT_LOOK_IN_APPLICATORS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAdditionalpropertiesShouldNotLookInApplicatorsResponseBodyForContentTypes"
    REQUEST_BODY_POST_ALLOF_REQUEST_BODY = "/requestBody/postAllofRequestBody"
    RESPONSE_BODY_POST_ALLOF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAllofResponseBodyForContentTypes"
    REQUEST_BODY_POST_ALLOF_WITH_BASE_SCHEMA_REQUEST_BODY = "/requestBody/postAllofWithBaseSchemaRequestBody"
    RESPONSE_BODY_POST_ALLOF_WITH_BASE_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAllofWithBaseSchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_ALLOF_SIMPLE_TYPES_REQUEST_BODY = "/requestBody/postAllofSimpleTypesRequestBody"
    RESPONSE_BODY_POST_ALLOF_SIMPLE_TYPES_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAllofSimpleTypesResponseBodyForContentTypes"
    REQUEST_BODY_POST_ALLOF_WITH_ONE_EMPTY_SCHEMA_REQUEST_BODY = "/requestBody/postAllofWithOneEmptySchemaRequestBody"
    RESPONSE_BODY_POST_ALLOF_WITH_ONE_EMPTY_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAllofWithOneEmptySchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_ALLOF_WITH_TWO_EMPTY_SCHEMAS_REQUEST_BODY = "/requestBody/postAllofWithTwoEmptySchemasRequestBody"
    RESPONSE_BODY_POST_ALLOF_WITH_TWO_EMPTY_SCHEMAS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAllofWithTwoEmptySchemasResponseBodyForContentTypes"
    REQUEST_BODY_POST_ALLOF_WITH_THE_FIRST_EMPTY_SCHEMA_REQUEST_BODY = "/requestBody/postAllofWithTheFirstEmptySchemaRequestBody"
    RESPONSE_BODY_POST_ALLOF_WITH_THE_FIRST_EMPTY_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAllofWithTheFirstEmptySchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_ALLOF_WITH_THE_LAST_EMPTY_SCHEMA_REQUEST_BODY = "/requestBody/postAllofWithTheLastEmptySchemaRequestBody"
    RESPONSE_BODY_POST_ALLOF_WITH_THE_LAST_EMPTY_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAllofWithTheLastEmptySchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_NESTED_ALLOF_TO_CHECK_VALIDATION_SEMANTICS_REQUEST_BODY = "/requestBody/postNestedAllofToCheckValidationSemanticsRequestBody"
    RESPONSE_BODY_POST_NESTED_ALLOF_TO_CHECK_VALIDATION_SEMANTICS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNestedAllofToCheckValidationSemanticsResponseBodyForContentTypes"
    REQUEST_BODY_POST_ALLOF_COMBINED_WITH_ANYOF_ONEOF_REQUEST_BODY = "/requestBody/postAllofCombinedWithAnyofOneofRequestBody"
    RESPONSE_BODY_POST_ALLOF_COMBINED_WITH_ANYOF_ONEOF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAllofCombinedWithAnyofOneofResponseBodyForContentTypes"
    REQUEST_BODY_POST_ANYOF_REQUEST_BODY = "/requestBody/postAnyofRequestBody"
    RESPONSE_BODY_POST_ANYOF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAnyofResponseBodyForContentTypes"
    REQUEST_BODY_POST_ANYOF_WITH_BASE_SCHEMA_REQUEST_BODY = "/requestBody/postAnyofWithBaseSchemaRequestBody"
    RESPONSE_BODY_POST_ANYOF_WITH_BASE_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAnyofWithBaseSchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_ANYOF_COMPLEX_TYPES_REQUEST_BODY = "/requestBody/postAnyofComplexTypesRequestBody"
    RESPONSE_BODY_POST_ANYOF_COMPLEX_TYPES_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAnyofComplexTypesResponseBodyForContentTypes"
    REQUEST_BODY_POST_ANYOF_WITH_ONE_EMPTY_SCHEMA_REQUEST_BODY = "/requestBody/postAnyofWithOneEmptySchemaRequestBody"
    RESPONSE_BODY_POST_ANYOF_WITH_ONE_EMPTY_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postAnyofWithOneEmptySchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_NESTED_ANYOF_TO_CHECK_VALIDATION_SEMANTICS_REQUEST_BODY = "/requestBody/postNestedAnyofToCheckValidationSemanticsRequestBody"
    RESPONSE_BODY_POST_NESTED_ANYOF_TO_CHECK_VALIDATION_SEMANTICS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNestedAnyofToCheckValidationSemanticsResponseBodyForContentTypes"
    REQUEST_BODY_POST_INVALID_STRING_VALUE_FOR_DEFAULT_REQUEST_BODY = "/requestBody/postInvalidStringValueForDefaultRequestBody"
    RESPONSE_BODY_POST_INVALID_STRING_VALUE_FOR_DEFAULT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postInvalidStringValueForDefaultResponseBodyForContentTypes"
    REQUEST_BODY_POST_THE_DEFAULT_KEYWORD_DOES_NOT_DO_ANYTHING_IF_THE_PROPERTY_IS_MISSING_REQUEST_BODY = "/requestBody/postTheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingRequestBody"
    RESPONSE_BODY_POST_THE_DEFAULT_KEYWORD_DOES_NOT_DO_ANYTHING_IF_THE_PROPERTY_IS_MISSING_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postTheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingResponseBodyForContentTypes"
    REQUEST_BODY_POST_SIMPLE_ENUM_VALIDATION_REQUEST_BODY = "/requestBody/postSimpleEnumValidationRequestBody"
    RESPONSE_BODY_POST_SIMPLE_ENUM_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postSimpleEnumValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_ENUMS_IN_PROPERTIES_REQUEST_BODY = "/requestBody/postEnumsInPropertiesRequestBody"
    RESPONSE_BODY_POST_ENUMS_IN_PROPERTIES_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postEnumsInPropertiesResponseBodyForContentTypes"
    REQUEST_BODY_POST_ENUM_WITH_ESCAPED_CHARACTERS_REQUEST_BODY = "/requestBody/postEnumWithEscapedCharactersRequestBody"
    RESPONSE_BODY_POST_ENUM_WITH_ESCAPED_CHARACTERS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postEnumWithEscapedCharactersResponseBodyForContentTypes"
    REQUEST_BODY_POST_ENUM_WITH_FALSE_DOES_NOT_MATCH0REQUEST_BODY = "/requestBody/postEnumWithFalseDoesNotMatch0RequestBody"
    RESPONSE_BODY_POST_ENUM_WITH_FALSE_DOES_NOT_MATCH0RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postEnumWithFalseDoesNotMatch0ResponseBodyForContentTypes"
    REQUEST_BODY_POST_ENUM_WITH_TRUE_DOES_NOT_MATCH1REQUEST_BODY = "/requestBody/postEnumWithTrueDoesNotMatch1RequestBody"
    RESPONSE_BODY_POST_ENUM_WITH_TRUE_DOES_NOT_MATCH1RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postEnumWithTrueDoesNotMatch1ResponseBodyForContentTypes"
    REQUEST_BODY_POST_ENUM_WITH0DOES_NOT_MATCH_FALSE_REQUEST_BODY = "/requestBody/postEnumWith0DoesNotMatchFalseRequestBody"
    RESPONSE_BODY_POST_ENUM_WITH0DOES_NOT_MATCH_FALSE_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postEnumWith0DoesNotMatchFalseResponseBodyForContentTypes"
    REQUEST_BODY_POST_ENUM_WITH1DOES_NOT_MATCH_TRUE_REQUEST_BODY = "/requestBody/postEnumWith1DoesNotMatchTrueRequestBody"
    RESPONSE_BODY_POST_ENUM_WITH1DOES_NOT_MATCH_TRUE_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postEnumWith1DoesNotMatchTrueResponseBodyForContentTypes"
    REQUEST_BODY_POST_NUL_CHARACTERS_IN_STRINGS_REQUEST_BODY = "/requestBody/postNulCharactersInStringsRequestBody"
    RESPONSE_BODY_POST_NUL_CHARACTERS_IN_STRINGS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNulCharactersInStringsResponseBodyForContentTypes"
    REQUEST_BODY_POST_EMAIL_FORMAT_REQUEST_BODY = "/requestBody/postEmailFormatRequestBody"
    RESPONSE_BODY_POST_EMAIL_FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postEmailFormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_IPV4FORMAT_REQUEST_BODY = "/requestBody/postIpv4FormatRequestBody"
    RESPONSE_BODY_POST_IPV4FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postIpv4FormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_IPV6FORMAT_REQUEST_BODY = "/requestBody/postIpv6FormatRequestBody"
    RESPONSE_BODY_POST_IPV6FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postIpv6FormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_HOSTNAME_FORMAT_REQUEST_BODY = "/requestBody/postHostnameFormatRequestBody"
    RESPONSE_BODY_POST_HOSTNAME_FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postHostnameFormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_DATE_TIME_FORMAT_REQUEST_BODY = "/requestBody/postDateTimeFormatRequestBody"
    RESPONSE_BODY_POST_DATE_TIME_FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postDateTimeFormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_JSON_POINTER_FORMAT_REQUEST_BODY = "/requestBody/postJsonPointerFormatRequestBody"
    RESPONSE_BODY_POST_JSON_POINTER_FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postJsonPointerFormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_URI_FORMAT_REQUEST_BODY = "/requestBody/postUriFormatRequestBody"
    RESPONSE_BODY_POST_URI_FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postUriFormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_URI_REFERENCE_FORMAT_REQUEST_BODY = "/requestBody/postUriReferenceFormatRequestBody"
    RESPONSE_BODY_POST_URI_REFERENCE_FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postUriReferenceFormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_URI_TEMPLATE_FORMAT_REQUEST_BODY = "/requestBody/postUriTemplateFormatRequestBody"
    RESPONSE_BODY_POST_URI_TEMPLATE_FORMAT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postUriTemplateFormatResponseBodyForContentTypes"
    REQUEST_BODY_POST_NESTED_ITEMS_REQUEST_BODY = "/requestBody/postNestedItemsRequestBody"
    RESPONSE_BODY_POST_NESTED_ITEMS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNestedItemsResponseBodyForContentTypes"
    REQUEST_BODY_POST_MAXIMUM_VALIDATION_REQUEST_BODY = "/requestBody/postMaximumValidationRequestBody"
    RESPONSE_BODY_POST_MAXIMUM_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMaximumValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_MAXIMUM_VALIDATION_WITH_UNSIGNED_INTEGER_REQUEST_BODY = "/requestBody/postMaximumValidationWithUnsignedIntegerRequestBody"
    RESPONSE_BODY_POST_MAXIMUM_VALIDATION_WITH_UNSIGNED_INTEGER_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMaximumValidationWithUnsignedIntegerResponseBodyForContentTypes"
    REQUEST_BODY_POST_MAXITEMS_VALIDATION_REQUEST_BODY = "/requestBody/postMaxitemsValidationRequestBody"
    RESPONSE_BODY_POST_MAXITEMS_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMaxitemsValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_MAXLENGTH_VALIDATION_REQUEST_BODY = "/requestBody/postMaxlengthValidationRequestBody"
    RESPONSE_BODY_POST_MAXLENGTH_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMaxlengthValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_MAXPROPERTIES_VALIDATION_REQUEST_BODY = "/requestBody/postMaxpropertiesValidationRequestBody"
    RESPONSE_BODY_POST_MAXPROPERTIES_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMaxpropertiesValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_MAXPROPERTIES0MEANS_THE_OBJECT_IS_EMPTY_REQUEST_BODY = "/requestBody/postMaxproperties0MeansTheObjectIsEmptyRequestBody"
    RESPONSE_BODY_POST_MAXPROPERTIES0MEANS_THE_OBJECT_IS_EMPTY_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMaxproperties0MeansTheObjectIsEmptyResponseBodyForContentTypes"
    REQUEST_BODY_POST_MINIMUM_VALIDATION_REQUEST_BODY = "/requestBody/postMinimumValidationRequestBody"
    RESPONSE_BODY_POST_MINIMUM_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMinimumValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_MINIMUM_VALIDATION_WITH_SIGNED_INTEGER_REQUEST_BODY = "/requestBody/postMinimumValidationWithSignedIntegerRequestBody"
    RESPONSE_BODY_POST_MINIMUM_VALIDATION_WITH_SIGNED_INTEGER_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMinimumValidationWithSignedIntegerResponseBodyForContentTypes"
    REQUEST_BODY_POST_MINITEMS_VALIDATION_REQUEST_BODY = "/requestBody/postMinitemsValidationRequestBody"
    RESPONSE_BODY_POST_MINITEMS_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMinitemsValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_MINLENGTH_VALIDATION_REQUEST_BODY = "/requestBody/postMinlengthValidationRequestBody"
    RESPONSE_BODY_POST_MINLENGTH_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMinlengthValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_MINPROPERTIES_VALIDATION_REQUEST_BODY = "/requestBody/postMinpropertiesValidationRequestBody"
    RESPONSE_BODY_POST_MINPROPERTIES_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postMinpropertiesValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_BY_INT_REQUEST_BODY = "/requestBody/postByIntRequestBody"
    RESPONSE_BODY_POST_BY_INT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postByIntResponseBodyForContentTypes"
    REQUEST_BODY_POST_BY_NUMBER_REQUEST_BODY = "/requestBody/postByNumberRequestBody"
    RESPONSE_BODY_POST_BY_NUMBER_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postByNumberResponseBodyForContentTypes"
    REQUEST_BODY_POST_BY_SMALL_NUMBER_REQUEST_BODY = "/requestBody/postBySmallNumberRequestBody"
    RESPONSE_BODY_POST_BY_SMALL_NUMBER_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postBySmallNumberResponseBodyForContentTypes"
    REQUEST_BODY_POST_INVALID_INSTANCE_SHOULD_NOT_RAISE_ERROR_WHEN_FLOAT_DIVISION_INF_REQUEST_BODY = "/requestBody/postInvalidInstanceShouldNotRaiseErrorWhenFloatDivisionInfRequestBody"
    RESPONSE_BODY_POST_INVALID_INSTANCE_SHOULD_NOT_RAISE_ERROR_WHEN_FLOAT_DIVISION_INF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postInvalidInstanceShouldNotRaiseErrorWhenFloatDivisionInfResponseBodyForContentTypes"
    REQUEST_BODY_POST_NOT_REQUEST_BODY = "/requestBody/postNotRequestBody"
    RESPONSE_BODY_POST_NOT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNotResponseBodyForContentTypes"
    REQUEST_BODY_POST_NOT_MORE_COMPLEX_SCHEMA_REQUEST_BODY = "/requestBody/postNotMoreComplexSchemaRequestBody"
    RESPONSE_BODY_POST_NOT_MORE_COMPLEX_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNotMoreComplexSchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_FORBIDDEN_PROPERTY_REQUEST_BODY = "/requestBody/postForbiddenPropertyRequestBody"
    RESPONSE_BODY_POST_FORBIDDEN_PROPERTY_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postForbiddenPropertyResponseBodyForContentTypes"
    REQUEST_BODY_POST_ONEOF_REQUEST_BODY = "/requestBody/postOneofRequestBody"
    RESPONSE_BODY_POST_ONEOF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postOneofResponseBodyForContentTypes"
    REQUEST_BODY_POST_ONEOF_WITH_BASE_SCHEMA_REQUEST_BODY = "/requestBody/postOneofWithBaseSchemaRequestBody"
    RESPONSE_BODY_POST_ONEOF_WITH_BASE_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postOneofWithBaseSchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_ONEOF_COMPLEX_TYPES_REQUEST_BODY = "/requestBody/postOneofComplexTypesRequestBody"
    RESPONSE_BODY_POST_ONEOF_COMPLEX_TYPES_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postOneofComplexTypesResponseBodyForContentTypes"
    REQUEST_BODY_POST_ONEOF_WITH_EMPTY_SCHEMA_REQUEST_BODY = "/requestBody/postOneofWithEmptySchemaRequestBody"
    RESPONSE_BODY_POST_ONEOF_WITH_EMPTY_SCHEMA_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postOneofWithEmptySchemaResponseBodyForContentTypes"
    REQUEST_BODY_POST_ONEOF_WITH_REQUIRED_REQUEST_BODY = "/requestBody/postOneofWithRequiredRequestBody"
    RESPONSE_BODY_POST_ONEOF_WITH_REQUIRED_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postOneofWithRequiredResponseBodyForContentTypes"
    REQUEST_BODY_POST_NESTED_ONEOF_TO_CHECK_VALIDATION_SEMANTICS_REQUEST_BODY = "/requestBody/postNestedOneofToCheckValidationSemanticsRequestBody"
    RESPONSE_BODY_POST_NESTED_ONEOF_TO_CHECK_VALIDATION_SEMANTICS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNestedOneofToCheckValidationSemanticsResponseBodyForContentTypes"
    REQUEST_BODY_POST_PATTERN_VALIDATION_REQUEST_BODY = "/requestBody/postPatternValidationRequestBody"
    RESPONSE_BODY_POST_PATTERN_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postPatternValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_PATTERN_IS_NOT_ANCHORED_REQUEST_BODY = "/requestBody/postPatternIsNotAnchoredRequestBody"
    RESPONSE_BODY_POST_PATTERN_IS_NOT_ANCHORED_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postPatternIsNotAnchoredResponseBodyForContentTypes"
    REQUEST_BODY_POST_OBJECT_PROPERTIES_VALIDATION_REQUEST_BODY = "/requestBody/postObjectPropertiesValidationRequestBody"
    RESPONSE_BODY_POST_OBJECT_PROPERTIES_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postObjectPropertiesValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_PROPERTIES_WITH_ESCAPED_CHARACTERS_REQUEST_BODY = "/requestBody/postPropertiesWithEscapedCharactersRequestBody"
    RESPONSE_BODY_POST_PROPERTIES_WITH_ESCAPED_CHARACTERS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postPropertiesWithEscapedCharactersResponseBodyForContentTypes"
    REQUEST_BODY_POST_PROPERTY_NAMED_REF_THAT_IS_NOT_AREFERENCE_REQUEST_BODY = "/requestBody/postPropertyNamedRefThatIsNotAReferenceRequestBody"
    RESPONSE_BODY_POST_PROPERTY_NAMED_REF_THAT_IS_NOT_AREFERENCE_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postPropertyNamedRefThatIsNotAReferenceResponseBodyForContentTypes"
    REQUEST_BODY_POST_REF_IN_ADDITIONALPROPERTIES_REQUEST_BODY = "/requestBody/postRefInAdditionalpropertiesRequestBody"
    RESPONSE_BODY_POST_REF_IN_ADDITIONALPROPERTIES_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRefInAdditionalpropertiesResponseBodyForContentTypes"
    REQUEST_BODY_POST_REF_IN_ITEMS_REQUEST_BODY = "/requestBody/postRefInItemsRequestBody"
    RESPONSE_BODY_POST_REF_IN_ITEMS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRefInItemsResponseBodyForContentTypes"
    REQUEST_BODY_POST_REF_IN_PROPERTY_REQUEST_BODY = "/requestBody/postRefInPropertyRequestBody"
    RESPONSE_BODY_POST_REF_IN_PROPERTY_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRefInPropertyResponseBodyForContentTypes"
    REQUEST_BODY_POST_REF_IN_ALLOF_REQUEST_BODY = "/requestBody/postRefInAllofRequestBody"
    RESPONSE_BODY_POST_REF_IN_ALLOF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRefInAllofResponseBodyForContentTypes"
    REQUEST_BODY_POST_REF_IN_ONEOF_REQUEST_BODY = "/requestBody/postRefInOneofRequestBody"
    RESPONSE_BODY_POST_REF_IN_ONEOF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRefInOneofResponseBodyForContentTypes"
    REQUEST_BODY_POST_REF_IN_ANYOF_REQUEST_BODY = "/requestBody/postRefInAnyofRequestBody"
    RESPONSE_BODY_POST_REF_IN_ANYOF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRefInAnyofResponseBodyForContentTypes"
    REQUEST_BODY_POST_REF_IN_NOT_REQUEST_BODY = "/requestBody/postRefInNotRequestBody"
    RESPONSE_BODY_POST_REF_IN_NOT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRefInNotResponseBodyForContentTypes"
    REQUEST_BODY_POST_ROOT_POINTER_REF_REQUEST_BODY = "/requestBody/postRootPointerRefRequestBody"
    RESPONSE_BODY_POST_ROOT_POINTER_REF_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRootPointerRefResponseBodyForContentTypes"
    REQUEST_BODY_POST_REQUIRED_VALIDATION_REQUEST_BODY = "/requestBody/postRequiredValidationRequestBody"
    RESPONSE_BODY_POST_REQUIRED_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRequiredValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_REQUIRED_DEFAULT_VALIDATION_REQUEST_BODY = "/requestBody/postRequiredDefaultValidationRequestBody"
    RESPONSE_BODY_POST_REQUIRED_DEFAULT_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRequiredDefaultValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_REQUIRED_WITH_EMPTY_ARRAY_REQUEST_BODY = "/requestBody/postRequiredWithEmptyArrayRequestBody"
    RESPONSE_BODY_POST_REQUIRED_WITH_EMPTY_ARRAY_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRequiredWithEmptyArrayResponseBodyForContentTypes"
    REQUEST_BODY_POST_REQUIRED_WITH_ESCAPED_CHARACTERS_REQUEST_BODY = "/requestBody/postRequiredWithEscapedCharactersRequestBody"
    RESPONSE_BODY_POST_REQUIRED_WITH_ESCAPED_CHARACTERS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postRequiredWithEscapedCharactersResponseBodyForContentTypes"
    REQUEST_BODY_POST_INTEGER_TYPE_MATCHES_INTEGERS_REQUEST_BODY = "/requestBody/postIntegerTypeMatchesIntegersRequestBody"
    RESPONSE_BODY_POST_INTEGER_TYPE_MATCHES_INTEGERS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes"
    REQUEST_BODY_POST_NUMBER_TYPE_MATCHES_NUMBERS_REQUEST_BODY = "/requestBody/postNumberTypeMatchesNumbersRequestBody"
    RESPONSE_BODY_POST_NUMBER_TYPE_MATCHES_NUMBERS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNumberTypeMatchesNumbersResponseBodyForContentTypes"
    REQUEST_BODY_POST_STRING_TYPE_MATCHES_STRINGS_REQUEST_BODY = "/requestBody/postStringTypeMatchesStringsRequestBody"
    RESPONSE_BODY_POST_STRING_TYPE_MATCHES_STRINGS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postStringTypeMatchesStringsResponseBodyForContentTypes"
    REQUEST_BODY_POST_OBJECT_TYPE_MATCHES_OBJECTS_REQUEST_BODY = "/requestBody/postObjectTypeMatchesObjectsRequestBody"
    RESPONSE_BODY_POST_OBJECT_TYPE_MATCHES_OBJECTS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postObjectTypeMatchesObjectsResponseBodyForContentTypes"
    REQUEST_BODY_POST_BOOLEAN_TYPE_MATCHES_BOOLEANS_REQUEST_BODY = "/requestBody/postBooleanTypeMatchesBooleansRequestBody"
    RESPONSE_BODY_POST_BOOLEAN_TYPE_MATCHES_BOOLEANS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postBooleanTypeMatchesBooleansResponseBodyForContentTypes"
    REQUEST_BODY_POST_NULL_TYPE_MATCHES_ONLY_THE_NULL_OBJECT_REQUEST_BODY = "/requestBody/postNullTypeMatchesOnlyTheNullObjectRequestBody"
    RESPONSE_BODY_POST_NULL_TYPE_MATCHES_ONLY_THE_NULL_OBJECT_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postNullTypeMatchesOnlyTheNullObjectResponseBodyForContentTypes"
    REQUEST_BODY_POST_ARRAY_TYPE_MATCHES_ARRAYS_REQUEST_BODY = "/requestBody/postArrayTypeMatchesArraysRequestBody"
    RESPONSE_BODY_POST_ARRAY_TYPE_MATCHES_ARRAYS_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postArrayTypeMatchesArraysResponseBodyForContentTypes"
    REQUEST_BODY_POST_UNIQUEITEMS_VALIDATION_REQUEST_BODY = "/requestBody/postUniqueitemsValidationRequestBody"
    RESPONSE_BODY_POST_UNIQUEITEMS_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postUniqueitemsValidationResponseBodyForContentTypes"
    REQUEST_BODY_POST_UNIQUEITEMS_FALSE_VALIDATION_REQUEST_BODY = "/requestBody/postUniqueitemsFalseValidationRequestBody"
    RESPONSE_BODY_POST_UNIQUEITEMS_FALSE_VALIDATION_RESPONSE_BODY_FOR_CONTENT_TYPES = "/responseBody/postUniqueitemsFalseValidationResponseBodyForContentTypes"
