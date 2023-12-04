petstore_api.paths.fake_json_form_data.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| json_form_data | [FakeApi](../../apis/tags/fake_api.md) | This api is only for tag=fake |
| get | ApiForGet | This api is only for this endpoint |
| get | FakeJsonFormData | This api is only for path=/fake/jsonFormData |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | test json serialization of form data |
| Path | "/fake/jsonFormData" |
| HTTP Method | get |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#requestbody) | typing.Union[[schema.SchemaDictInput](../../paths/fake_json_form_data/get/request_body/content/application_x_www_form_urlencoded/schema.md#schemadictinput), [schema.SchemaDict](../../paths/fake_json_form_data/get/request_body/content/application_x_www_form_urlencoded/schema.md#schemadict), schemas.Unset] | optional, default is unset |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body. value must be one of ['application/x-www-form-urlencoded']
server_index | typing.Optional[int] | default is None | Allows one to select a different [server](#servers). If not None, must be one of [0, 1, 2]
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_response.ApiResponseWithoutDeserialization will be returned

### RequestBody

#### Content Type To Schema
Content-Type | Schema
------------ | -------
"application/x-www-form-urlencoded" | [content.application_x_www_form_urlencoded.Schema](#requestbody-content-applicationxwwwformurlencoded-schema)

#### RequestBody content ApplicationXWwwFormUrlencoded Schema
petstore_api.paths.fake_json_form_data.get.request_body.content.application_x_www_form_urlencoded.schema
```
type: schemas.Schema
```

##### validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[SchemaDictInput](#requestbody-content-applicationxwwwformurlencoded-schema-schemadictinput), [SchemaDict](#requestbody-content-applicationxwwwformurlencoded-schema-schemadict) | [SchemaDict](#requestbody-content-applicationxwwwformurlencoded-schema-schemadict) |

##### RequestBody content ApplicationXWwwFormUrlencoded Schema SchemaDictInput
```
type: typing.Mapping[str, schemas.INPUT_TYPES_ALL]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**param** | str | field1 |
**param2** | str | field2 |
**any_string_name** | dict, schemas.immutabledict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.FileIO | any string name can be used but the value must be the correct type | [optional]

##### RequestBody content ApplicationXWwwFormUrlencoded Schema SchemaDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
###### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**param** | str | field1 |
**param2** | str | field2 |
**kwargs** | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO | any string name can be used but the value must be the correct type | [optional] typed value is accessed with the get_additional_property_ method

###### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**param** | str | field1 |
**param2** | str | field2 |

###### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [SchemaDictInput](#requestbody-content-applicationxwwwformurlencoded-schema-schemadictinput), [SchemaDict](#requestbody-content-applicationxwwwformurlencoded-schema-schemadict) | [SchemaDict](#requestbody-content-applicationxwwwformurlencoded-schema-schemadict) | a constructor
get_additional_property_ | str | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO, schemas.Unset | provides type safety for additional properties

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

    # example passing only optional values
    body = {
        "param": "param_example",
        "param2": "param2_example",
    }
    try:
        # test json serialization of form data
        api_response = api_instance.json_form_data(
            body=body,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling FakeApi->json_form_data: %s\n" % e)
```

[[Back to top]](#top)
[[Back to FakeApi API]](../../apis/tags/fake_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)