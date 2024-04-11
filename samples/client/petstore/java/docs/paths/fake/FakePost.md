# FakePost

public class FakePost

A class that contains necessary endpoint classes
- a class that calls the endpoint method using the http verb
- a class that calls the endpoint method using the operationId name
- class(es) to store the request inputs
- builder(s) to set the request input data

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [Post](#post)<br>The class that has a post method to call the endpoint |
| interface | [EndpointParametersOperation](#endpointparametersoperation)<br>The interface that has a endpointParameters method to call the endpoint |
| static class | [PostRequest](#postrequest)<br>The request inputs class |
| static class | [PostRequestBuilder](#postrequestbuilder)<br>A builder for the request input class |

## Post
public static class Post extends ApiClient.ApiClient1 implements PostOperation<br>

a class that allows one to call the endpoint using a method named post

### Code Sample
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
import org.openapijsonschematools.client.paths.fake.post.FakePostRequestBody;
import org.openapijsonschematools.client.paths.fake.post.requestbody.content.applicationxwwwformurlencoded.ApplicationxwwwformurlencodedSchema;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.fake.post.FakePostSecurityInfo;
import org.openapijsonschematools.client.servers.Server0;
import org.openapijsonschematools.client.servers.Server1;
import org.openapijsonschematools.client.servers.Server2;
import org.openapijsonschematools.client.securityschemes.SecurityScheme;
import org.openapijsonschematools.client.components.securityschemes.HttpBasicTest;
import org.openapijsonschematools.client.paths.fake.post.responses.FakePostCode200Response;
import org.openapijsonschematools.client.paths.fake.post.responses.FakePostCode404Response;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.paths.fake.FakePost;
import org.openapijsonschematools.client.paths.fake.post.FakePostResponses;

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
List<SecurityScheme> securitySchemes = new ArrayList();
securitySchemes.add(
    new HttpBasicTest("someUserId", "somePassword");
);
ApiConfiguration.SecurityIndexInfo securityIndexInfo = new ApiConfiguration.SecurityIndexInfoBuilder()
    .fakePostSecurityRequirementObject0SecurityIndex(FakePostSecurityRequirementObject0.SecurityIndex.SECURITY_0)
    .build();
Duration timeout = Duration.ofSeconds(1L);
ApiConfiguration apiConfiguration = new ApiConfiguration(
    serverInfo
    serverIndexInfo,
    securitySchemes,
    securityIndexInfo,
    timeout
);
SchemaConfiguration schemaConfiguration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());
FakePost.Post apiClient = new FakePost.Post(apiConfiguration, schemaConfiguration);


var request = new FakePost.PostRequestBuilder().build();

FakePostResponses.EndpointResponse response;
try {
    response = apiClient.post(request);
} catch (FakePostCode404Response.ResponseApiException e) {
    // server returned an error response defined in the openapi document
    throw e;
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
FakePostResponses.EndpointFakePostCode200Response castResponse = (FakePostResponses.EndpointFakePostCode200Response) response;
```
### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Post(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakePostResponses.EndpointResponse](../../paths/fake/post/FakePostResponses.md#endpointresponse) | post([PostRequest](#postrequest) request) |

## EndpointParametersOperation
public interface EndpointParametersOperation<br>

an interface that allows one to call the endpoint using a method named endpointParameters by the operationId

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakePostResponses.EndpointResponse](../../paths/fake/post/FakePostResponses.md#endpointresponse) | endpointParameters([PostRequest](#postrequest) request) |

## PostRequest
public static class PostRequest<br>

a class that stores the final request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [FakePostRequestBody.@Nullable SealedRequestBody](../../paths/fake/post/FakePostRequestBody.md#sealedrequestbody) | requestBody<br>optional |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex<br>optional. Note: this will override the value in apiConfiguration |
| [FakePostSecurityInfo.@Nullable SecurityIndex](../../paths/fake/post/FakePostSecurityInfo.md#securityindex) | securityIndex<br>optional. Note: this will override the value in apiConfiguration |
| @Nullable Duration | timeout<br>optional. Note: this will override the value in apiConfiguration |

## PostRequestBuilder
public static class PostRequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PostRequestBuilder()<br>Creates a builder that contains null for all parameters |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PostRequest](#postrequest) | build()<br>Returns the request input used to call an endpoint method |
| [PostRequestBuilder](#postrequestbuilder) | requestBody([FakePostRequestBody.SealedRequestBody](../../paths/fake/post/FakePostRequestBody.md#sealedrequestbody) requestBody)<br>sets the optional property |
| [PostRequestBuilder](#postrequestbuilder) | serverIndex([RootServerInfo.ServerIndex](../../RootServerInfo.md#serverindex) serverIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [PostRequestBuilder](#postrequestbuilder) | securityIndex([FakePostSecurityInfo.SecurityIndex](../../paths/fake/post/FakePostSecurityInfo.md#securityindex) securityIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [PostRequestBuilder](#postrequestbuilder) | timeout(Duration timeout)<br>sets the optional property. Note: this will override the value in apiConfiguration |

[[Back to top]](#top) [[Back to README]](../../../README.md)
