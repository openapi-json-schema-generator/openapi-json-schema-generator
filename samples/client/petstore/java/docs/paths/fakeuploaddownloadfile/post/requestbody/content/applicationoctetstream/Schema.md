# Schema
public class Schema

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [Schema.Schema1Boxed](#schema1boxed)<br> abstract sealed validated payload class |
| static class | [Schema.Schema1](#schema1)<br> schema class |

## Schema1Boxed
public static abstract sealed class Schema1Boxed<br>
permits<br>

abstract sealed class that stores validated payloads using boxed classes

## Schema1
public static class Schema1<br>
extends JsonSchema

A schema class that validates payloads

## Description
file to upload
