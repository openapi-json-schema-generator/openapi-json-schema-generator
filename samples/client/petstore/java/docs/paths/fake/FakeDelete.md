# FakeDelete

public class FakeDelete

A class that contains necessary endpoint classes
- a class that calls the endpoint method using the http verb
- a class that calls the endpoint method using the operationId name
- class(es) to store the request inputs
- builder(s) to set the request input data

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [Delete](#delete)<br>The class that has a delete method to call the endpoint |
| interface | [GroupParametersOperation](#groupparametersoperation)<br>The interface that has a groupParameters method to call the endpoint |
| static class | [DeleteRequest](#deleterequest)<br>The final request inputs class |
| static class | [DeleteNullableRequest](#deletenullablerequest)<br>The initial request inputs class |
| static class | [Delete00RequestBuilder](#delete00requestbuilder)<br>A builder for the request input class |
| static class | [Delete01RequestBuilder](#delete01requestbuilder)<br>A builder for the request input class |
| static class | [Delete10RequestBuilder](#delete10requestbuilder)<br>A builder for the request input class |
| static class | [DeleteRequestBuilder](#deleterequestbuilder)<br>A builder for the request input class |

## Delete
public static class Delete extends ApiClient.ApiClient1 implements DeleteOperation<br>

a class that allows one to call the endpoint using a method named delete

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
import org.openapijsonschematools.client.paths.fake.delete.FakeDeleteSecurityInfo;
import org.openapijsonschematools.client.paths.fake.delete.FakeDeleteHeaderParameters;
import org.openapijsonschematools.client.paths.fake.delete.FakeDeleteQueryParameters;
import org.openapijsonschematools.client.servers.Server0;
import org.openapijsonschematools.client.servers.Server1;
import org.openapijsonschematools.client.servers.Server2;
import org.openapijsonschematools.client.securityschemes.SecurityScheme;
import org.openapijsonschematools.client.components.securityschemes.BearerTest;
import org.openapijsonschematools.client.paths.fake.delete.responses.FakeDeleteCode200Response;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.paths.fake.FakeDelete;
import org.openapijsonschematools.client.paths.fake.delete.FakeDeleteResponses;

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
    new BearerTest("someAccessToken");
);
ApiConfiguration.SecurityIndexInfo securityIndexInfo = new ApiConfiguration.SecurityIndexInfoBuilder()
    .fakeDeleteSecurityRequirementObject0SecurityIndex(FakeDeleteSecurityRequirementObject0.SecurityIndex.SECURITY_0)
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
FakeDelete.Delete apiClient = new FakeDelete.Delete(apiConfiguration, schemaConfiguration);


// Map validation
FakeDeleteHeaderParameters.FakeDeleteHeaderParametersMap headerParameters =
    FakeDeleteHeaderParameters.FakeDeleteHeaderParameters1.validate(
    new FakeDeleteHeaderParameters.FakeDeleteHeaderParametersMapBuilder()
        .required_boolean_group("true")

        .boolean_group("true")

    .build(),
    schemaConfiguration
);

// Map validation
FakeDeleteQueryParameters.FakeDeleteQueryParametersMap queryParameters =
    FakeDeleteQueryParameters.FakeDeleteQueryParameters1.validate(
    new FakeDeleteQueryParameters.FakeDeleteQueryParametersMapBuilder()
        .required_int64_group(1L)

        .required_string_group("a")

        .int64_group(1L)

        .string_group("a")

    .build(),
    schemaConfiguration
);

var request = new FakeDelete.DeleteRequestBuilder()
    .headerParameters(headerParameters)
    .queryParameters(queryParameters)
    .build();

FakeDeleteResponses.EndpointResponse response;
try {
    response = apiClient.delete(request);
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
FakeDeleteResponses.EndpointFakeDeleteCode200Response castResponse = (FakeDeleteResponses.EndpointFakeDeleteCode200Response) response;
```
### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Delete(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakeDeleteResponses.EndpointResponse](../../paths/fake/delete/FakeDeleteResponses.md#endpointresponse) | delete([DeleteRequest](#deleterequest) request) |

## GroupParametersOperation
public interface GroupParametersOperation<br>

an interface that allows one to call the endpoint using a method named groupParameters by the operationId

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakeDeleteResponses.EndpointResponse](../../paths/fake/delete/FakeDeleteResponses.md#endpointresponse) | groupParameters([DeleteRequest](#deleterequest) request) |

## DeleteRequest
public static class DeleteRequest<br>

a class that stores the final request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [FakeDeleteHeaderParameters.FakeDeleteHeaderParametersMap](../../paths/fake/delete/FakeDeleteHeaderParameters.md#fakedeleteheaderparametersmap) | headerParameters |
| [FakeDeleteQueryParameters.FakeDeleteQueryParametersMap](../../paths/fake/delete/FakeDeleteQueryParameters.md#fakedeletequeryparametersmap) | queryParameters |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex<br>optional. Note: this will override the value in apiConfiguration |
| [FakeDeleteSecurityInfo.@Nullable SecurityIndex](../../paths/fake/delete/FakeDeleteSecurityInfo.md#securityindex) | securityIndex<br>optional. Note: this will override the value in apiConfiguration |
| @Nullable Duration | timeout<br>optional. Note: this will override the value in apiConfiguration |

## DeleteNullableRequest
public static class DeleteNullableRequest<br>

a class that stores the initial request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [FakeDeleteHeaderParameters.@Nullable FakeDeleteHeaderParametersMap](../../paths/fake/delete/FakeDeleteHeaderParameters.md#fakedeleteheaderparametersmap) | headerParameters |
| [FakeDeleteQueryParameters.@Nullable FakeDeleteQueryParametersMap](../../paths/fake/delete/FakeDeleteQueryParameters.md#fakedeletequeryparametersmap) | queryParameters |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex |
| [FakeDeleteSecurityInfo.@Nullable SecurityIndex](../../paths/fake/delete/FakeDeleteSecurityInfo.md#securityindex) | securityIndex |
| @Nullable Duration | timeout |

## Delete00RequestBuilder
public static class Delete00RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Delete00RequestBuilder(Delete00RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [DeleteRequest](#deleterequest) | build()<br>Returns the request input used to call an endpoint method |
| [Delete00RequestBuilder](#delete00requestbuilder) | serverIndex([RootServerInfo.ServerIndex](../../RootServerInfo.md#serverindex) serverIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [Delete00RequestBuilder](#delete00requestbuilder) | securityIndex([FakeDeleteSecurityInfo.SecurityIndex](../../paths/fake/delete/FakeDeleteSecurityInfo.md#securityindex) securityIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [Delete00RequestBuilder](#delete00requestbuilder) | timeout(Duration timeout)<br>sets the optional property. Note: this will override the value in apiConfiguration |

## Delete01RequestBuilder
public static class Delete01RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Delete01RequestBuilder(Delete01RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [Delete00RequestBuilder](#delete00requestbuilder) | queryParameters([FakeDeleteQueryParametersFakeDeleteQueryParametersMap](../../paths/fake/delete/FakeDeleteQueryParameters.md#fakedeletequeryparametersmap) queryParameters)<br>sets the property |

## Delete10RequestBuilder
public static class Delete10RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Delete10RequestBuilder(Delete10RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [Delete00RequestBuilder](#delete00requestbuilder) | headerParameters([FakeDeleteHeaderParametersFakeDeleteHeaderParametersMap](../../paths/fake/delete/FakeDeleteHeaderParameters.md#fakedeleteheaderparametersmap) headerParameters)<br>sets the property |

## DeleteRequestBuilder
public static class DeleteRequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DeleteRequestBuilder()<br>Creates a builder that contains null for all parameters |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [Delete01RequestBuilder](#delete01requestbuilder) | headerParameters([FakeDeleteHeaderParametersFakeDeleteHeaderParametersMap](../../paths/fake/delete/FakeDeleteHeaderParameters.md#fakedeleteheaderparametersmap) headerParameters)<br>sets the property |
| [Delete10RequestBuilder](#delete10requestbuilder) | queryParameters([FakeDeleteQueryParametersFakeDeleteQueryParametersMap](../../paths/fake/delete/FakeDeleteQueryParameters.md#fakedeletequeryparametersmap) queryParameters)<br>sets the property |

[[Back to top]](#top) [[Back to README]](../../../README.md)
