# FakedeletecoffeeidDelete

public class FakedeletecoffeeidDelete

A class that contains necessary endpoint classes
- a class that calls the endpoint method using the http verb
- a class that calls the endpoint method using the operationId name
- class(es) to store the request inputs
- builder(s) to set the request input data

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [Delete](#delete)<br>The class that has a delete method to call the endpoint |
| interface | [DeleteCoffeeOperation](#deletecoffeeoperation)<br>The interface that has a deleteCoffee method to call the endpoint |
| static class | [DeleteRequest](#deleterequest)<br>The final request inputs class |
| static class | [DeleteNullableRequest](#deletenullablerequest)<br>The initial request inputs class |
| static class | [Delete0RequestBuilder](#delete0requestbuilder)<br>A builder for the request input class |
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
import org.openapijsonschematools.client.paths.fakedeletecoffeeid.delete.FakedeletecoffeeidDeletePathParameters;
import org.openapijsonschematools.client.servers.Server0;
import org.openapijsonschematools.client.servers.Server1;
import org.openapijsonschematools.client.servers.Server2;
import org.openapijsonschematools.client.paths.fakedeletecoffeeid.delete.responses.FakedeletecoffeeidDeleteCode200Response;
import org.openapijsonschematools.client.paths.fakedeletecoffeeid.delete.responses.FakedeletecoffeeidDeleteCodedefaultResponse;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.paths.fakedeletecoffeeid.FakedeletecoffeeidDelete;
import org.openapijsonschematools.client.paths.fakedeletecoffeeid.delete.FakedeletecoffeeidDeleteResponses;

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
FakedeletecoffeeidDelete.Delete apiClient = new FakedeletecoffeeidDelete.Delete(apiConfiguration, schemaConfiguration);


// Map validation
FakedeletecoffeeidDeletePathParameters.FakedeletecoffeeidDeletePathParametersMap pathParameters =
    FakedeletecoffeeidDeletePathParameters.FakedeletecoffeeidDeletePathParameters1.validate(
    new FakedeletecoffeeidDeletePathParameters.FakedeletecoffeeidDeletePathParametersMapBuilder()
        .id("a")

    .build(),
    schemaConfiguration
);

var request = new FakedeletecoffeeidDelete.DeleteRequestBuilder()
    .pathParameters(pathParameters)
    .build();

FakedeletecoffeeidDeleteResponses.EndpointResponse response;
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
if (response instanceof FakedeletecoffeeidDeleteResponses.EndpointFakedeletecoffeeidDeleteCode200Response castResponse) {
} else {
    FakedeletecoffeeidDeleteResponses.EndpointFakedeletecoffeeidDeleteCodedefaultResponse castResponse = (FakedeletecoffeeidDeleteResponses.EndpointFakedeletecoffeeidDeleteCodedefaultResponse) response;
}
```
### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Delete(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakedeletecoffeeidDeleteResponses.EndpointResponse](../../paths/fakedeletecoffeeid/delete/FakedeletecoffeeidDeleteResponses.md#endpointresponse) | delete([DeleteRequest](#deleterequest) request) |

## DeleteCoffeeOperation
public interface DeleteCoffeeOperation<br>

an interface that allows one to call the endpoint using a method named deleteCoffee by the operationId

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FakedeletecoffeeidDeleteResponses.EndpointResponse](../../paths/fakedeletecoffeeid/delete/FakedeletecoffeeidDeleteResponses.md#endpointresponse) | deleteCoffee([DeleteRequest](#deleterequest) request) |

## DeleteRequest
public static class DeleteRequest<br>

a class that stores the final request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [FakedeletecoffeeidDeletePathParameters.FakedeletecoffeeidDeletePathParametersMap](../../paths/fakedeletecoffeeid/delete/FakedeletecoffeeidDeletePathParameters.md#fakedeletecoffeeiddeletepathparametersmap) | pathParameters |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex<br>optional. Note: this will override the value in apiConfiguration |
| @Nullable Duration | timeout<br>optional. Note: this will override the value in apiConfiguration |

## DeleteNullableRequest
public static class DeleteNullableRequest<br>

a class that stores the initial request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [FakedeletecoffeeidDeletePathParameters.@Nullable FakedeletecoffeeidDeletePathParametersMap](../../paths/fakedeletecoffeeid/delete/FakedeletecoffeeidDeletePathParameters.md#fakedeletecoffeeiddeletepathparametersmap) | pathParameters |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex |
| @Nullable Duration | timeout |

## Delete0RequestBuilder
public static class Delete0RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Delete0RequestBuilder(Delete0RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [DeleteRequest](#deleterequest) | build()<br>Returns the request input used to call an endpoint method |
| [Delete0RequestBuilder](#delete0requestbuilder) | serverIndex([RootServerInfo.ServerIndex](../../RootServerInfo.md#serverindex) serverIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [Delete0RequestBuilder](#delete0requestbuilder) | timeout(Duration timeout)<br>sets the optional property. Note: this will override the value in apiConfiguration |

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
| [Delete0RequestBuilder](#delete0requestbuilder) | pathParameters([FakedeletecoffeeidDeletePathParametersFakedeletecoffeeidDeletePathParametersMap](../../paths/fakedeletecoffeeid/delete/FakedeletecoffeeidDeletePathParameters.md#fakedeletecoffeeiddeletepathparametersmap) pathParameters)<br>sets the property |

[[Back to top]](#top) [[Back to README]](../../../README.md)
