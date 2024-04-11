# FakeclassnametestPatch

public class FakeclassnametestPatch

A class that contains necessary endpoint classes
- a class that calls the endpoint method using the http verb
- a class that calls the endpoint method using the operationId name
- class(es) to store the request inputs
- builder(s) to set the request input data

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [Patch](#patch)<br>The class that has a patch method to call the endpoint |
| interface | [ClassnameOperation](#classnameoperation)<br>The interface that has a classname method to call the endpoint |
| static class | [PatchRequest](#patchrequest)<br>The final request inputs class |
| static class | [PatchNullableRequest](#patchnullablerequest)<br>The initial request inputs class |
| static class | [Patch0RequestBuilder](#patch0requestbuilder)<br>A builder for the request input class |
| static class | [PatchRequestBuilder](#patchrequestbuilder)<br>A builder for the request input class |

## Patch
public static class Patch extends ApiClient.ApiClient1 implements PatchOperation<br>

a class that allows one to call the endpoint using a method named patch

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
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.fakeclassnametest.patch.FakeclassnametestPatchSecurityInfo;
import org.openapijsonschematools.client.paths.fakeclassnametest.patch.FakeclassnametestPatchRequestBody;
import org.openapijsonschematools.client.components.schemas.Client;
import org.openapijsonschematools.client.servers.Server0;
import org.openapijsonschematools.client.servers.Server1;
import org.openapijsonschematools.client.servers.Server2;
import org.openapijsonschematools.client.securityschemes.SecurityScheme;
import org.openapijsonschematools.client.components.securityschemes.ApiKeyQuery;
import org.openapijsonschematools.client.paths.fakeclassnametest.patch.responses.FakeclassnametestPatchCode200Response;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.paths.fakeclassnametest.FakeclassnametestPatch;
import org.openapijsonschematools.client.paths.fakeclassnametest.patch.FakeclassnametestPatchResponses;

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
    new ApiKeyQuery("someApiKey");
);
ApiConfiguration.SecurityIndexInfo securityIndexInfo = new ApiConfiguration.SecurityIndexInfoBuilder()
    .fakeclassnametestPatchSecurityRequirementObject0SecurityIndex(FakeclassnametestPatchSecurityRequirementObject0.SecurityIndex.SECURITY_0)
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
FakeclassnametestPatch.Patch apiClient = new FakeclassnametestPatch.Patch(apiConfiguration, schemaConfiguration);


Client1BoxedMap requestBodyPayload =
    Client.Client1.validateAndBox(
    new Client.ClientMapBuilder1()
        .client("a")

    .build(),
    schemaConfiguration
);
FakeclassnametestPatchRequestBody.SealedRequestBody requestBody = new FakeclassnametestPatchRequestBody.ApplicationjsonRequestBody(requestBodyPayload);

var request = new FakeclassnametestPatch.PatchRequestBuilder()
    .requestBody(requestBody)
    .build();

FakeclassnametestPatchResponses.EndpointResponse response;
try {
    response = apiClient.patch(request);
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
FakeclassnametestPatchResponses.EndpointFakeclassnametestPatchCode200Response castResponse = (FakeclassnametestPatchResponses.EndpointFakeclassnametestPatchCode200Response) response;
FakeclassnametestPatchCode200Response.ApplicationjsonResponseBody deserializedBody = (FakeclassnametestPatchCode200Response.ApplicationjsonResponseBody) castResponse.body;
// handle deserialized body here
```
### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Patch(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakeclassnametestPatchResponses.EndpointResponse](../../paths/fakeclassnametest/patch/FakeclassnametestPatchResponses.md#endpointresponse) | patch([PatchRequest](#patchrequest) request) |

## ClassnameOperation
public interface ClassnameOperation<br>

an interface that allows one to call the endpoint using a method named classname by the operationId

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakeclassnametestPatchResponses.EndpointResponse](../../paths/fakeclassnametest/patch/FakeclassnametestPatchResponses.md#endpointresponse) | classname([PatchRequest](#patchrequest) request) |

## PatchRequest
public static class PatchRequest<br>

a class that stores the final request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [FakeclassnametestPatchRequestBody.SealedRequestBody](../../paths/fakeclassnametest/patch/FakeclassnametestPatchRequestBody.md#sealedrequestbody) | requestBody |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex<br>optional. Note: this will override the value in apiConfiguration |
| [FakeclassnametestPatchSecurityInfo.@Nullable SecurityIndex](../../paths/fakeclassnametest/patch/FakeclassnametestPatchSecurityInfo.md#securityindex) | securityIndex<br>optional. Note: this will override the value in apiConfiguration |
| @Nullable Duration | timeout<br>optional. Note: this will override the value in apiConfiguration |

## PatchNullableRequest
public static class PatchNullableRequest<br>

a class that stores the initial request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [FakeclassnametestPatchRequestBody.@Nullable SealedRequestBody](../../paths/fakeclassnametest/patch/FakeclassnametestPatchRequestBody.md#sealedrequestbody) | requestBody |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex |
| [FakeclassnametestPatchSecurityInfo.@Nullable SecurityIndex](../../paths/fakeclassnametest/patch/FakeclassnametestPatchSecurityInfo.md#securityindex) | securityIndex |
| @Nullable Duration | timeout |

## Patch0RequestBuilder
public static class Patch0RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Patch0RequestBuilder(Patch0RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PatchRequest](#patchrequest) | build()<br>Returns the request input used to call an endpoint method |
| [Patch0RequestBuilder](#patch0requestbuilder) | serverIndex([RootServerInfo.ServerIndex](../../RootServerInfo.md#serverindex) serverIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [Patch0RequestBuilder](#patch0requestbuilder) | securityIndex([FakeclassnametestPatchSecurityInfo.SecurityIndex](../../paths/fakeclassnametest/patch/FakeclassnametestPatchSecurityInfo.md#securityindex) securityIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [Patch0RequestBuilder](#patch0requestbuilder) | timeout(Duration timeout)<br>sets the optional property. Note: this will override the value in apiConfiguration |

## PatchRequestBuilder
public static class PatchRequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatchRequestBuilder()<br>Creates a builder that contains null for all parameters |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [Patch0RequestBuilder](#patch0requestbuilder) | requestBody([FakeclassnametestPatchRequestBody.SealedRequestBody](../../paths/fakeclassnametest/patch/FakeclassnametestPatchRequestBody.md#sealedrequestbody) requestBody)<br>sets the property |

[[Back to top]](#top) [[Back to README]](../../../README.md)
