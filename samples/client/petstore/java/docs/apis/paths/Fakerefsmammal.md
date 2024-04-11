# Fakerefsmammal

public class Fakerefsmammal extends extends ApiClient implements
[FakerefsmammalPost.PostOperation](../../paths/fakerefsmammal/FakerefsmammalPost.md#postoperation)

an api client class which contains all the routes for path=""

## Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakerefsmammalPostResponses.EndpointResponse](../../paths/fakerefsmammal/post/FakerefsmammalPostResponses.md#endpointresponse) | [post](#post)([FakerefsmammalPost.PostRequest](../../paths/fakerefsmammal/FakerefsmammalPost.md#postrequest) request)<br>Test serialization of mammals |

## Method Detail

### post
public [FakerefsmammalPostResponses.EndpointResponse](../../paths/fakerefsmammal/post/FakerefsmammalPostResponses.md#endpointresponse) post([FakerefsmammalPost.PostRequest](../../paths/fakerefsmammal/FakerefsmammalPost.md#postrequest) request)

Test serialization of mammals

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
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.fakerefsmammal.post.FakerefsmammalPostRequestBody;
import org.openapijsonschematools.client.components.schemas.Mammal;
import org.openapijsonschematools.client.servers.Server0;
import org.openapijsonschematools.client.servers.Server1;
import org.openapijsonschematools.client.servers.Server2;
import org.openapijsonschematools.client.paths.fakerefsmammal.post.responses.FakerefsmammalPostCode200Response;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.apis.paths.Fakerefsmammal;
import org.openapijsonschematools.client.paths.fakerefsmammal.post.FakerefsmammalPostResponses;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

// if you want to use a server that is not SERVER_0 pass it in here and change the ServerIndex input below
ApiConfiguration.ServerInfo serverInfo = new ApiConfiguration.ServerInfoBuilder()
    .rootServerInfo(
        new RootServerInfo.RootServerInfoBuilder()
            .server0(new Server0())
            .build()
    )
    .build();
ApiConfiguration.ServerIndexInfo serverIndexInfo = new ApiConfiguration.ServerIndexInfoBuilder()
    .rootServerInfoServerIndex(RootServerInfo.ServerIndex.SERVER_0)
    .build();
Duration timeout = Duration.ofSeconds(1L);
ApiConfiguration apiConfiguration = new ApiConfiguration(
    serverInfo
    serverIndexInfo,
    timeout
);
SchemaConfiguration schemaConfiguration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());
Fakerefsmammal apiClient = new Fakerefsmammal(apiConfiguration, schemaConfiguration);

FakerefsmammalPost.SealedRequestBody requestBody = new FakerefsmammalPost.ApplicationjsonRequestBody(requestBodyPayload);

var request = new FakerefsmammalPost.PostRequestBuilder()
    .requestBody(requestBody)
    .build();

FakerefsmammalPostResponses.EndpointResponse response;
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
FakerefsmammalPostResponses.EndpointFakerefsmammalPostCode200Response castResponse = (FakerefsmammalPostResponses.EndpointFakerefsmammalPostCode200Response) response;
FakerefsmammalPostCode200Response.ApplicationjsonResponseBody deserializedBody = (FakerefsmammalPostCode200Response.ApplicationjsonResponseBody) castResponse.body;
// handle deserialized body here
```
[[Back to top]](#top) [[Back to README]](../../../README.md)
