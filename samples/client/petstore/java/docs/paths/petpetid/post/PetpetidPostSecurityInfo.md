# PetpetidPostSecurityInfo
PetpetidPostSecurityInfo.java

public class PetpetidPostSecurityInfo

A class that provides a security requirement object, and any needed security info classes
- a class that stores a securityIndex and provides a SecurityRequirementsObject
- an enum class that describes security index values

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [PetpetidPostSecurityInfo.PetpetidPostSecurityInfo1](#petpetidpostsecurityinfo1)<br>SecurityRequirementObjectProvider
| enum | [PetpetidPostSecurityInfo.SecurityIndex](#securityindex)<br>class that stores a security index |

## PetpetidPostSecurityInfo1
implements SecurityRequirementObjectProvider<[SecurityIndex](#securityindex)>

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PetpetidPostSecurityInfo1()<br>Creates an instance |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| EnumMap<SecurityIndex, SecurityRequirementObject> | securities = new EnumMap<>(Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new AbstractMap.SimpleEntry<>(SecurityIndex.SECURITY_0, new [PetpetidPostSecurityRequirementObject0()](../../../paths/petpetid/post/security/PetpetidPostSecurityRequirementObject0.md),<br>&nbsp;&nbsp;&nbsp;&nbsp;new AbstractMap.SimpleEntry<>(SecurityIndex.SECURITY_1, new [PetpetidPostSecurityRequirementObject1()](../../../paths/petpetid/post/security/PetpetidPostSecurityRequirementObject1.md)<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| SecurityRequirementObject | getSecurityRequirementObject(@Nullable [SecurityIndex](#securityindex) securityIndex)<br>If null is input, then the instance's securityIndex will be used |

## SecurityIndex
enum SecurityIndex<br>

### Enum Constant Summary
| Enum Constant And Description |
| ----------------------------- |
| SECURITY_0<br>security 0 |
| SECURITY_1<br>security 1 |
