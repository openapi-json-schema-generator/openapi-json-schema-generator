package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class FileSchemaTestClass {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class FilesList extends FrozenList<File.FileMap> {

        FilesList(FrozenList<File.FileMap> m) {

            super(m);
        }
        public static FilesList of(List<Map<String, Object>> arg, SchemaConfiguration configuration) {


            return Files.validate(arg, configuration);
        }
    }
    
    
    public class Files extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(File.File1.class))
        ));
        protected static FilesList getListOutputInstance(FrozenList<File.FileMap> arg) {

            return new FilesList(arg);
        }
        public static FilesList validate(List<Map<String, Object>> arg, SchemaConfiguration configuration) {


            return JsonSchema.validate(Files.class, arg, configuration);
        }
    }    
    
    public static class FileSchemaTestClassMap extends FrozenMap<String, Object> {

        FileSchemaTestClassMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
        );
        public static final Set<String> optionalKeys = Set.of(
            "file",
            "files"
        );
        public static FileSchemaTestClassMap of(Map<String, Object> arg, SchemaConfiguration configuration) {

            return FileSchemaTestClass1.validate(arg, configuration);
        }
        
        public File.FileMap file() {

            String key = "file";
            if (!containsKey(key)) {
                throw new RuntimeException("file is unset");
            }
            return (File.FileMap) get(key);

        }
        
        public FilesList files() {

            String key = "files";
            if (!containsKey(key)) {
                throw new RuntimeException("files is unset");
            }
            return (FilesList) get(key);

        }
        
        public Object getAdditionalProperty(String name) {
            schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
            return self.get(name, schemas.unset)
        }
    }    
    
    public class FileSchemaTestClass1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("file", File.File1.class),
                new PropertyEntry("files", Files.class)
            )))
        ));
        protected static FileSchemaTestClassMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new FileSchemaTestClassMap(arg);
        }
        public static FileSchemaTestClassMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {

            return JsonSchema.validate(FileSchemaTestClass1.class, arg, configuration);
        }
    }
}
