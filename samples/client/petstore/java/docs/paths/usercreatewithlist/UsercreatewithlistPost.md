# UsercreatewithlistPost

public class UsercreatewithlistPost

A class that contains necessary endpoint classes
- a class that calls the endpoint method using the http verb
- a class that calls the endpoint method using the operationId name
- class(es) to store the request inputs
- builder(s) to set the request input data

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [Post](#post)<br>The class that has a post method to call the endpoint |
| interface | [CreateUsersWithListInputOperation](#createuserswithlistinputoperation)<br>The interface that has a createUsersWithListInput method to call the endpoint |
| static class | [PostRequest](#postrequest)<br>The final request inputs class |
| static class | [PostNullableRequest](#postnullablerequest)<br>The initial request inputs class |
| static class | [Post0RequestBuilder](#post0requestbuilder)<br>A builder for the request input class |
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
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.usercreatewithlist.post.UsercreatewithlistPostRequestBody;
import org.openapijsonschematools.client.components.requestbodies.userarray.content.applicationjson.ApplicationjsonSchema;
import org.openapijsonschematools.client.servers.Server0;
import org.openapijsonschematools.client.servers.Server1;
import org.openapijsonschematools.client.servers.Server2;
import org.openapijsonschematools.client.paths.usercreatewithlist.post.responses.UsercreatewithlistPostCodedefaultResponse;
import org.openapijsonschematools.client.servers.RootServerInfo;
import org.openapijsonschematools.client.paths.usercreatewithlist.UsercreatewithlistPost;
import org.openapijsonschematools.client.paths.usercreatewithlist.post.UsercreatewithlistPostResponses;

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
UsercreatewithlistPost.Post apiClient = new UsercreatewithlistPost.Post(apiConfiguration, schemaConfiguration);


ApplicationjsonSchema1BoxedList requestBodyPayload =
    ApplicationjsonSchema.ApplicationjsonSchema1.validateAndBox(
    new ApplicationjsonSchema.ApplicationjsonSchemaListBuilder()
        .add(
            MapUtils.makeMap(
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "id",
                    1L
                ),
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "username",
                    "a"
                ),
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "firstName",
                    "a"
                ),
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "lastName",
                    "a"
                ),
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "email",
                    "a"
                ),
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "password",
                    "a"
                ),
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "phone",
                    "a"
                ),
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "userStatus",
                    1
                ),
                new AbstractMap.SimpleEntry<String, @Nullable Object>(
                    "objectWithNoDeclaredPropsNullable",
                    null
                )
            )
        )
    .build(),
    schemaConfiguration
);
UsercreatewithlistPostRequestBody.SealedRequestBody requestBody = new UsercreatewithlistPostRequestBody.ApplicationjsonRequestBody(requestBodyPayload);

var request = new UsercreatewithlistPost.PostRequestBuilder()
    .requestBody(requestBody)
    .build();

UsercreatewithlistPostResponses.EndpointResponse response;
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
UsercreatewithlistPostResponses.EndpointUsercreatewithlistPostCodedefaultResponse castResponse = (UsercreatewithlistPostResponses.EndpointUsercreatewithlistPostCodedefaultResponse) response;
```
### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Post(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [UsercreatewithlistPostResponses.EndpointResponse](../../paths/usercreatewithlist/post/UsercreatewithlistPostResponses.md#endpointresponse) | post([PostRequest](#postrequest) request) |

## CreateUsersWithListInputOperation
public interface CreateUsersWithListInputOperation<br>

an interface that allows one to call the endpoint using a method named createUsersWithListInput by the operationId

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [UsercreatewithlistPostResponses.EndpointResponse](../../paths/usercreatewithlist/post/UsercreatewithlistPostResponses.md#endpointresponse) | createUsersWithListInput([PostRequest](#postrequest) request) |

## PostRequest
public static class PostRequest<br>

a class that stores the final request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [UsercreatewithlistPostRequestBody.SealedRequestBody](../../paths/usercreatewithlist/post/UsercreatewithlistPostRequestBody.md#sealedrequestbody) | requestBody |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex<br>optional. Note: this will override the value in apiConfiguration |
| @Nullable Duration | timeout<br>optional. Note: this will override the value in apiConfiguration |

## PostNullableRequest
public static class PostNullableRequest<br>

a class that stores the initial request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [UsercreatewithlistPostRequestBody.@Nullable SealedRequestBody](../../paths/usercreatewithlist/post/UsercreatewithlistPostRequestBody.md#sealedrequestbody) | requestBody |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex |
| @Nullable Duration | timeout |

## Post0RequestBuilder
public static class Post0RequestBuilder<br>

a builder for request inputs

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Post0RequestBuilder(Post0RequestBuilder instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PostRequest](#postrequest) | build()<br>Returns the request input used to call an endpoint method |
| [Post0RequestBuilder](#post0requestbuilder) | serverIndex([RootServerInfo.ServerIndex](../../RootServerInfo.md#serverindex) serverIndex)<br>sets the optional property. Note: this will override the value in apiConfiguration |
| [Post0RequestBuilder](#post0requestbuilder) | timeout(Duration timeout)<br>sets the optional property. Note: this will override the value in apiConfiguration |

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
| [Post0RequestBuilder](#post0requestbuilder) | requestBody([UsercreatewithlistPostRequestBody.SealedRequestBody](../../paths/usercreatewithlist/post/UsercreatewithlistPostRequestBody.md#sealedrequestbody) requestBody)<br>sets the property |

[[Back to top]](#top) [[Back to README]](../../../README.md)
