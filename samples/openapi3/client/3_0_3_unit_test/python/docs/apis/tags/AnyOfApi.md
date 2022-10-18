<a name="__pageTop"></a>
# unit_test_api.apis.tags.any_of_api.AnyOfApi

All URIs are relative to *https://someserver.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_anyof_complex_types_request_body**](#post_anyof_complex_types_request_body) | **post** /requestBody/postAnyofComplexTypesRequestBody | 
[**post_anyof_complex_types_response_body_for_content_types**](#post_anyof_complex_types_response_body_for_content_types) | **post** /responseBody/postAnyofComplexTypesResponseBodyForContentTypes | 
[**post_anyof_request_body**](#post_anyof_request_body) | **post** /requestBody/postAnyofRequestBody | 
[**post_anyof_response_body_for_content_types**](#post_anyof_response_body_for_content_types) | **post** /responseBody/postAnyofResponseBodyForContentTypes | 
[**post_anyof_with_base_schema_request_body**](#post_anyof_with_base_schema_request_body) | **post** /requestBody/postAnyofWithBaseSchemaRequestBody | 
[**post_anyof_with_base_schema_response_body_for_content_types**](#post_anyof_with_base_schema_response_body_for_content_types) | **post** /responseBody/postAnyofWithBaseSchemaResponseBodyForContentTypes | 
[**post_anyof_with_one_empty_schema_request_body**](#post_anyof_with_one_empty_schema_request_body) | **post** /requestBody/postAnyofWithOneEmptySchemaRequestBody | 
[**post_anyof_with_one_empty_schema_response_body_for_content_types**](#post_anyof_with_one_empty_schema_response_body_for_content_types) | **post** /responseBody/postAnyofWithOneEmptySchemaResponseBodyForContentTypes | 
[**post_nested_anyof_to_check_validation_semantics_request_body**](#post_nested_anyof_to_check_validation_semantics_request_body) | **post** /requestBody/postNestedAnyofToCheckValidationSemanticsRequestBody | 
[**post_nested_anyof_to_check_validation_semantics_response_body_for_content_types**](#post_nested_anyof_to_check_validation_semantics_response_body_for_content_types) | **post** /responseBody/postNestedAnyofToCheckValidationSemanticsResponseBodyForContentTypes | 

# **post_anyof_complex_types_request_body**
<a name="post_anyof_complex_types_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from unit_test_api.components.schema import anyof_complex_types_oapg
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = AnyofComplexTypes(None)
    try:
        api_response = api_instance.post_anyof_complex_types_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_anyof_complex_types_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_anyof_complex_types_request_body.RequestBody) | typing.Union[[RequestBody.Schemas.application_json](#post_anyof_complex_types_request_body.RequestBody.Schemas.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_anyof_complex_types_request_body.RequestBody" >body</a>

# <a id="post_anyof_complex_types_request_body.RequestBody.Schemas.application_json" >RequestBody.Schemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AnyofComplexTypes**](../../components/schema/anyof_complex_types_oapg.AnyofComplexTypes.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_anyof_complex_types_request_body.response_for_200.ApiResponse) | success

#### <a id="post_anyof_complex_types_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_anyof_complex_types_response_body_for_content_types**
<a name="post_anyof_complex_types_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_anyof_complex_types_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_anyof_complex_types_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_anyof_complex_types_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_anyof_complex_types_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.BodySchemas.application_json](#post_anyof_complex_types_response_body_for_content_types.response_for_200.BodySchemas.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_anyof_complex_types_response_body_for_content_types.response_for_200.BodySchemas.application_json" >response_for_200.BodySchemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AnyofComplexTypes**](../../components/schema/anyof_complex_types_oapg.AnyofComplexTypes.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_anyof_request_body**
<a name="post_anyof_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from unit_test_api.components.schema import anyof_oapg
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = Anyof(None)
    try:
        api_response = api_instance.post_anyof_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_anyof_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_anyof_request_body.RequestBody) | typing.Union[[RequestBody.Schemas.application_json](#post_anyof_request_body.RequestBody.Schemas.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_anyof_request_body.RequestBody" >body</a>

# <a id="post_anyof_request_body.RequestBody.Schemas.application_json" >RequestBody.Schemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Anyof**](../../components/schema/anyof_oapg.Anyof.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_anyof_request_body.response_for_200.ApiResponse) | success

#### <a id="post_anyof_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_anyof_response_body_for_content_types**
<a name="post_anyof_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_anyof_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_anyof_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_anyof_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_anyof_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.BodySchemas.application_json](#post_anyof_response_body_for_content_types.response_for_200.BodySchemas.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_anyof_response_body_for_content_types.response_for_200.BodySchemas.application_json" >response_for_200.BodySchemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**Anyof**](../../components/schema/anyof_oapg.Anyof.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_anyof_with_base_schema_request_body**
<a name="post_anyof_with_base_schema_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from unit_test_api.components.schema import anyof_with_base_schema_oapg
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = AnyofWithBaseSchema("body_example")
    try:
        api_response = api_instance.post_anyof_with_base_schema_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_anyof_with_base_schema_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_anyof_with_base_schema_request_body.RequestBody) | typing.Union[[RequestBody.Schemas.application_json](#post_anyof_with_base_schema_request_body.RequestBody.Schemas.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_anyof_with_base_schema_request_body.RequestBody" >body</a>

# <a id="post_anyof_with_base_schema_request_body.RequestBody.Schemas.application_json" >RequestBody.Schemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AnyofWithBaseSchema**](../../components/schema/anyof_with_base_schema_oapg.AnyofWithBaseSchema.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_anyof_with_base_schema_request_body.response_for_200.ApiResponse) | success

#### <a id="post_anyof_with_base_schema_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_anyof_with_base_schema_response_body_for_content_types**
<a name="post_anyof_with_base_schema_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_anyof_with_base_schema_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_anyof_with_base_schema_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_anyof_with_base_schema_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_anyof_with_base_schema_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.BodySchemas.application_json](#post_anyof_with_base_schema_response_body_for_content_types.response_for_200.BodySchemas.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_anyof_with_base_schema_response_body_for_content_types.response_for_200.BodySchemas.application_json" >response_for_200.BodySchemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AnyofWithBaseSchema**](../../components/schema/anyof_with_base_schema_oapg.AnyofWithBaseSchema.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_anyof_with_one_empty_schema_request_body**
<a name="post_anyof_with_one_empty_schema_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from unit_test_api.components.schema import anyof_with_one_empty_schema_oapg
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = AnyofWithOneEmptySchema(None)
    try:
        api_response = api_instance.post_anyof_with_one_empty_schema_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_anyof_with_one_empty_schema_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_anyof_with_one_empty_schema_request_body.RequestBody) | typing.Union[[RequestBody.Schemas.application_json](#post_anyof_with_one_empty_schema_request_body.RequestBody.Schemas.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_anyof_with_one_empty_schema_request_body.RequestBody" >body</a>

# <a id="post_anyof_with_one_empty_schema_request_body.RequestBody.Schemas.application_json" >RequestBody.Schemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AnyofWithOneEmptySchema**](../../components/schema/anyof_with_one_empty_schema_oapg.AnyofWithOneEmptySchema.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_anyof_with_one_empty_schema_request_body.response_for_200.ApiResponse) | success

#### <a id="post_anyof_with_one_empty_schema_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_anyof_with_one_empty_schema_response_body_for_content_types**
<a name="post_anyof_with_one_empty_schema_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_anyof_with_one_empty_schema_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_anyof_with_one_empty_schema_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_anyof_with_one_empty_schema_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_anyof_with_one_empty_schema_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.BodySchemas.application_json](#post_anyof_with_one_empty_schema_response_body_for_content_types.response_for_200.BodySchemas.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_anyof_with_one_empty_schema_response_body_for_content_types.response_for_200.BodySchemas.application_json" >response_for_200.BodySchemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**AnyofWithOneEmptySchema**](../../components/schema/anyof_with_one_empty_schema_oapg.AnyofWithOneEmptySchema.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_nested_anyof_to_check_validation_semantics_request_body**
<a name="post_nested_anyof_to_check_validation_semantics_request_body"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from unit_test_api.components.schema import nested_anyof_to_check_validation_semantics_oapg
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example passing only required values which don't have defaults set
    body = NestedAnyofToCheckValidationSemantics(None)
    try:
        api_response = api_instance.post_nested_anyof_to_check_validation_semantics_request_body(
            body=body,
        )
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_nested_anyof_to_check_validation_semantics_request_body: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#post_nested_anyof_to_check_validation_semantics_request_body.RequestBody) | typing.Union[[RequestBody.Schemas.application_json](#post_nested_anyof_to_check_validation_semantics_request_body.RequestBody.Schemas.application_json)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### <a id="post_nested_anyof_to_check_validation_semantics_request_body.RequestBody" >body</a>

# <a id="post_nested_anyof_to_check_validation_semantics_request_body.RequestBody.Schemas.application_json" >RequestBody.Schemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**NestedAnyofToCheckValidationSemantics**](../../components/schema/nested_anyof_to_check_validation_semantics_oapg.NestedAnyofToCheckValidationSemantics.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_nested_anyof_to_check_validation_semantics_request_body.response_for_200.ApiResponse) | success

#### <a id="post_nested_anyof_to_check_validation_semantics_request_body.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_nested_anyof_to_check_validation_semantics_response_body_for_content_types**
<a name="post_nested_anyof_to_check_validation_semantics_response_body_for_content_types"></a>


### Example

```python
import unit_test_api
from unit_test_api.apis.tags import any_of_api
from pprint import pprint
# Defining the host is optional and defaults to https://someserver.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = unit_test_api.Configuration(
    host = "https://someserver.com/v1"
)

# Enter a context with an instance of the API client
with unit_test_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = any_of_api.AnyOfApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.post_nested_anyof_to_check_validation_semantics_response_body_for_content_types()
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling AnyOfApi->post_nested_anyof_to_check_validation_semantics_response_body_for_content_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [response_for_200.ApiResponse](#post_nested_anyof_to_check_validation_semantics_response_body_for_content_types.response_for_200.ApiResponse) | success

#### <a id="post_nested_anyof_to_check_validation_semantics_response_body_for_content_types.response_for_200.ApiResponse" >response_for_200.ApiResponse</a>
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[[response_for_200.BodySchemas.application_json](#post_nested_anyof_to_check_validation_semantics_response_body_for_content_types.response_for_200.BodySchemas.application_json), ] |  |
headers | Unset | headers were not defined |

# <a id="post_nested_anyof_to_check_validation_semantics_response_body_for_content_types.response_for_200.BodySchemas.application_json" >response_for_200.BodySchemas.application_json</a>
Type | Description  | Notes
------------- | ------------- | -------------
[**NestedAnyofToCheckValidationSemantics**](../../components/schema/nested_anyof_to_check_validation_semantics_oapg.NestedAnyofToCheckValidationSemantics.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

