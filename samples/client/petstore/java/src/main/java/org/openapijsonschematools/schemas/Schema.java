package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public interface Schema<T extends Map, U extends List> extends SchemaValidator {
   static Object castToAllowedTypes(Object arg, List<Object> pathToItem, PathToTypeMap pathToType) {
      if (arg == null) {
         pathToType.put(pathToItem, Void.class);
         return null;
      } else if (arg instanceof String) {
         pathToType.put(pathToItem, String.class);
         return (String) arg;
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
         return argFixed;
      } else if (arg instanceof Boolean) {
         pathToType.put(pathToItem, Boolean.class);
         return (Boolean) arg;
      } else if (arg instanceof Integer) {
         pathToType.put(pathToItem, Integer.class);
         return (Integer) arg;
      } else if (arg instanceof Float) {
         pathToType.put(pathToItem, Float.class);
         return (Float) arg;
      } else if (arg instanceof Double) {
         pathToType.put(pathToItem, Double.class);
         return (Double) arg;
      } else if (arg instanceof BigDecimal) {
         pathToType.put(pathToItem, BigDecimal.class);
         return (BigDecimal) arg;
      } else if (arg instanceof List) {
         pathToType.put(pathToItem, List.class);
         List<Object> argFixed = new ArrayList<>();
         int i =0;
         for (Object item: ((List<?>) arg).toArray()) {
            List<Object> newPathToItem = new ArrayList<>(pathToItem);
            newPathToItem.add(i);
            Object fixedVal = castToAllowedTypes(item, newPathToItem, pathToType);
            argFixed.add(fixedVal);
            i += 1;
         }
         return argFixed;
      } else if (arg instanceof ZonedDateTime) {
         pathToType.put(pathToItem, String.class);
         return arg.toString();
      } else if (arg instanceof LocalDate) {
         pathToType.put(pathToItem, String.class);
         return arg.toString();
      } else {
         Class<?> argClass = arg.getClass();
         throw new RuntimeException("Invalid type passed in got input="+arg+" type="+argClass);
      }
   }

   static PathToSchemasMap getPathToSchemas(Class<Schema> cls, Object arg, ValidationMetadata validationMetadata, PathToTypeMap pathToType) {
      PathToSchemasMap pathToSchemasMap = new PathToSchemasMap();
      if (validationMetadata.validationRanEarlier(cls)) {
         // todo add deeper validated schemas
      } else {
         try {
            PathToSchemasMap otherPathToSchemas = SchemaValidator._validate(cls, arg, validationMetadata);
            pathToSchemasMap.update(otherPathToSchemas);
         } catch (InvocationTargetException | IllegalAccessException e) {
            throw new RuntimeException(e);
         }
         for (LinkedHashMap<Class<?>, Void> schemas: pathToSchemasMap.values()) {
            Class<?> firstSchema = schemas.entrySet().iterator().next().getKey();
            schemas.clear();
            schemas.put(firstSchema, null);
         }
         Set<List<Object>> missingPaths = new HashSet<>(pathToType.keySet());
         missingPaths.removeAll(pathToSchemasMap.keySet());
         if (!missingPaths.isEmpty()) {
            LinkedHashMap<Class<?>, Void> unsetAnyTypeSchema = new LinkedHashMap<>();
            unsetAnyTypeSchema.put(UnsetAnyTypeSchema.class, null);
            for (List<Object> pathToItem: missingPaths) {
               pathToSchemasMap.put(pathToItem, unsetAnyTypeSchema);
            }
         }
      }
      return pathToSchemasMap;
   }

   static LinkedHashMap<String, Object> getProperties(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
      LinkedHashMap<String, Object> properties = new LinkedHashMap<>();
      Map<String, Object> castArg = (Map<String, Object>) arg;
      for(Map.Entry<String, Object> entry: castArg.entrySet()) {
         String propertyName = entry.getKey();
         List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
         propertyPathToItem.add(propertyName);
         Class<Schema> propertyClass = (Class<Schema>) pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
         Object value = entry.getValue();
         Object castValue = getNewInstance(propertyClass, value, propertyPathToItem, pathToSchemas);
         properties.put(propertyName, castValue);
      }
      return properties;
   }

   static List<Object> getItems(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
      ArrayList<Object> items = new ArrayList<>();
      List<Object> castItems = (List<Object>) arg;
      int i = 0;
      for (Object item: items) {
         List<Object> itemPathToItem = new ArrayList<>(pathToItem);
         itemPathToItem.add(i);
         Class<Schema> itemClass = (Class<Schema>) pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
         Object castItem = getNewInstance(itemClass, item, itemPathToItem, pathToSchemas);
         items.add(castItem);
         i += 1;
      }
      return items;
   }

   static Map<Class<?>, Class<?>> getTypeToOutputClass(Class<?> cls) {
      try {
         // This must be implemented in Schemas that are generics as a static method
         Method method = cls.getMethod("typeToOutputClass");
         Map<Class<?>, Class<?>> typeToOutputClass = (Map<Class<?>, Class<?>>) method.invoke(null);
         return typeToOutputClass;
      } catch (NoSuchMethodException | InvocationTargetException | IllegalAccessException e) {
         return null;
      }
   }

   static Object getNewInstance(Class<Schema> cls, Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
      Object usedArg;
      if (arg instanceof Map) {
         usedArg = getProperties(arg, pathToItem, pathToSchemas);
      } else if (arg instanceof List) {
         usedArg = getItems(arg, pathToItem, pathToSchemas);
      } else if (arg instanceof Boolean) {
         return (Boolean) arg;
      } else {
         // str, int, float, FileIO, bytes
         return arg;
      }
      Class<?> argType = arg.getClass();
      Map<Class<?>, Class<?>> typeToOutputClass = getTypeToOutputClass(cls);
      if (typeToOutputClass == null) {
         return usedArg;
      }
      Class<?> outputClass = typeToOutputClass.get(argType);
      // TODO add class instantiation here
      return null;
   }

   public static Void validateBase(Class<?> cls, Void arg, SchemaConfiguration configuration) {
      return (Void) validateObjectBase(cls, arg, configuration);
   }

   public static Boolean validateBase(Class<?> cls, Boolean arg, SchemaConfiguration configuration) {
      return (Boolean) validateObjectBase(cls, arg, configuration);
   }

   public static Integer validateBase(Class<?> cls, Integer arg, SchemaConfiguration configuration) {
      return (Integer) validateObjectBase(cls, arg, configuration);
   }

   public static Float validateBase(Class<?> cls, Float arg, SchemaConfiguration configuration) {
      return (Float) validateObjectBase(cls, arg, configuration);
   }

   public static Double validateBase(Class<?> cls, Double arg, SchemaConfiguration configuration) {
      return (Double) validateObjectBase(cls, arg, configuration);
   }

   public static String validateBase(Class<?> cls, String arg, SchemaConfiguration configuration) {
      return (String) validateObjectBase(cls, arg, configuration);
   }

   public static String validateBase(Class<?> cls, ZonedDateTime arg, SchemaConfiguration configuration) {
      return (String) validateObjectBase(cls, arg, configuration);
   }

   public static String validateBase(Class<?> cls, LocalDate arg, SchemaConfiguration configuration) {
      return (String) validateObjectBase(cls, arg, configuration);
   }

   public static <T extends Map> T validateBase(Class<?> cls, T arg, SchemaConfiguration configuration) {
      return (T) validateObjectBase(cls, arg, configuration);
   }

   public static <U extends List> U validateBase(Class<?> cls, U arg, SchemaConfiguration configuration) {
      return (U) validateObjectBase(cls, arg, configuration);
   }

   // todo add bytes and FileIO

   private static Object validateObjectBase(Class<?> cls, Object arg, SchemaConfiguration configuration) {
      Class<Schema> castCls = (Class<Schema>) cls;
      if (arg instanceof Map || arg instanceof List) {
         // todo don't run validation if the instance is one of the class generic types
      }
      PathToTypeMap pathToType = new PathToTypeMap();
      List<Object> pathToItem = new ArrayList<>();
      pathToItem.add("args[0]");
      Object castArg = castToAllowedTypes(arg, pathToItem, pathToType);
      SchemaConfiguration usedConfiguration;
      if (configuration != null) {
         usedConfiguration = configuration;
      } else {
         usedConfiguration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());
      }
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