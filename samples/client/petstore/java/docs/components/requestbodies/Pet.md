# Pet
Pet.java

public class Pet

A class that contains necessary nested request body classes
- supporting XMediaType classes which store the openapi request body contentType to schema information
- a class that extends RequestBodySerializer and is used to serialize input SealedRequestBody instances
- SealedRequestBody class, an abstract sealed class which contains all the contentType/schema input types
- final classes which extend SealedRequestBody, the concrete request body types

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [Pet.ApplicationjsonMediaType](#applicationjsonmediatype)<br>class storing schema info for a specific contentType |
| static class | [Pet.ApplicationxmlMediaType](#applicationxmlmediatype)<br>class storing schema info for a specific contentType |
| static class | [Pet.Pet1](#pet1)<br>class that serializes request bodies |
| static class | [Pet.SealedRequestBody](#sealedrequestbody)<br>abstract sealed request body class |
| static class | [Pet.ApplicationjsonRequestBody](#applicationjsonrequestbody)<br>implementing sealed class to store request body input |
| static class | [Pet.ApplicationxmlRequestBody](#applicationxmlrequestbody)<br>implementing sealed class to store request body input |

## ApplicationjsonMediaType
public static class ApplicationjsonMediaType<br>
extends MediaType<[ApplicationjsonSchema.ApplicationjsonSchema1](../../components/requestbodies/pet/content/applicationjson/ApplicationjsonSchema.md#applicationjsonschema1)>

class storing schema info for a specific contentType

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ApplicationjsonMediaType()<br>Creates an instance |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [ApplicationjsonSchema.ApplicationjsonSchema1](../../components/requestbodies/pet/content/applicationjson/ApplicationjsonSchema.md#applicationjsonschema1) | schema<br>the schema for this MediaType |

## ApplicationxmlMediaType
public static class ApplicationxmlMediaType<br>
extends MediaType<[ApplicationxmlSchema.ApplicationxmlSchema1](../../components/requestbodies/pet/content/applicationxml/ApplicationxmlSchema.md#applicationxmlschema1)>

class storing schema info for a specific contentType

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ApplicationxmlMediaType()<br>Creates an instance |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| [ApplicationxmlSchema.ApplicationxmlSchema1](../../components/requestbodies/pet/content/applicationxml/ApplicationxmlSchema.md#applicationxmlschema1) | schema<br>the schema for this MediaType |

## Pet1
public static class Pet1<br>

a class that serializes SealedRequestBody request bodies

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Pet1()<br>Creates an instance |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| boolean | required = true<br>whether the request body is required |
| Map<String, MediaType<?>> | content =  Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new AbstractMap.SimpleEntry<>("application/json", new [ApplicationjsonMediaType](#applicationjsonmediatype)()),<br>&nbsp;&nbsp;&nbsp;&nbsp;new AbstractMap.SimpleEntry<>("application/xml", new [ApplicationxmlMediaType](#applicationxmlmediatype)())<br>)<br>the contentType to schema info |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| SerializedRequestBody | serialize([SealedRequestBody](#sealedrequestbody) requestBody)<br>called by endpoint when creating request body bytes |

## SealedRequestBody
public static abstract sealed class SealedRequestBody<br>
permits<br>
[ApplicationjsonRequestBody](#applicationjsonrequestbody),
[ApplicationxmlRequestBody](#applicationxmlrequestbody)

abstract sealed class that stores request contentType + validated schema data

## ApplicationjsonRequestBody
public static final class ApplicationjsonRequestBody<br>
extends [SealedRequestBody](#sealedrequestbody)<br>
implements GenericRequestBody<ApplicationjsonSchema.[Pet1Boxed](../../components/schemas/Pet.md#pet1boxed)><br>

A final class to store request body input for contentType="application/json"

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ApplicationjsonRequestBody(ApplicationjsonSchema.[Pet1Boxed](../../components/schemas/Pet.md#pet1boxed) body)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | contentType()<br>always returns "application/json" |
| ApplicationjsonSchema.[Pet1Boxed](../../components/schemas/Pet.md#pet1boxed) | body()<br>returns the body passed in in the constructor |
## ApplicationxmlRequestBody
public static final class ApplicationxmlRequestBody<br>
extends [SealedRequestBody](#sealedrequestbody)<br>
implements GenericRequestBody<ApplicationxmlSchema.[Pet1Boxed](../../components/schemas/Pet.md#pet1boxed)><br>

A final class to store request body input for contentType="application/xml"

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ApplicationxmlRequestBody(ApplicationxmlSchema.[Pet1Boxed](../../components/schemas/Pet.md#pet1boxed) body)<br>Creates an instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | contentType()<br>always returns "application/xml" |
| ApplicationxmlSchema.[Pet1Boxed](../../components/schemas/Pet.md#pet1boxed) | body()<br>returns the body passed in in the constructor |

[[Back to top]](#top) [[Back to Component RequestBodies]](../../../README.md#Component-RequestBodies) [[Back to README]](../../../README.md)
