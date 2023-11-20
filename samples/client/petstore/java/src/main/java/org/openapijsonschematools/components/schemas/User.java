package org.openapijsonschematools.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.Int32JsonSchema;
import org.openapijsonschematools.schemas.Int64JsonSchema;
import org.openapijsonschematools.schemas.MapJsonSchema;
import org.openapijsonschematools.schemas.NullJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class User {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Id extends Int64JsonSchema {}
    
    
    public class Username extends StringJsonSchema {}
    
    
    public class FirstName extends StringJsonSchema {}
    
    
    public class LastName extends StringJsonSchema {}
    
    
    public class Email extends StringJsonSchema {}
    
    
    public class Password extends StringJsonSchema {}
    
    
    public class Phone extends StringJsonSchema {}
    
    
    public class UserStatus extends Int32JsonSchema {}
    
    
    public class ObjectWithNoDeclaredProps extends MapJsonSchema {}
    
    
    public class ObjectWithNoDeclaredPropsNullable extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
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
    
    public class AnyTypeProp extends AnyTypeJsonSchema {}
    
    
    public class Not extends NullJsonSchema {}
    
    
    public class AnyTypeExceptNullProp extends JsonSchema {
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
        
        public static String validate(UUID arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
        
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AnyTypeExceptNullProp.class, arg, configuration);
        }
    }    
    
    public class AnyTypePropNullable extends AnyTypeJsonSchema {}
    
    
    public static class UserMap extends FrozenMap<String, Object> {
        UserMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static UserMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return User1.validate(arg, configuration);
        }
    }    
    
    public class User1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
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
        protected static UserMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new UserMap(arg);
        }
        public static UserMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(User1.class, arg, configuration);
        }
    }
}
