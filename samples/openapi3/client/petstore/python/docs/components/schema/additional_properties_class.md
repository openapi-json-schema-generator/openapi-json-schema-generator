petstore_api.components.schema.additional_properties_class
# Schema AdditionalPropertiesClass

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**map_property** | dict, frozendict.frozendict | [properties.MapProperty](#properties-mapproperty) |  | [optional]
**map_of_map_property** | dict, frozendict.frozendict | [properties.MapOfMapProperty](#properties-mapofmapproperty) |  | [optional]
**anytype_1** | dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, io.FileIO |  | [optional]
**map_with_undeclared_properties_anytype_1** | dict, frozendict.frozendict | [properties.MapWithUndeclaredPropertiesAnytype1](#properties-mapwithundeclaredpropertiesanytype1) |  | [optional]
**map_with_undeclared_properties_anytype_2** | dict, frozendict.frozendict | [properties.MapWithUndeclaredPropertiesAnytype2](#properties-mapwithundeclaredpropertiesanytype2) |  | [optional]
**map_with_undeclared_properties_anytype_3** | dict, frozendict.frozendict | [properties.MapWithUndeclaredPropertiesAnytype3](#properties-mapwithundeclaredpropertiesanytype3) |  | [optional]
**empty_map** | dict, frozendict.frozendict | [properties.EmptyMap](#properties-emptymap) | an object with no declared properties and no undeclared properties, hence it&#x27;s an empty map. | [optional]
**map_with_undeclared_properties_string** | dict, frozendict.frozendict | [properties.MapWithUndeclaredPropertiesString](#properties-mapwithundeclaredpropertiesstring) |  | [optional]
**any_string_name** | dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema | frozendict.frozendict, tuple, decimal.Decimal, str, bytes, BoolClass, NoneClass, FileIO | any string name can be used but the value must be the correct type | [optional]

# properties MapProperty

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str | str | any string name can be used but the value must be the correct type | [optional]

# properties MapOfMapProperty

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict | [AdditionalProperties](#properties-mapofmapproperty-additionalproperties) | any string name can be used but the value must be the correct type | [optional]

# properties MapOfMapProperty AdditionalProperties

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str | str | any string name can be used but the value must be the correct type | [optional]

# properties MapWithUndeclaredPropertiesAnytype1

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

# properties MapWithUndeclaredPropertiesAnytype2

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

# properties MapWithUndeclaredPropertiesAnytype3

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, io.FileIO | any string name can be used but the value must be the correct type | [optional]

# properties EmptyMap

## Description
an object with no declared properties and no undeclared properties, hence it&#x27;s an empty map.

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict | an object with no declared properties and no undeclared properties, hence it&#x27;s an empty map. |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------

# properties MapWithUndeclaredPropertiesString

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str | str | any string name can be used but the value must be the correct type | [optional]

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
