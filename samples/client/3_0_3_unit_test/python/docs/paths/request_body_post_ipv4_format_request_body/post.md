unit_test_api.paths.request_body_post_ipv4_format_request_body.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| post_ipv4_format_request_body | [OperationRequestBodyApi](../../apis/tags/operation_request_body_api.md) | This api is only for tag=operation.requestBody |
| post_ipv4_format_request_body | [PathPostApi](../../apis/tags/path_post_api.md) | This api is only for tag=path.post |
| post_ipv4_format_request_body | [ContentTypeJsonApi](../../apis/tags/content_type_json_api.md) | This api is only for tag=contentType_json |
| post_ipv4_format_request_body | [FormatApi](../../apis/tags/format_api.md) | This api is only for tag=format |
| post | ApiForPost | This api is only for this endpoint |
| post | RequestBodyPostIpv4FormatRequestBody | This api is only for path=/requestBody/postIpv4FormatRequestBody |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Path | "/requestBody/postIpv4FormatRequestBody" |
| HTTP Method | post |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#requestbody) | typing.Union[dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body. value must be one of ['application/json']
server_index | typing.Optional[int] | default is None | Allows one to select a different [server](#servers). If not None, must be one of [0]
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_response.ApiResponseWithoutDeserialization will be returned

### RequestBody

#### Content Type To Schema
Content-Type | Schema
------------ | -------
"application/json" | [content.application_json.Schema](#requestbody-content-applicationjson-schema)

#### RequestBody content ApplicationJson Schema
unit_test_api.paths.request_body_post_ipv4_format_request_body.post.request_body.content.application_json.schema
```
type: schemas.Schema
```

##### Ref Schema Info
Ref Schema | Input Type | Output Type
---------- | ---------- | -----------
[**ipv4_format.Ipv4Format**](../../components/schema/ipv4_format.md) | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | schemas.immutabledict, str, float, int, bool, None, tuple, bytes, io.FileIO

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_response.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ResponseFor200.ApiResponse](#responsefor200-apiresponse) | success

## ResponseFor200

### Description
success

### ResponseFor200 ApiResponse
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
- defaults to server_index=0, server.url = https://someserver.com/v1

server_index | Class | Description
------------ | ----- | ------------
0 | [Server0](../../servers/server_0.md) |

## Code Sample

```python
import unit_test_api
from unit_test_api.configurations import api_configuration
from unit_test_api.apis.tags import operation_request_body_api
from pprint import pprint
used_configuration = api_configuration.ApiConfiguration(
)
# Enter a context with an instance of the API client
with unit_test_api.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = operation_request_body_api.OperationRequestBodyApi(api_client)

    # example passing only required values which don't have defaults set
    body = ipv4_format.Ipv4Format(None)
    try:
        api_response = api_instance.post_ipv4_format_request_body(
            body=body,
        )
        pprint(api_response)
    except unit_test_api.ApiException as e:
        print("Exception when calling OperationRequestBodyApi->post_ipv4_format_request_body: %s\n" % e)
```

[[Back to top]](#top)
[[Back to OperationRequestBodyApi API]](../../apis/tags/operation_request_body_api.md)
[[Back to PathPostApi API]](../../apis/tags/path_post_api.md)
[[Back to ContentTypeJsonApi API]](../../apis/tags/content_type_json_api.md)
[[Back to FormatApi API]](../../apis/tags/format_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)