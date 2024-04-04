# Post

public class Post

A class that contains necessary endpoint classes
- a class that calls the endpoint method using the http verb
- a class that calls the endpoint method using the operationId name
- class(es) to store the request inputs
- builder(s) to set the request input data

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [Post1](#post1)<br>The class that has a post method to call the endpoint |
| static class | [PostRequest](#postrequest)<br>The final request inputs class |
| static class | [PostNullableRequest](#postnullablerequest)<br>The initial request inputs class |
| static class | [Post0RequestBuilder](#post0requestbuilder)<br>A builder for the request input class |
| static class | [PostRequestBuilder](#postrequestbuilder)<br>A builder for the request input class |

## Post1
public static class Post1 extends ApiClient.ApiClient1 implements PostOperation<br>

a class that allows one to call the endpoint using a method named post

TODO code sample

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Post1(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [Responses.EndpointResponse](../../paths/fakeparametercollisions1ababselfab/post/Responses.md#endpointresponse) | post([PostRequest](#postrequest) request) |

## PostRequest
public static class PostRequest<br>

a class that stores the final request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [PathParameters.PathParametersMap](../../paths/fakeparametercollisions1ababselfab/post/PathParameters.md#pathparametersmap) | pathParameters |
| [RequestBody.@Nullable SealedRequestBody](../../paths/fakeparametercollisions1ababselfab/post/RequestBody.md#sealedrequestbody) | requestBody<br>optional |
| [HeaderParameters.@Nullable HeaderParametersMap](../../paths/fakeparametercollisions1ababselfab/post/HeaderParameters.md#headerparametersmap) | headerParameters<br>optional |
| [QueryParameters.@Nullable QueryParametersMap](../../paths/fakeparametercollisions1ababselfab/post/QueryParameters.md#queryparametersmap) | queryParameters<br>optional |
| [CookieParameters.@Nullable CookieParametersMap](../../paths/fakeparametercollisions1ababselfab/post/CookieParameters.md#cookieparametersmap) | cookieParameters<br>optional |
| [RootServerInfo.@Nullable ServerIndex](../../RootServerInfo.md#serverindex) | serverIndex<br>optional. Note: this will override the value in apiConfiguration |
| @Nullable Duration | timeout<br>optional. Note: this will override the value in apiConfiguration |

## PostNullableRequest
public static class PostNullableRequest<br>

a class that stores the initial request inputs

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [PathParameters.@Nullable PathParametersMap](../../paths/fakeparametercollisions1ababselfab/post/PathParameters.md#pathparametersmap) | pathParameters |
| [RequestBody.@Nullable SealedRequestBody](../../paths/fakeparametercollisions1ababselfab/post/RequestBody.md#sealedrequestbody) | requestBody |
| [HeaderParameters.@Nullable HeaderParametersMap](../../paths/fakeparametercollisions1ababselfab/post/HeaderParameters.md#headerparametersmap) | headerParameters |
| [QueryParameters.@Nullable QueryParametersMap](../../paths/fakeparametercollisions1ababselfab/post/QueryParameters.md#queryparametersmap) | queryParameters |
| [CookieParameters.@Nullable CookieParametersMap](../../paths/fakeparametercollisions1ababselfab/post/CookieParameters.md#cookieparametersmap) | cookieParameters |
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
| [Post0RequestBuilder](#post0requestbuilder) | requestBody([RequestBody.SealedRequestBody](../../paths/fakeparametercollisions1ababselfab/post/RequestBody.md#sealedrequestbody) requestBody)<br>sets the optional property |
| [Post0RequestBuilder](#post0requestbuilder) | headerParameters([HeaderParametersHeaderParametersMap](../../paths/fakeparametercollisions1ababselfab/post/HeaderParameters.md#headerparametersmap) headerParameters)<br>sets the optional property |
| [Post0RequestBuilder](#post0requestbuilder) | queryParameters([QueryParametersQueryParametersMap](../../paths/fakeparametercollisions1ababselfab/post/QueryParameters.md#queryparametersmap) queryParameters)<br>sets the optional property |
| [Post0RequestBuilder](#post0requestbuilder) | cookieParameters([CookieParametersCookieParametersMap](../../paths/fakeparametercollisions1ababselfab/post/CookieParameters.md#cookieparametersmap) cookieParameters)<br>sets the optional property |
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
| [Post0RequestBuilder](#post0requestbuilder) | pathParameters([PathParametersPathParametersMap](../../paths/fakeparametercollisions1ababselfab/post/PathParameters.md#pathparametersmap) pathParameters)<br>sets the property |

[[Back to top]](#top) [[Back to README]](../../../README.md)
