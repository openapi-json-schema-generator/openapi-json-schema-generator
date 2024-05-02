# Fakeuploadfile

public class Fakeuploadfile extends extends ApiClient implements
[FakeuploadfilePost.PostOperation](../../paths/fakeuploadfile/FakeuploadfilePost.md#postoperation)

an api client class which contains all the routes for path="/fake/uploadFile"

## Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakeuploadfilePostResponses.EndpointResponse](../../paths/fakeuploadfile/post/FakeuploadfilePostResponses.md#endpointresponse) | [post](#post)([FakeuploadfilePost.PostRequest](../../paths/fakeuploadfile/FakeuploadfilePost.md#postrequest) request)<br> |

## Method Detail

### post
public [FakeuploadfilePostResponses.EndpointResponse](../../paths/fakeuploadfile/post/FakeuploadfilePostResponses.md#endpointresponse) post([FakeuploadfilePost.PostRequest](../../paths/fakeuploadfile/FakeuploadfilePost.md#postrequest) request)



**Parameters:**<br>
request - the input request

**Returns:**<br>
the deserialized response

**Throws:**<br>
IOException, InterruptedException - an exception happened when making the request<br>
ValidationException - the returned response body or header values do not conform the the schema validation requirements<br>
NotImplementedException - the request body serialization or deserialization has not yet been implemented<br>
                          or the header content type deserialization has not yet been implemented for this contentType<br>
ApiException - server returned a response/contentType not defined in the openapi document<br>

#### Code Sample
```
import org.openapijsonschematools.client.configurations.ApiConfiguration;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.NotImplementedException;
import org.openapijsonschematools.client.exceptions.ApiException;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.paths.fakeuploadfile.post.FakeuploadfilePostRequestBody;
import org.openapijsonschematools.client.paths.fakeuploadfile.post.requestbody.content.multipartformdata.MultipartformdataSchema;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.servers.RootServer0;
import org.openapijsonschematools.client.servers.RootServer1;
import org.openapijsonschematools.client.servers.RootServer2;
import org.openapijsonschematools.client.paths.fakeuploadfile.post.responses.FakeuploadfilePostCode200Response;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.apis.paths.Fakeuploadfile;
import org.openapijsonschematools.client.paths.fakeuploadfile.post.FakeuploadfilePostResponses;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.AbstractMap;

// if you want to use a server that is not SERVER_0 pass it in here and change the ServerIndex input below
ApiConfiguration.ServerInfo serverInfo = new ApiConfiguration.ServerInfoBuilder()
    .rootServerInfo(
        new RootServerInfo.RootServerInfoBuilder()
            .rootServer0(new RootServer0())
            .build()
    )
    .build();
ApiConfiguration.ServerIndexInfo serverIndexInfo = new ApiConfiguration.ServerIndexInfoBuilder()
    .rootServerInfoServerIndex(RootServerInfo.ServerIndex.SERVER_0)
    .build();
Duration timeout = Duration.ofSeconds(1L);
Map<String, List<String>> defaultHeaders = Map.of("User-Agent", List.of("OpenAPI-JSON-Schema-Generator/1.0.0/java"));
ApiConfiguration apiConfiguration = new ApiConfiguration(
    serverInfo
    serverIndexInfo,
    timeout,
    defaultHeaders
);
SchemaConfiguration schemaConfiguration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());
Fakeuploadfile apiClient = new Fakeuploadfile(apiConfiguration, schemaConfiguration);


var request = new FakeuploadfilePost.PostRequestBuilder().build();

FakeuploadfilePostResponses.EndpointResponse response;
try {
    response = apiClient.post(request);
} catch (ApiException e) {
    // server returned a response/contentType not defined in the openapi document
    throw e;
} catch (ValidationException e) {
    // the returned response body or header values do not conform the the schema validation requirements
    throw e;
} catch (IOException | InterruptedException e) {
    // an exception happened when making the request
    throw e;
} catch (NotImplementedException e) {
    // the request body serialization or deserialization has not yet been implemented
    // or the header content type deserialization has not yet been implemented for this contentType
    throw e;
}
FakeuploadfilePostResponses.EndpointFakeuploadfilePostCode200Response castResponse = (FakeuploadfilePostResponses.EndpointFakeuploadfilePostCode200Response) response;
FakeuploadfilePostCode200Response.ApplicationjsonResponseBody deserializedBody = (FakeuploadfilePostCode200Response.ApplicationjsonResponseBody) castResponse.body;
// handle deserialized body here
```
[[Back to top]](#top) [[Back to README]](../../../README.md)
