petstore_api.paths.fake_query_param_with_json_content_type.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| query_param_with_json_content_type | [FakeApi](../../apis/tags/fake_api.md) | This api is only for tag=fake |
| get | ApiForGet | This api is only for this endpoint |
| get | FakeQueryParamWithJsonContentType | This api is only for path=/fake/queryParamWithJsonContentType |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | query param with json content-type |
| Path | "/fake/queryParamWithJsonContentType" |
| HTTP Method | get |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[query_params](#query_params) | [RequestQueryParameters.Params](#requestqueryparametersparams), dict | |
accept_content_types | typing.Tuple[str] | default is ("application/json", ) | Tells the server the content type(s) that are accepted by the client
server_index | typing.Optional[int] | default is None | Allows one to select a different [server](#servers). If not None, must be one of [0, 1, 2]
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_response.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParameters.Params
This is a TypedDict

Key | Input Type | Description  | Notes
------------- | ------------- | ------------- | -------------
someParam | [Parameter0.content.application_json.schema](#parameter0-content-applicationjson-schema), dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | | 


#### Parameter0

##### Description
The internal object id

##### Content Type To Schema
Content-Type | Schema
------------ | -------
"application/json" | [content.application_json.Schema](#parameter0-content-applicationjson-schema)
##### Parameter0 content ApplicationJson Schema

###### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, io.FileIO |  |

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_response.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ResponseFor200.response_cls](#responsefor200-response_cls) | success

## ResponseFor200

### Description
success

### ResponseFor200 response_cls
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
[body](#responsefor200-body) | [content.application_json.schema](#responsefor200-content-applicationjson-schema) |  |
headers | Unset | headers were not defined |

### ResponseFor200 Body
Content-Type | Schema
------------ | -------
"application/json" | [content.application_json.Schema](#responsefor200-content-applicationjson-schema)

### Body Details
#### ResponseFor200 content ApplicationJson Schema

##### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, io.FileIO |  |

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
from petstore_api.paths.fake_query_param_with_json_content_type.get import operation
from pprint import pprint
used_configuration = api_configuration.ApiConfiguration(
)
# Enter a context with an instance of the API client
with petstore_api.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = fake_api.FakeApi(api_client)

    # example passing only required values which don't have defaults set
    query_params: operation.RequestQueryParameters.Params = {
        'someParam': ,
    }
    try:
        # query param with json content-type
        api_response = api_instance.query_param_with_json_content_type(
            query_params=query_params,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling FakeApi->query_param_with_json_content_type: %s\n" % e)
```

[[Back to top]](#top)
[[Back to FakeApi API]](../../apis/tags/fake_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)