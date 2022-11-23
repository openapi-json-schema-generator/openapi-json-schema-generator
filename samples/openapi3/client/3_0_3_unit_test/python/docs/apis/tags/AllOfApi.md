<a name="__pageTop"></a>
# unit_test_api.apis.tags.all_of_api.AllOfApi

All URIs are relative to *https://someserver.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_allof_combined_with_anyof_oneof_request_body**](#post_allof_combined_with_anyof_oneof_request_body) | **post** /requestBody/postAllofCombinedWithAnyofOneofRequestBody | 
[**post_allof_combined_with_anyof_oneof_response_body_for_content_types**](#post_allof_combined_with_anyof_oneof_response_body_for_content_types) | **post** /responseBody/postAllofCombinedWithAnyofOneofResponseBodyForContentTypes | 
[**post_allof_request_body**](#post_allof_request_body) | **post** /requestBody/postAllofRequestBody | 
[**post_allof_response_body_for_content_types**](#post_allof_response_body_for_content_types) | **post** /responseBody/postAllofResponseBodyForContentTypes | 
[**post_allof_simple_types_request_body**](#post_allof_simple_types_request_body) | **post** /requestBody/postAllofSimpleTypesRequestBody | 
[**post_allof_simple_types_response_body_for_content_types**](#post_allof_simple_types_response_body_for_content_types) | **post** /responseBody/postAllofSimpleTypesResponseBodyForContentTypes | 
[**post_allof_with_base_schema_request_body**](#post_allof_with_base_schema_request_body) | **post** /requestBody/postAllofWithBaseSchemaRequestBody | 
[**post_allof_with_base_schema_response_body_for_content_types**](#post_allof_with_base_schema_response_body_for_content_types) | **post** /responseBody/postAllofWithBaseSchemaResponseBodyForContentTypes | 
[**post_allof_with_one_empty_schema_request_body**](#post_allof_with_one_empty_schema_request_body) | **post** /requestBody/postAllofWithOneEmptySchemaRequestBody | 
[**post_allof_with_one_empty_schema_response_body_for_content_types**](#post_allof_with_one_empty_schema_response_body_for_content_types) | **post** /responseBody/postAllofWithOneEmptySchemaResponseBodyForContentTypes | 
[**post_allof_with_the_first_empty_schema_request_body**](#post_allof_with_the_first_empty_schema_request_body) | **post** /requestBody/postAllofWithTheFirstEmptySchemaRequestBody | 
[**post_allof_with_the_first_empty_schema_response_body_for_content_types**](#post_allof_with_the_first_empty_schema_response_body_for_content_types) | **post** /responseBody/postAllofWithTheFirstEmptySchemaResponseBodyForContentTypes | 
[**post_allof_with_the_last_empty_schema_request_body**](#post_allof_with_the_last_empty_schema_request_body) | **post** /requestBody/postAllofWithTheLastEmptySchemaRequestBody | 
[**post_allof_with_the_last_empty_schema_response_body_for_content_types**](#post_allof_with_the_last_empty_schema_response_body_for_content_types) | **post** /responseBody/postAllofWithTheLastEmptySchemaResponseBodyForContentTypes | 
[**post_allof_with_two_empty_schemas_request_body**](#post_allof_with_two_empty_schemas_request_body) | **post** /requestBody/postAllofWithTwoEmptySchemasRequestBody | 
[**post_allof_with_two_empty_schemas_response_body_for_content_types**](#post_allof_with_two_empty_schemas_response_body_for_content_types) | **post** /responseBody/postAllofWithTwoEmptySchemasResponseBodyForContentTypes | 
[**post_nested_allof_to_check_validation_semantics_request_body**](#post_nested_allof_to_check_validation_semantics_request_body) | **post** /requestBody/postNestedAllofToCheckValidationSemanticsRequestBody | 
[**post_nested_allof_to_check_validation_semantics_response_body_for_content_types**](#post_nested_allof_to_check_validation_semantics_response_body_for_content_types) | **post** /responseBody/postNestedAllofToCheckValidationSemanticsResponseBodyForContentTypes | 

# **post_allof_combined_with_anyof_oneof_request_body**
<a name="post_allof_combined_with_anyof_oneof_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = allof_combined_with_anyof_oneof.AllofCombinedWithAnyofOneof(None)
    try:
        api_response = api_instance.post_allof_combined_with_anyof_oneof_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_combined_with_anyof_oneof_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_allof_combined_with_anyof_oneof_request_body.request_body) | typing.Union[[request_body.application_json](#post_allof_combined_with_anyof_oneof_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_allof_combined_with_anyof_oneof_request_body.request_body" >body</a>

# <a id="post_allof_combined_with_anyof_oneof_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofCombinedWithAnyofOneof**](../../components/schema/allof_combined_with_anyof_oneof.AllofCombinedWithAnyofOneof.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_combined_with_anyof_oneof_request_body.response_for_200.ApiResponse) | success

#### <a id="post_allof_combined_with_anyof_oneof_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_combined_with_anyof_oneof_response_body_for_content_types**
<a name="post_allof_combined_with_anyof_oneof_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_allof_combined_with_anyof_oneof_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_combined_with_anyof_oneof_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_combined_with_anyof_oneof_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_allof_combined_with_anyof_oneof_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_allof_combined_with_anyof_oneof_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_allof_combined_with_anyof_oneof_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofCombinedWithAnyofOneof**](../../components/schema/allof_combined_with_anyof_oneof.AllofCombinedWithAnyofOneof.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_request_body**
<a name="post_allof_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = allof.Allof(None)
    try:
        api_response = api_instance.post_allof_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_allof_request_body.request_body) | typing.Union[[request_body.application_json](#post_allof_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_allof_request_body.request_body" >body</a>

# <a id="post_allof_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Allof**](../../components/schema/allof.Allof.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_request_body.response_for_200.ApiResponse) | success

#### <a id="post_allof_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_response_body_for_content_types**
<a name="post_allof_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_allof_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_allof_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_allof_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_allof_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Allof**](../../components/schema/allof.Allof.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_simple_types_request_body**
<a name="post_allof_simple_types_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = allof_simple_types.AllofSimpleTypes(None)
    try:
        api_response = api_instance.post_allof_simple_types_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_simple_types_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_allof_simple_types_request_body.request_body) | typing.Union[[request_body.application_json](#post_allof_simple_types_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_allof_simple_types_request_body.request_body" >body</a>

# <a id="post_allof_simple_types_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofSimpleTypes**](../../components/schema/allof_simple_types.AllofSimpleTypes.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_simple_types_request_body.response_for_200.ApiResponse) | success

#### <a id="post_allof_simple_types_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_simple_types_response_body_for_content_types**
<a name="post_allof_simple_types_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_allof_simple_types_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_simple_types_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_simple_types_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_allof_simple_types_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_allof_simple_types_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_allof_simple_types_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofSimpleTypes**](../../components/schema/allof_simple_types.AllofSimpleTypes.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_base_schema_request_body**
<a name="post_allof_with_base_schema_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = allof_with_base_schema.AllofWithBaseSchema({})
    try:
        api_response = api_instance.post_allof_with_base_schema_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_base_schema_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_allof_with_base_schema_request_body.request_body) | typing.Union[[request_body.application_json](#post_allof_with_base_schema_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_allof_with_base_schema_request_body.request_body" >body</a>

# <a id="post_allof_with_base_schema_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithBaseSchema**](../../components/schema/allof_with_base_schema.AllofWithBaseSchema.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_base_schema_request_body.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_base_schema_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_base_schema_response_body_for_content_types**
<a name="post_allof_with_base_schema_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_allof_with_base_schema_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_base_schema_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_base_schema_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_base_schema_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_allof_with_base_schema_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_allof_with_base_schema_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithBaseSchema**](../../components/schema/allof_with_base_schema.AllofWithBaseSchema.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_one_empty_schema_request_body**
<a name="post_allof_with_one_empty_schema_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = allof_with_one_empty_schema.AllofWithOneEmptySchema(None)
    try:
        api_response = api_instance.post_allof_with_one_empty_schema_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_one_empty_schema_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_allof_with_one_empty_schema_request_body.request_body) | typing.Union[[request_body.application_json](#post_allof_with_one_empty_schema_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_allof_with_one_empty_schema_request_body.request_body" >body</a>

# <a id="post_allof_with_one_empty_schema_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithOneEmptySchema**](../../components/schema/allof_with_one_empty_schema.AllofWithOneEmptySchema.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_one_empty_schema_request_body.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_one_empty_schema_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_one_empty_schema_response_body_for_content_types**
<a name="post_allof_with_one_empty_schema_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_allof_with_one_empty_schema_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_one_empty_schema_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_one_empty_schema_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_one_empty_schema_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_allof_with_one_empty_schema_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_allof_with_one_empty_schema_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithOneEmptySchema**](../../components/schema/allof_with_one_empty_schema.AllofWithOneEmptySchema.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_the_first_empty_schema_request_body**
<a name="post_allof_with_the_first_empty_schema_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = allof_with_the_first_empty_schema.AllofWithTheFirstEmptySchema(None)
    try:
        api_response = api_instance.post_allof_with_the_first_empty_schema_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_the_first_empty_schema_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_allof_with_the_first_empty_schema_request_body.request_body) | typing.Union[[request_body.application_json](#post_allof_with_the_first_empty_schema_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_allof_with_the_first_empty_schema_request_body.request_body" >body</a>

# <a id="post_allof_with_the_first_empty_schema_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithTheFirstEmptySchema**](../../components/schema/allof_with_the_first_empty_schema.AllofWithTheFirstEmptySchema.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_the_first_empty_schema_request_body.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_the_first_empty_schema_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_the_first_empty_schema_response_body_for_content_types**
<a name="post_allof_with_the_first_empty_schema_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_allof_with_the_first_empty_schema_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_the_first_empty_schema_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_the_first_empty_schema_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_the_first_empty_schema_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_allof_with_the_first_empty_schema_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_allof_with_the_first_empty_schema_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithTheFirstEmptySchema**](../../components/schema/allof_with_the_first_empty_schema.AllofWithTheFirstEmptySchema.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_the_last_empty_schema_request_body**
<a name="post_allof_with_the_last_empty_schema_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = allof_with_the_last_empty_schema.AllofWithTheLastEmptySchema(None)
    try:
        api_response = api_instance.post_allof_with_the_last_empty_schema_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_the_last_empty_schema_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_allof_with_the_last_empty_schema_request_body.request_body) | typing.Union[[request_body.application_json](#post_allof_with_the_last_empty_schema_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_allof_with_the_last_empty_schema_request_body.request_body" >body</a>

# <a id="post_allof_with_the_last_empty_schema_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithTheLastEmptySchema**](../../components/schema/allof_with_the_last_empty_schema.AllofWithTheLastEmptySchema.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_the_last_empty_schema_request_body.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_the_last_empty_schema_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_the_last_empty_schema_response_body_for_content_types**
<a name="post_allof_with_the_last_empty_schema_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_allof_with_the_last_empty_schema_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_the_last_empty_schema_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_the_last_empty_schema_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_the_last_empty_schema_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_allof_with_the_last_empty_schema_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_allof_with_the_last_empty_schema_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithTheLastEmptySchema**](../../components/schema/allof_with_the_last_empty_schema.AllofWithTheLastEmptySchema.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_two_empty_schemas_request_body**
<a name="post_allof_with_two_empty_schemas_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = allof_with_two_empty_schemas.AllofWithTwoEmptySchemas(None)
    try:
        api_response = api_instance.post_allof_with_two_empty_schemas_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_two_empty_schemas_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_allof_with_two_empty_schemas_request_body.request_body) | typing.Union[[request_body.application_json](#post_allof_with_two_empty_schemas_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_allof_with_two_empty_schemas_request_body.request_body" >body</a>

# <a id="post_allof_with_two_empty_schemas_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithTwoEmptySchemas**](../../components/schema/allof_with_two_empty_schemas.AllofWithTwoEmptySchemas.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_two_empty_schemas_request_body.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_two_empty_schemas_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_allof_with_two_empty_schemas_response_body_for_content_types**
<a name="post_allof_with_two_empty_schemas_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_allof_with_two_empty_schemas_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_allof_with_two_empty_schemas_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_allof_with_two_empty_schemas_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_allof_with_two_empty_schemas_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_allof_with_two_empty_schemas_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_allof_with_two_empty_schemas_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AllofWithTwoEmptySchemas**](../../components/schema/allof_with_two_empty_schemas.AllofWithTwoEmptySchemas.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_nested_allof_to_check_validation_semantics_request_body**
<a name="post_nested_allof_to_check_validation_semantics_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = nested_allof_to_check_validation_semantics.NestedAllofToCheckValidationSemantics(None)
    try:
        api_response = api_instance.post_nested_allof_to_check_validation_semantics_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_nested_allof_to_check_validation_semantics_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_nested_allof_to_check_validation_semantics_request_body.request_body) | typing.Union[[request_body.application_json](#post_nested_allof_to_check_validation_semantics_request_body.request_body.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_nested_allof_to_check_validation_semantics_request_body.request_body" >body</a>

# <a id="post_nested_allof_to_check_validation_semantics_request_body.request_body.application_json" >request_body.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**NestedAllofToCheckValidationSemantics**](../../components/schema/nested_allof_to_check_validation_semantics.NestedAllofToCheckValidationSemantics.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_nested_allof_to_check_validation_semantics_request_body.response_for_200.ApiResponse) | success

#### <a id="post_nested_allof_to_check_validation_semantics_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_nested_allof_to_check_validation_semantics_response_body_for_content_types**
<a name="post_nested_allof_to_check_validation_semantics_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import all_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_of_api.AllOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_nested_allof_to_check_validation_semantics_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AllOfApi->post_nested_allof_to_check_validation_semantics_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_nested_allof_to_check_validation_semantics_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_nested_allof_to_check_validation_semantics_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.application_json](#post_nested_allof_to_check_validation_semantics_response_body_for_content_types.response_for_200.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_nested_allof_to_check_validation_semantics_response_body_for_content_types.response_for_200.application_json" >response_for_200.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**NestedAllofToCheckValidationSemantics**](../../components/schema/nested_allof_to_check_validation_semantics.NestedAllofToCheckValidationSemantics.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

