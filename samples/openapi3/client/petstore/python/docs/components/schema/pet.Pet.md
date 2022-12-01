<a name="top"></a>
<a id="Pet"></a>
# petstore_api.components.schema.pet.Pet

Pet object that needs to be added to the store

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Pet object that needs to be added to the store | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[photoUrls](#photoUrls)** | list, tuple,  | tuple,  |  | 
**name** | str,  | str,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**category** | [**Category**](category.Category.md) | [**Category**](category.Category.md) |  | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  |  | [optional] 
**status** | str,  | str,  | pet status in the store | [optional] must be one of ["available", "pending", "sold", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# photoUrls

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Tag**](tag.Tag.md) | [**Tag**](tag.Tag.md) | [**Tag**](tag.Tag.md) |  | 

[[Back to top]](#top) [[Back to README]](../../../README.md)