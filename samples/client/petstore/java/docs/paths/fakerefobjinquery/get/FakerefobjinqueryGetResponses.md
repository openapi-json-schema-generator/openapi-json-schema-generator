# FakerefobjinqueryGetResponses

public class FakerefobjinqueryGetResponses

A class that contains necessary responses classes
- a sealed interface, EndpointResponse, that stores endpoint responses
- records for each endpoint response

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| sealed interface | [EndpointResponse](#endpointresponse)<br> stores the endpoint responses |
| record | [EndpointFakerefobjinqueryGetCode200Response](#endpointfakerefobjinquerygetcode200response)<br> the response for 200 |

## EndpointResponse
public sealed interface EndpointResponse permits<br>
[EndpointFakerefobjinqueryGetCode200Response](#endpointfakerefobjinquerygetcode200response)

a sealed interface that stores endpoint responses

## EndpointFakerefobjinqueryGetCode200Response
public record EndpointFakerefobjinqueryGetCode200Response(
    HttpResponse<byte[]> response,
    Void body,
    Void headers
) implements EndpointResponse, ApiResponse<Void, Void><br>

a class that stores an endpoint response

