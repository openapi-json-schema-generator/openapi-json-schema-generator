petstore_api.paths.fake_json_patch.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| json_patch | [FakeApi](../../apis/tags/fake_api.md) | This api is only for tag=fake |
| patch | ApiForPatch | This api is only for this endpoint |
| patch | FakeJsonPatch | This api is only for path=/fake/jsonPatch |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | json patch |
| Description | json patch route with a requestBody |
| Path | "/fake/jsonPatch" |
| HTTP Method | patch |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#requestbody) | typing.Union[[RequestBody.content.application_json_patchjson.schema](#RequestBody-content-applicationjsonpatchjson-schema), Unset, list, tuple] | optional, default is unset |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
server_index | typing.Optional[int] | default is None | Allows one to select a different [server](#servers). If not None, must be one of [0, 1, 2]
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### RequestBody

#### Content Type To Schema
Content-Type | Schema
------------ | -------
"application/json-patch+json" | [content.application_json_patchjson.Schema](#requestbody-content-applicationjsonpatchjson-schema)

#### RequestBody content ApplicationJsonPatchjson Schema

##### Type Info
Ref Class | Input Type | Accessed Type | Description
--------- | ---------- | ------------- | ------------
[JSONPatchRequest](../../components/schema/json_patch_request.md) | list, tuple | tuple |

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [SuccessDescriptionOnly.response_cls](../../components/responses/response_success_description_only.md#response_success_description_onlyresponse_cls) | Success

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
from pprint import pprint
used_configuration = api_configuration.ApiConfiguration(
)
# Enter a context with an instance of the API client
with petstore_api.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = fake_api.FakeApi(api_client)

    # example passing only optional values
    body = json_patch_request.JSONPatchRequest([
        None
    ])
    try:
        # json patch
        api_response = api_instance.json_patch(
            body=body,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling FakeApi->json_patch: %s\n" % e)
```

[[Back to top]](#top)
[[Back to FakeApi API]](../../apis/tags/fake_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)