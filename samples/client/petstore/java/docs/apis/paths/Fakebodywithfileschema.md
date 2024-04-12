# Fakebodywithfileschema

public class Fakebodywithfileschema extends extends ApiClient implements
[FakebodywithfileschemaPut.PutOperation](../../paths/fakebodywithfileschema/FakebodywithfileschemaPut.md#putoperation)

an api client class which contains all the routes for path="/fake/body-with-file-schema"

## Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakebodywithfileschemaPutResponses.EndpointResponse](../../paths/fakebodywithfileschema/put/FakebodywithfileschemaPutResponses.md#endpointresponse) | [put](#put)([FakebodywithfileschemaPut.PutRequest](../../paths/fakebodywithfileschema/FakebodywithfileschemaPut.md#putrequest) request)<br>For this test, the body for this request much reference a schema named &#x60;File&#x60;. |

## Method Detail

### put
public [FakebodywithfileschemaPutResponses.EndpointResponse](../../paths/fakebodywithfileschema/put/FakebodywithfileschemaPutResponses.md#endpointresponse) put([FakebodywithfileschemaPut.PutRequest](../../paths/fakebodywithfileschema/FakebodywithfileschemaPut.md#putrequest) request)

For this test, the body for this request much reference a schema named &#x60;File&#x60;.

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
import org.openapijsonschematools.client.paths.fakebodywithfileschema.put.FakebodywithfileschemaPutRequestBody;
import org.openapijsonschematools.client.components.schemas.FileSchemaTestClass;
import org.openapijsonschematools.client.servers.RootServer0;
import org.openapijsonschematools.client.servers.RootServer1;
import org.openapijsonschematools.client.servers.RootServer2;
import org.openapijsonschematools.client.paths.fakebodywithfileschema.put.responses.FakebodywithfileschemaPutCode200Response;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.apis.paths.Fakebodywithfileschema;
import org.openapijsonschematools.client.paths.fakebodywithfileschema.put.FakebodywithfileschemaPutResponses;

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
Fakebodywithfileschema apiClient = new Fakebodywithfileschema(apiConfiguration, schemaConfiguration);


FileSchemaTestClass1BoxedMap requestBodyPayload =
    FileSchemaTestClass.FileSchemaTestClass1.validateAndBox(
    new FileSchemaTestClass.FileSchemaTestClassMapBuilder()
        .files(
            Arrays.asList(
            )
        )
    .build(),
    schemaConfiguration
);
FakebodywithfileschemaPut.SealedRequestBody requestBody = new FakebodywithfileschemaPut.ApplicationjsonRequestBody(requestBodyPayload);

var request = new FakebodywithfileschemaPut.PutRequestBuilder()
    .requestBody(requestBody)
    .build();

FakebodywithfileschemaPutResponses.EndpointResponse response;
try {
    response = apiClient.put(request);
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
FakebodywithfileschemaPutResponses.EndpointFakebodywithfileschemaPutCode200Response castResponse = (FakebodywithfileschemaPutResponses.EndpointFakebodywithfileschemaPutCode200Response) response;
```
[[Back to top]](#top) [[Back to README]](../../../README.md)
