petstore_api.paths.fake_delete_coffee_id.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| delete_coffee | [FakeApi](../../apis/tags/fake_api.md) | This api is only for tag=fake |
| delete | ApiForDelete | This api is only for this endpoint |
| delete | FakeDeleteCoffeeId | This api is only for path=/fake/deleteCoffee/{id} |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | Delete coffee |
| Description | Delete the coffee identified by the given id, (delete without request body) |
| Path | "/fake/deleteCoffee/{id}" |
| HTTP Method | delete |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[path_params](#path_params) | [PathParametersDictInput](#pathparameters-pathparametersdictinput), [PathParametersDict](#pathparameters-pathparametersdict) | |
server_index | typing.Optional[int] | default is None | Allows one to select a different [server](#servers). If not None, must be one of [0, 1, 2]
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_response.ApiResponseWithoutDeserialization will be returned
### path_params
### PathParameters
```
type: schemas.Schema
```

#### validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[PathParametersDictInput](#pathparameters-pathparametersdictinput), [PathParametersDict](#pathparameters-pathparametersdict) | [PathParametersDict](#pathparameters-pathparametersdict) |

#### PathParameters PathParametersDictInput
```
type: typing.TypedDict
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**id** | str |  |

#### PathParameters PathParametersDict
```
base class: schemas.immutabledict[str, str]

```
##### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**id** | str |  |

##### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**id** | str |  |

##### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [PathParametersDictInput](#pathparameters-pathparametersdictinput), [PathParametersDict](#pathparameters-pathparametersdict) | [PathParametersDict](#pathparameters-pathparametersdict) | a constructor

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_response.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [Default.ApiResponse](#default-apiresponse) | Unexpected error
200 | [SuccessDescriptionOnly.ApiResponse](../../components/responses/response_success_description_only.md#apiresponse) | Success

## Default

### Description
Unexpected error

### Default ApiResponse
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

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
from petstore_api.paths.fake_delete_coffee_id.delete import operation
from pprint import pprint
used_configuration = api_configuration.ApiConfiguration(
)
# Enter a context with an instance of the API client
with petstore_api.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = fake_api.FakeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params: operation.PathParametersDictInput = {
        'id': "id_example",
    }
    try:
        # Delete coffee
        api_response = api_instance.delete_coffee(
            path_params=path_params,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling FakeApi->delete_coffee: %s\n" % e)
```

[[Back to top]](#top)
[[Back to FakeApi API]](../../apis/tags/fake_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)