# Responses

public class Responses

A class that contains necessary responses classes
- a sealed interface, EndpointResponse, that stores endpoint responses
- records for each endpoint response

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| sealed interface | [EndpointResponse](#endpointresponse)<br> stores the endpoint responses |
| record | [EndpointCode200Response](#endpointcode200response)<br> the response for 200 |
| record | [EndpointCodedefaultResponse](#endpointcodedefaultresponse)<br> the response for default |

## EndpointResponse
public sealed interface EndpointResponse permits<br>
[EndpointCode200Response](#endpointcode200response),
[EndpointCodedefaultResponse](#endpointcodedefaultresponse)

a sealed interface that stores endpoint responses

## EndpointCode200Response
public record EndpointCode200Response(
    HttpResponse<byte[]> response,
    Void body,
    Void headers
) implements EndpointResponse, ApiResponse<Void, Void><br>

a class that stores an endpoint response

## EndpointCodedefaultResponse
public record EndpointCodedefaultResponse(
    HttpResponse<byte[]> response,
    Void body,
    Void headers
) implements EndpointResponse, ApiResponse<Void, Void><br>

a class that stores an endpoint response

