# UserusernamePut

public class UserusernamePut

A class that contains necessary endpoint classes
- a class that calls the endpoint method using the http verb
- a class that calls the endpoint method using the operationId name
- class(es) to store the request inputs
- builder(s) to set the request input data

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [Put](#put)<br>The class that has a put method to call the endpoint |
| interface | [UpdateUserOperation](#updateuseroperation)<br>The interface that has a updateUser method to call the endpoint |
| static class | [PutRequest](#putrequest)<br>The final request inputs class |
| static class | [PutNullableRequest](#putnullablerequest)<br>The initial request inputs class |
| static class | [Put00RequestBuilder](#put00requestbuilder)<br>A builder for the request input class |
| static class | [Put01RequestBuilder](#put01requestbuilder)<br>A builder for the request input class |
| static class | [Put10RequestBuilder](#put10requestbuilder)<br>A builder for the request input class |
| static class | [PutRequestBuilder](#putrequestbuilder)<br>A builder for the request input class |

## Put
public static class Put extends ApiClient.ApiClient1 implements PutOperation<br>

a class that allows one to call the endpoint using a method named put

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
import org.openapijsonschematools.client.paths.userusername.put.UserusernamePutRequestBody;
import org.openapijsonschematools.client.components.schemas.User;
import org.openapijsonschematools.client.paths.userusername.put.UserusernamePutPathParameters;
import org.openapijsonschematools.client.servers.RootServer0;
import org.openapijsonschematools.client.servers.RootServer1;
import org.openapijsonschematools.client.servers.RootServer2;
import org.openapijsonschematools.client.paths.userusername.put.responses.UserusernamePutCode400Response;
import org.openapijsonschematools.client.paths.userusername.put.responses.UserusernamePutCode404Response;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.paths.userusername.UserusernamePut;
import org.openapijsonschematools.client.paths.userusername.put.UserusernamePutResponses;

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
UserusernamePut.Put apiClient = new UserusernamePut.Put(apiConfiguration, schemaConfiguration);


User1BoxedMap requestBodyPayload =
    User.User1.validateAndBox(
    new User.UserMapBuilder()
        .id(1L)

        .username("a")

        .firstName("a")

        .lastName("a")

        .email("a")

        .password("a")

        .phone("a")

        .userStatus(1)

        .objectWithNoDeclaredPropsNullable(null)

    .build(),
    schemaConfiguration
);
UserusernamePut.SealedRequestBody requestBody = new UserusernamePut.ApplicationjsonRequestBody(requestBodyPayload);

// Map validation
UserusernamePutPathParameters.PathParametersMap pathParameters =
    UserusernamePutPathParameters.UserusernamePutPathParameters1.validate(
    new UserusernamePutPathParameters.PathParametersMapBuilder()
        .username("a")

    .build(),
    schemaConfiguration
);

var request = new UserusernamePut.PutRequestBuilder()
    .requestBody(requestBody)
    .pathParameters(pathParameters)
    .build();

Void response;
try {
    response = apiClient.put(request);
} catch (UserusernamePutCode400Response.ResponseApiException | UserusernamePutCode404Response.ResponseApiException e) {
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
```
### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Put(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | put([PutRequest](#putrequest) request) |

## UpdateUserOperation
public interface UpdateUserOperation<br>

an interface that allows one to call the endpoint using a method named updateUser by the operationId

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | updateUser([PutRequest](#putrequest) request) |

## PutRequest
public static class PutRequest<br>

a class that stores the final request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [UserusernamePutRequestBody.SealedRequestBody](../../paths/userusername/put/UserusernamePutRequestBody.md#sealedrequestbody) | requestBody |
| [UserusernamePutPathParameters.PathParametersMap](../../paths/userusername/put/UserusernamePutPathParameters.md#pathparametersmap) | pathParameters |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex<br>optional. Note: this will override the value in apiConfiguration |
| @Nullable Duration | timeout<br>optional. Note: this will override the value in apiConfiguration |

## PutNullableRequest
public static class PutNullableRequest<br>

a class that stores the initial request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [UserusernamePutRequestBody.@Nullable SealedRequestBody](../../paths/userusername/put/UserusernamePutRequestBody.md#sealedrequestbody) | requestBody |
| [UserusernamePutPathParameters.@Nullable PathParametersMap](../../paths/userusername/put/UserusernamePutPathParameters.md#pathparametersmap) | pathParameters |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex |
| @Nullable Duration | timeout |

## Put00RequestBuilder
public static class Put00RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Put00RequestBuilder(Put00RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PutRequest](#putrequest) | build()<br>Returns the request input used to call an endpoint method |
| [Put00RequestBuilder](#put00requestbuilder) | serverIndex([RootServerInfo.ServerIndex](../../RootServerInfo.md#serverindex) serverIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [Put00RequestBuilder](#put00requestbuilder) | timeout(Duration timeout)<br>sets the optional property. Note: this will override the value in apiConfiguration |

## Put01RequestBuilder
public static class Put01RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Put01RequestBuilder(Put01RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [Put00RequestBuilder](#put00requestbuilder) | pathParameters([UserusernamePutPathParametersPathParametersMap](../../paths/userusername/put/UserusernamePutPathParameters.md#pathparametersmap) pathParameters)<br>sets the property |

## Put10RequestBuilder
public static class Put10RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Put10RequestBuilder(Put10RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [Put00RequestBuilder](#put00requestbuilder) | requestBody([UserusernamePutRequestBody.SealedRequestBody](../../paths/userusername/put/UserusernamePutRequestBody.md#sealedrequestbody) requestBody)<br>sets the property |

## PutRequestBuilder
public static class PutRequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PutRequestBuilder()<br>Creates a builder that contains null for all parameters |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [Put01RequestBuilder](#put01requestbuilder) | requestBody([UserusernamePutRequestBody.SealedRequestBody](../../paths/userusername/put/UserusernamePutRequestBody.md#sealedrequestbody) requestBody)<br>sets the property |
| [Put10RequestBuilder](#put10requestbuilder) | pathParameters([UserusernamePutPathParametersPathParametersMap](../../paths/userusername/put/UserusernamePutPathParameters.md#pathparametersmap) pathParameters)<br>sets the property |

[[Back to top]](#top) [[Back to README]](../../../README.md)
