petstore_api.paths.fake.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| group_parameters | [FakeApi](../../apis/tags/fake_api.md) | This api is only for tag=fake |
| delete | ApiForDelete | This api is only for this endpoint |
| delete | Fake | This api is only for path=/fake |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Security](#security)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | Fake endpoint to test group parameters (optional) |
| Description | Fake endpoint to test group parameters (optional) |
| Path | "/fake" |
| HTTP Method | delete |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[query_params](#query_params) | [QueryParametersDictInput](#queryparameters-queryparametersdictinput), [QueryParametersDict](#queryparameters-queryparametersdict) | |
[header_params](#header_params) | [HeaderParametersDictInput](#headerparameters-headerparametersdictinput), [HeaderParametersDict](#headerparameters-headerparametersdict) | |
security_index | typing.Optional[int] | default is None | Allows one to select a different [security](#security) definition. If not None, must be one of [0]
server_index | typing.Optional[int] | default is None | Allows one to select a different [server](#servers). If not None, must be one of [0, 1, 2]
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_response.ApiResponseWithoutDeserialization will be returned
### query_params
### QueryParameters
```
type: schemas.Schema
```

#### validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[QueryParametersDictInput](#queryparameters-queryparametersdictinput), [QueryParametersDict](#queryparameters-queryparametersdict) | [QueryParametersDict](#queryparameters-queryparametersdict) |

#### QueryParameters QueryParametersDictInput
```
type: typing.TypedDict
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**required_int64_group** | int |  |
**required_string_group** | str |  |
**int64_group** | int |  | [optional]
**string_group** | str |  | [optional]

#### QueryParameters QueryParametersDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
##### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**required_int64_group** | int |  |
**required_string_group** | str |  |
**int64_group** | int, schemas.Unset |  | [optional]
**string_group** | str, schemas.Unset |  | [optional]

##### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**required_int64_group** | int |  |
**required_string_group** | str |  |
**int64_group** | int, schemas.Unset |  | [optional]
**string_group** | str, schemas.Unset |  | [optional]

##### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [QueryParametersDictInput](#queryparameters-queryparametersdictinput), [QueryParametersDict](#queryparameters-queryparametersdict) | [QueryParametersDict](#queryparameters-queryparametersdict) | a constructor
### header_params
### HeaderParameters
```
type: schemas.Schema
```

#### validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[HeaderParametersDictInput](#headerparameters-headerparametersdictinput), [HeaderParametersDict](#headerparameters-headerparametersdict) | [HeaderParametersDict](#headerparameters-headerparametersdict) |

#### HeaderParameters HeaderParametersDictInput
```
type: typing.TypedDict
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**required_boolean_group** | typing.Literal["true", "false"] |  |
**boolean_group** | typing.Literal["true", "false"] |  | [optional]

#### HeaderParameters HeaderParametersDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
##### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**required_boolean_group** | typing.Literal["true", "false"] |  |
**boolean_group** | typing.Literal["true", "false"], schemas.Unset |  | [optional]

##### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**required_boolean_group** | typing.Literal["true", "false"] |  |
**boolean_group** | typing.Literal["true", "false"], schemas.Unset |  | [optional]

##### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [HeaderParametersDictInput](#headerparameters-headerparametersdictinput), [HeaderParametersDict](#headerparameters-headerparametersdict) | [HeaderParametersDict](#headerparameters-headerparametersdict) | a constructor

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_response.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [SuccessDescriptionOnly.ApiResponse](../../components/responses/response_success_description_only.md#apiresponse) | Success

## Security

Set auth info by setting ApiConfiguration.security_scheme_info to a dict where the
key is the below security scheme quoted name, and the value is an instance of the linked
component security scheme class.
Select the security index by setting ApiConfiguration.security_index_info or by
passing in security_index into the endpoint method.
See how to do this in the code sample.
- these securities are specific to this to this endpoint

| Security Index | Security Scheme to Scope Names |
| -------------- | ------------------------------ |
| 0       | ["bearer_test"](../../components/security_schemes/security_scheme_bearer_test.md) []<br> |

## Servers

Set the available servers by defining your used servers in ApiConfiguration.server_info
Then select your server by setting a server index in ApiConfiguration.server_index_info or by
passing server_index in to the endpoint method.
- these servers are the general api servers
- defaults to server_index=0, server.url = http://petstore.swagger.io:80/v2

server_index | Class | Description
------------ | ----- | ------------
0 | [Server0](../../servers/server_0.md) | petstore server
1 | [Server1](../../servers/server_1.md) | The local server
2 | [Server2](../../servers/server_2.md) | staging server with no variables

## Code Sample

```python
import petstore_api
from petstore_api.configurations import api_configuration
from petstore_api.apis.tags import fake_api
from petstore_api.paths.fake.delete import operation
from pprint import pprint
# security_index 0
from petstore_api.components.security_schemes import security_scheme_bearer_test

# security_scheme_info for security_index 0
security_scheme_info: api_configuration.SecuritySchemeInfo = {
    "bearer_test": security_scheme_bearer_test.BearerTest(
        access_token='someAccessToken'
    ),
}

used_configuration = api_configuration.ApiConfiguration(
    security_scheme_info=security_scheme_info,
)
# Enter a context with an instance of the API client
with petstore_api.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = fake_api.FakeApi(api_client)

    # example passing only required values which don't have defaults set
    query_params: operation.QueryParametersDictInput = {
        'required_string_group': "required_string_group_example",
        'required_int64_group': 1,
    }
    header_params: operation.HeaderParametersDictInput = {
        'required_boolean_group': "true",
    }
    try:
        # Fake endpoint to test group parameters (optional)
        api_response = api_instance.group_parameters(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling FakeApi->group_parameters: %s\n" % e)

    # example passing only optional values
    query_params: operation.QueryParametersDictInput = {
        'required_string_group': "required_string_group_example",
        'required_int64_group': 1,
        'string_group': "string_group_example",
        'int64_group': 1,
    }
    header_params: operation.HeaderParametersDictInput = {
        'required_boolean_group': "true",
        'boolean_group': "true",
    }
    try:
        # Fake endpoint to test group parameters (optional)
        api_response = api_instance.group_parameters(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling FakeApi->group_parameters: %s\n" % e)
```

[[Back to top]](#top)
[[Back to FakeApi API]](../../apis/tags/fake_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)