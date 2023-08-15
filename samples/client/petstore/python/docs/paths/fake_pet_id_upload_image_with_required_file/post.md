petstore_api.paths.fake_pet_id_upload_image_with_required_file.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| upload_file_with_required_file | [PetApi](../../apis/tags/pet_api.md) | This api is only for tag=pet |
| post | ApiForPost | This api is only for this endpoint |
| post | FakePetIdUploadImageWithRequiredFile | This api is only for path=/fake/{petId}/uploadImageWithRequiredFile |

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
| Summary | uploads an image (required) |
| Path | "/fake/{petId}/uploadImageWithRequiredFile" |
| HTTP Method | post |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#requestbody) | typing.Union[[schema.SchemaDictInput](../../paths/fake_pet_id_upload_image_with_required_file/post/request_body/content/multipart_form_data/schema.md#schemadictinput), [schema.SchemaDict](../../paths/fake_pet_id_upload_image_with_required_file/post/request_body/content/multipart_form_data/schema.md#schemadict), schemas.Unset] | optional, default is unset |
[path_params](#path_params) | [PathParametersDictInput](#pathparameters-pathparametersdictinput), [PathParametersDict](#pathparameters-pathparametersdict) | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body. value must be one of ['multipart/form-data']
accept_content_types | typing.Tuple[str] | default is ("application/json", ) | Tells the server the content type(s) that are accepted by the client
security_index | typing.Optional[int] | default is None | Allows one to select a different [security](#security) definition. If not None, must be one of [0]
server_index | typing.Optional[int] | default is None | Allows one to select a different [server](#servers). If not None, must be one of [0, 1, 2]
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_response.ApiResponseWithoutDeserialization will be returned

### RequestBody

#### Content Type To Schema
Content-Type | Schema
------------ | -------
"multipart/form-data" | [content.multipart_form_data.Schema](#requestbody-content-multipartformdata-schema)

#### RequestBody content MultipartFormData Schema
petstore_api.paths.fake_pet_id_upload_image_with_required_file.post.request_body.content.multipart_form_data.schema
```
type: schemas.Schema
```

##### validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[SchemaDictInput](#requestbody-content-multipartformdata-schema-schemadictinput), [SchemaDict](#requestbody-content-multipartformdata-schema-schemadict) | [SchemaDict](#requestbody-content-multipartformdata-schema-schemadict) |

##### RequestBody content MultipartFormData Schema SchemaDictInput
```
type: typing.Mapping[str, schemas.INPUT_TYPES_ALL]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**requiredFile** | bytes, io.FileIO, io.BufferedReader | file to upload |
**additionalMetadata** | str | Additional data to pass to server | [optional]
**any_string_name** | dict, schemas.immutabledict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.FileIO | any string name can be used but the value must be the correct type | [optional]

##### RequestBody content MultipartFormData Schema SchemaDict
```
base class: schemas.immutabledict[str, str]

```
###### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**requiredFile** | bytes, io.FileIO, io.BufferedReader | file to upload |
**additionalMetadata** | str, schemas.Unset | Additional data to pass to server | [optional]
**kwargs** | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO | any string name can be used but the value must be the correct type | [optional] typed value is accessed with the get_additional_property_ method

###### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**requiredFile** | bytes, io.FileIO | file to upload |
**additionalMetadata** | str, schemas.Unset | Additional data to pass to server | [optional]

###### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [SchemaDictInput](#requestbody-content-multipartformdata-schema-schemadictinput), [SchemaDict](#requestbody-content-multipartformdata-schema-schemadict) | [SchemaDict](#requestbody-content-multipartformdata-schema-schemadict) | a constructor
get_additional_property_ | str | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO, schemas.Unset }} | provides type safety for additional properties
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
**petId** | int |  |

#### PathParameters PathParametersDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
##### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**petId** | int |  |

##### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**petId** | int |  |

##### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [PathParametersDictInput](#pathparameters-pathparametersdictinput), [PathParametersDict](#pathparameters-pathparametersdict) | [PathParametersDict](#pathparameters-pathparametersdict) | a constructor

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_response.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ResponseFor200.ApiResponse](#responsefor200-apiresponse) | successful operation

## ResponseFor200

### Description
successful operation

### ResponseFor200 ApiResponse
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
[body](#responsefor200-body) | [api_response.ApiResponseDict](../../components/schema/api_response.md#apiresponsedict) |  |
headers | Unset | headers were not defined |

### ResponseFor200 Body
Content-Type | Schema
------------ | -------
"application/json" | [content.application_json.Schema](#responsefor200-content-applicationjson-schema)

### Body Details
#### ResponseFor200 content ApplicationJson Schema
petstore_api.paths.fake_pet_id_upload_image_with_required_file.post.responses.response_200.content.application_json.schema
```
type: schemas.Schema
```

##### Ref Schema Info
Ref Schema | Input Type | Output Type
---------- | ---------- | -----------
[**api_response.ApiResponse**](../../components/schema/api_response.md) | [api_response.ApiResponseDictInput](../../components/schema/api_response.md#apiresponsedictinput), [api_response.ApiResponseDict](../../components/schema/api_response.md#apiresponsedict) | [api_response.ApiResponseDict](../../components/schema/api_response.md#apiresponsedict)

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
| 0       | ["petstore_auth"](../../components/security_schemes/security_scheme_petstore_auth.md) [write:pets, read:pets]<br> |

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
from petstore_api.apis.tags import pet_api
from petstore_api.paths.fake_pet_id_upload_image_with_required_file.post import operation
from pprint import pprint
# security_index 0
from petstore_api.components.security_schemes import security_scheme_petstore_auth

# security_scheme_info for security_index 0
security_scheme_info: api_configuration.SecuritySchemeInfo = {
    "petstore_auth": security_scheme_petstore_auth.PetstoreAuth(
    ),
}

used_configuration = api_configuration.ApiConfiguration(
    security_scheme_info=security_scheme_info,
)
# Enter a context with an instance of the API client
with petstore_api.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = pet_api.PetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params: operation.PathParametersDictInput = {
        'petId': 1,
    }
    try:
        # uploads an image (required)
        api_response = api_instance.upload_file_with_required_file(
            path_params=path_params,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->upload_file_with_required_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'petId': 1,
    }
    body = {
        "additional_metadata": "additional_metadata_example",
        "required_file": open('/path/to/file', 'rb'),
    }
    try:
        # uploads an image (required)
        api_response = api_instance.upload_file_with_required_file(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except petstore_api.ApiException as e:
        print("Exception when calling PetApi->upload_file_with_required_file: %s\n" % e)
```

[[Back to top]](#top)
[[Back to PetApi API]](../../apis/tags/pet_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)