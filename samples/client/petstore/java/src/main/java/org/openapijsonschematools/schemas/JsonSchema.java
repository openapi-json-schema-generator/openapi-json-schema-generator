package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.UUID;

public interface JsonSchema extends SchemaValidator {
   private static Object castToAllowedTypes(Object arg, List<Object> pathToItem, PathToTypeMap pathToType) {
      if (arg == null) {
         pathToType.put(pathToItem, Void.class);
         return null;
      } else if (arg instanceof String) {
         pathToType.put(pathToItem, String.class);
         return arg;
      } else if (arg instanceof Map) {
         pathToType.put(pathToItem, Map.class);
         LinkedHashMap<String, Object> argFixed = new LinkedHashMap<>();
         for (Map.Entry<?, ?> entry: ((Map<?, ?>) arg).entrySet()) {
            String key = (String) entry.getKey();
            Object val = entry.getValue();
            List<Object> newPathToItem = new ArrayList<>(pathToItem);
            newPathToItem.add(key);
            Object fixedVal = castToAllowedTypes(val, newPathToItem, pathToType);
            argFixed.put(key, fixedVal);
         }
         return new FrozenMap<>(argFixed);
      } else if (arg instanceof Boolean) {
         pathToType.put(pathToItem, Boolean.class);
         return arg;
      } else if (arg instanceof Integer) {
         pathToType.put(pathToItem, Integer.class);
         return arg;
      } else if (arg instanceof Long) {
         pathToType.put(pathToItem, Long.class);
         return arg;
      } else if (arg instanceof Float) {
         pathToType.put(pathToItem, Float.class);
         return arg;
      } else if (arg instanceof Double) {
         pathToType.put(pathToItem, Double.class);
         return arg;
      } else if (arg instanceof List) {
         pathToType.put(pathToItem, FrozenList.class);
         List<Object> argFixed = new ArrayList<>();
         int i =0;
         for (Object item: ((List<?>) arg).toArray()) {
            List<Object> newPathToItem = new ArrayList<>(pathToItem);
            newPathToItem.add(i);
            Object fixedVal = castToAllowedTypes(item, newPathToItem, pathToType);
            argFixed.add(fixedVal);
            i += 1;
         }
         return new FrozenList<>(argFixed);
      } else if (arg instanceof ZonedDateTime) {
         pathToType.put(pathToItem, String.class);
         return arg.toString();
      } else if (arg instanceof LocalDate) {
         pathToType.put(pathToItem, String.class);
         return arg.toString();
      } else if (arg instanceof UUID) {
         pathToType.put(pathToItem, String.class);
         return arg.toString();
      } else {
         Class<?> argClass = arg.getClass();
         throw new RuntimeException("Invalid type passed in got input="+arg+" type="+argClass);
      }
   }

   private static PathToSchemasMap getPathToSchemas(Class<JsonSchema> cls, Object arg, ValidationMetadata validationMetadata, PathToTypeMap pathToType) {
      PathToSchemasMap pathToSchemasMap = new PathToSchemasMap();
      if (validationMetadata.validationRanEarlier(cls)) {
         // todo add deeper validated schemas
      } else {
         PathToSchemasMap otherPathToSchemas = SchemaValidator.validate(cls, arg, validationMetadata);
         pathToSchemasMap.update(otherPathToSchemas);
         for (LinkedHashMap<Class<?>, Void> schemas: pathToSchemasMap.values()) {
            Class<?> firstSchema = schemas.entrySet().iterator().next().getKey();
            schemas.clear();
            schemas.put(firstSchema, null);
         }
         Set<List<Object>> missingPaths = new HashSet<>(pathToType.keySet());
         missingPaths.removeAll(pathToSchemasMap.keySet());
         if (!missingPaths.isEmpty()) {
            LinkedHashMap<Class<?>, Void> unsetAnyTypeSchema = new LinkedHashMap<>();
            unsetAnyTypeSchema.put(UnsetAnyTypeJsonSchema.class, null);
            for (List<Object> pathToItem: missingPaths) {
               pathToSchemasMap.put(pathToItem, unsetAnyTypeSchema);
            }
         }
      }
      return pathToSchemasMap;
   }

   private static FrozenMap<String, Object> getProperties(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
      LinkedHashMap<String, Object> properties = new LinkedHashMap<>();
      Map<String, Object> castArg = (Map<String, Object>) arg;
      for(Map.Entry<String, Object> entry: castArg.entrySet()) {
         String propertyName = entry.getKey();
         List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
         propertyPathToItem.add(propertyName);
         Class<JsonSchema> propertyClass = (Class<JsonSchema>) pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
         Object value = entry.getValue();
         Object castValue = getNewInstance(propertyClass, value, propertyPathToItem, pathToSchemas);
         properties.put(propertyName, castValue);
      }
      return new FrozenMap<>(properties);
   }

