petstore_api.paths.fake_inline_additional_properties.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| inline_additional_properties | [FakeApi](../../apis/tags/fake_api.md) | This api is only for tag=fake |
| post | ApiForPost | This api is only for this endpoint |
| post | FakeInlineAdditionalProperties | This api is only for path=/fake/inline-additionalProperties |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | test inline additionalProperties |
| Description |  |
| Path | "/fake/inline-additionalProperties" |
| HTTP Method | post |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#requestbody) | typing.Union[[schema.SchemaDictInput](../../paths/fake_inline_additional_properties/post/request_body/content/application_json/schema.md#schemadictinput), [schema.SchemaDict](../../paths/fake_inline_additional_properties/post/request_body/content/application_json/schema.md#schemadict)] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body. value must be one of ['application/json']
server_index | typing.Optional[int] | default is None | Allows one to select a different [server](#servers). If not None, must be one of [0, 1, 2]
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_response.ApiResponseWithoutDeserialization will be returned

### RequestBody

#### Description
request body

#### Content Type To Schema
Content-Type | Schema
------------ | -------
"application/json" | [content.application_json.Schema](#requestbody-content-applicationjson-schema)

#### RequestBody content ApplicationJson Schema
```
type: schemas.Schema
```

##### validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[SchemaDictInput](#requestbody-content-applicationjson-schema-schemadictinput), [SchemaDict](#requestbody-content-applicationjson-schema-schemadict) | [SchemaDict](#requestbody-content-applicationjson-schema-schemadict) |

##### RequestBody content ApplicationJson Schema SchemaDictInput
```
type: typing.Mapping[
    str,
    str,
]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**any_string_name** | str | any string name can be used but the value must be the correct type | [optional]

##### RequestBody content ApplicationJson Schema SchemaDict
```
base class: schemas.immutabledict[str, str]

```
###### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**kwargs** | str | any string name can be used but the value must be the correct type | [optional] typed value is accessed with the get_additional_property_ method

###### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [SchemaDictInput](#requestbody-content-applicationjson-schema-schemadictinput), [SchemaDict](#requestbody-content-applicationjson-schema-schemadict) | [SchemaDict](#requestbody-content-applicationjson-schema-schemadict) | a constructor
get_additional_property_ | str | str, schemas.Unset | provides type safety for additional properties

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_response.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [SuccessDescriptionOnly.ApiResponse](../../components/responses/response_success_description_only.md#apiresponse) | Success

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

    # example passing only required values which don't have defaults set
    body = {
        "key": "key_example",
    }
    try:
        # test inline additionalProperties
        api_response = api_instance.inline_additional_properties(
            body=body,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling FakeApi->inline_additional_properties: %s\n" % e)
```

[[Back to top]](#top)
[[Back to FakeApi API]](../../apis/tags/fake_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)