package org.openapijsonschematools.components.schemas;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.BooleanJsonSchema;
import org.openapijsonschematools.schemas.DateJsonSchema;
import org.openapijsonschematools.schemas.DateTimeJsonSchema;
import org.openapijsonschematools.schemas.DecimalJsonSchema;
import org.openapijsonschematools.schemas.DoubleJsonSchema;
import org.openapijsonschematools.schemas.FloatJsonSchema;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;
import org.openapijsonschematools.schemas.Int32JsonSchema;
import org.openapijsonschematools.schemas.Int64JsonSchema;
import org.openapijsonschematools.schemas.IntJsonSchema;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.ListJsonSchema;
import org.openapijsonschematools.schemas.MapJsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.NullJsonSchema;
import org.openapijsonschematools.schemas.NumberJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.UnsetAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.UuidJsonSchema;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class User {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Id extends Int64JsonSchema {
    }
    
    
    public class Username implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Username.class, arg, configuration);
        }
    }    
    
    public class FirstName implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(FirstName.class, arg, configuration);
        }
    }    
    
    public class LastName implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(LastName.class, arg, configuration);
        }
    }    
    
    public class Email implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Email.class, arg, configuration);
        }
    }    
    
    public class Password implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Password.class, arg, configuration);
        }
    }    
    
    public class Phone implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Phone.class, arg, configuration);
        }
    }    
    
    public class UserStatus extends Int32JsonSchema {
    }
    
    
    public class ObjectWithNoDeclaredProps extends MapJsonSchema {
    }
    
    
    public class ObjectWithNoDeclaredPropsNullable implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            Void.class,
            FrozenMap.class
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithNoDeclaredPropsNullable.class, arg, configuration);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithNoDeclaredPropsNullable.class, arg, configuration);
        }
    }    
    
    public class AnyTypeProp implements JsonSchema {
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static Integer validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static Float validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static String validate(LocalDate arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
        
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeProp.class, arg, configuration);
        }
    }    
    
    public class Not implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            Void.class
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Not.class, arg, configuration);
        }
    }    
    
    public class AnyTypeExceptNullProp implements JsonSchema {
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static Integer validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static Float validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static String validate(LocalDate arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
    }    
    
    public class AnyTypePropNullable implements JsonSchema {
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static Integer validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static Float validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static String validate(LocalDate arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
        
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypePropNullable.class, arg, configuration);
        }
    }    
    
    public class User1 implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("id", Id.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("username", Username.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("firstName", FirstName.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("lastName", LastName.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("email", Email.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("password", Password.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("phone", Phone.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("userStatus", UserStatus.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("objectWithNoDeclaredProps", ObjectWithNoDeclaredProps.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("objectWithNoDeclaredPropsNullable", ObjectWithNoDeclaredPropsNullable.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("anyTypeProp", AnyTypeProp.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("anyTypeExceptNullProp", AnyTypeExceptNullProp.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("anyTypePropNullable", AnyTypePropNullable.class)
        ));
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(User1.class, arg, configuration);
        }
    }
}