   private static FrozenList<Object> getItems(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
      ArrayList<Object> items = new ArrayList<>();
      List<Object> castItems = (List<Object>) arg;
      int i = 0;
      for (Object item: castItems) {
         List<Object> itemPathToItem = new ArrayList<>(pathToItem);
         itemPathToItem.add(i);
         Class<JsonSchema> itemClass = (Class<JsonSchema>) pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
         Object castItem = getNewInstance(itemClass, item, itemPathToItem, pathToSchemas);
         items.add(castItem);
         i += 1;
      }
      return new FrozenList<>(items);
   }

   private static Object getNewInstance(Class<JsonSchema> cls, Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
      if (!(arg instanceof Map || arg instanceof List)) {
          // str, int, float, boolean, null, FileIO, bytes
          return arg;
      }
      if (arg instanceof Map) {
         FrozenMap<String, Object> usedArg = getProperties(arg, pathToItem, pathToSchemas);
         try {
            Method method = cls.getMethod("getMapOutputInstance", FrozenMap.class);
            return method.invoke(null, usedArg);
         } catch (NoSuchMethodException e) {
            return usedArg;
         } catch (InvocationTargetException | IllegalAccessException e) {
            throw new RuntimeException(e);
         }
      } else if (arg instanceof List) {
         FrozenList<Object> usedArg = getItems(arg, pathToItem, pathToSchemas);
         try {
            Method method = cls.getMethod("getListOutputInstance", FrozenList.class);
            return method.invoke(null, usedArg);
         } catch (NoSuchMethodException e) {
            return usedArg;
         } catch (InvocationTargetException | IllegalAccessException e) {
            throw new RuntimeException(e);
         }
      }
      return null;
   }

   static Void validate(Class<?> cls, Void arg, SchemaConfiguration configuration) {
      return (Void) validateObject(cls, arg, configuration);
   }

   static Boolean validate(Class<?> cls, Boolean arg, SchemaConfiguration configuration) {
      return (Boolean) validateObject(cls, arg, configuration);
   }

   static Integer validate(Class<?> cls, Integer arg, SchemaConfiguration configuration) {
      return (Integer) validateObject(cls, arg, configuration);
   }

   static Long validate(Class<?> cls, Long arg, SchemaConfiguration configuration) {
      return (Long) validateObject(cls, arg, configuration);
   }

   static Float validate(Class<?> cls, Float arg, SchemaConfiguration configuration) {
      return (Float) validateObject(cls, arg, configuration);
   }

   static Double validate(Class<?> cls, Double arg, SchemaConfiguration configuration) {
      return (Double) validateObject(cls, arg, configuration);
   }

   static String validate(Class<?> cls, String arg, SchemaConfiguration configuration) {
      return (String) validateObject(cls, arg, configuration);
   }

   static String validate(Class<?> cls, ZonedDateTime arg, SchemaConfiguration configuration) {
      return (String) validateObject(cls, arg, configuration);
   }

   static String validate(Class<?> cls, LocalDate arg, SchemaConfiguration configuration) {
      return (String) validateObject(cls, arg, configuration);
   }

   static String validate(Class<?> cls, UUID arg, SchemaConfiguration configuration) {
      return (String) validateObject(cls, arg, configuration);
   }

   static <T extends FrozenMap> T validate(Class<?> cls, Map<String, Object> arg, SchemaConfiguration configuration) {
      return (T) validateObject(cls, arg, configuration);
   }

   static <U extends FrozenList> U validate(Class<?> cls, List<Object> arg, SchemaConfiguration configuration) {
      return (U) validateObject(cls, arg, configuration);
   }

   // todo add bytes and FileIO

   private static Object validateObject(Class<?> cls, Object arg, SchemaConfiguration configuration) {
      Class<JsonSchema> castCls = (Class<JsonSchema>) cls;
      if (arg instanceof Map || arg instanceof List) {
         // todo don't run validation if the instance is one of the class generic types
      }
      PathToTypeMap pathToType = new PathToTypeMap();
      List<Object> pathToItem = new ArrayList<>();
      pathToItem.add("args[0]");
      Object castArg = castToAllowedTypes(arg, pathToItem, pathToType);
      SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
      PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
      ValidationMetadata validationMetadata = new ValidationMetadata(
              pathToItem,
              usedConfiguration,
              validatedPathToSchemas,
              new LinkedHashSet<>()
      );
      PathToSchemasMap pathToSchemasMap = getPathToSchemas(castCls, castArg, validationMetadata, pathToType);
      return getNewInstance(castCls, castArg, validationMetadata.pathToItem(), pathToSchemasMap);
   }

}