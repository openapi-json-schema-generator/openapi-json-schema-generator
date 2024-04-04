# FakePostSecurityInfo
FakePostSecurityInfo.java

public class FakePostSecurityInfo

A class that provides a security requirement object, and any needed security info classes
- a class that stores a securityIndex and provides a SecurityRequirementsObject
- an enum class that describes security index values

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [FakePostSecurityInfo.FakePostSecurityInfo1](#fakepostsecurityinfo1)<br>SecurityRequirementObjectProvider
| enum | [FakePostSecurityInfo.SecurityIndex](#securityindex)<br>class that stores a security index |

## FakePostSecurityInfo1
implements SecurityRequirementObjectProvider<[SecurityIndex](#securityindex)>

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FakePostSecurityInfo1()<br>Creates an instance |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| EnumMap<SecurityIndex, SecurityRequirementObject> | securities = new EnumMap<>(Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new AbstractMap.SimpleEntry<>(SecurityIndex.SECURITY_0, new [FakePostSecurityRequirementObject0()](../../../paths/fake/post/security/FakePostSecurityRequirementObject0.md)<br>)); |

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
