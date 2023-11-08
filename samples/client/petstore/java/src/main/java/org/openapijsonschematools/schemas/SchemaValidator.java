package org.openapijsonschematools.schemas;

import org.openapijsonschematools.schemas.validators.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validators.KeywordValidator;
import org.openapijsonschematools.schemas.validators.TypeValidator;
import org.openapijsonschematools.schemas.validators.FormatValidator;
import org.openapijsonschematools.schemas.validators.PropertiesValidator;
import org.openapijsonschematools.schemas.validators.RequiredValidator;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.RecordComponent;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public interface SchemaValidator {
    HashMap<String, KeywordValidator> keywordToValidator = new HashMap(){{
        put("additionalProperties", new AdditionalPropertiesValidator());
        put("type", new TypeValidator());
        put("format", new FormatValidator());
        put("properties", new PropertiesValidator());
        put("required", new RequiredValidator());
    }};

    static PathToSchemasMap validate(
            Class<?> schemaCls,
            Object arg,
            ValidationMetadata validationMetadata
    ) {
        HashMap<String, Object> fieldsToValues = new HashMap<>();
        SchemaValidator schema;
        try {
            schema = (SchemaValidator) schemaCls.getMethod("withDefaults").invoke(null);
        } catch (IllegalAccessException | InvocationTargetException | NoSuchMethodException e) {
            throw new RuntimeException(e);
        }
        LinkedHashSet<String> disabledKeywords = validationMetadata.configuration().disabledKeywordFlags().getKeywords();
        RecordComponent[] recordComponents = schemaCls.getRecordComponents();
        for (RecordComponent recordComponent : recordComponents) {
            String fieldName = recordComponent.getName();
            if (disabledKeywords.contains(fieldName)) {
                continue;
            }
            try {
                Object value = recordComponent.getAccessor().invoke(schema);
                fieldsToValues.put(fieldName, value);
            } catch (IllegalAccessException | InvocationTargetException e) {
                throw new RuntimeException(e);
            }
        }
        Object extra = null;
        PathToSchemasMap pathToSchemas = new PathToSchemasMap();
        Class<SchemaValidator> castSchemaCls = (Class<SchemaValidator>) schemaCls;
        for (Map.Entry<String, Object> entry: fieldsToValues.entrySet()) {
            String jsonKeyword = entry.getKey();
            Object value = entry.getValue();
            if (jsonKeyword.equals("additionalProperties") && fieldsToValues.containsKey("properties")) {
                extra = fieldsToValues.get("properties");
            }
            KeywordValidator validatorClass = keywordToValidator.get(jsonKeyword);
            PathToSchemasMap otherPathToSchemas = validatorClass.validate(
                    arg,
                    value,
                    extra,
                    castSchemaCls,
                    validationMetadata
            );
            if (otherPathToSchemas == null) {
                continue;
            }
            pathToSchemas.update(otherPathToSchemas);
        }
        Class<?> baseClass;
        if (arg == null) {
            baseClass = Void.class;
        } else {
            baseClass = arg.getClass();
        }
        List<Object> pathToItem = validationMetadata.pathToItem();
        if (!pathToSchemas.containsKey(pathToItem)) {
            pathToSchemas.put(validationMetadata.pathToItem(), new LinkedHashMap<>());
        }
        pathToSchemas.get(pathToItem).put(baseClass, null);
        pathToSchemas.get(pathToItem).put(schemaCls, null);

        return pathToSchemas;
    }
}
/**
 *     @classmethod
 *     def _validate(
 *         cls,
 *         arg,
 *         validation_metadata: ValidationMetadata,
 *     ) -> PathToSchemasType:
 *         """
 *         SchemaValidator validate
 *         All keyword validation except for type checking was done in calling stack frames
 *         If those validations passed, the validated classes are collected in path_to_schemas
 *         """
 *         cls_schema = cls()
 *         json_schema_data = {
 *             k: v
 *             for k, v in vars(cls_schema).items()
 *             if k not in cls.__excluded_cls_properties
 *             and k
 *             not in validation_metadata.configuration.disabled_json_schema_python_keywords
 *         }
 *         contains_path_to_schemas = []
 *         path_to_schemas: PathToSchemasType = {}
 *         if 'contains' in vars(cls_schema):
 *             contains_path_to_schemas = _get_contains_path_to_schemas(
 *                 arg,
 *                 vars(cls_schema)['contains'],
 *                 validation_metadata,
 *                 path_to_schemas
 *             )
 *         if_path_to_schemas = None
 *         if 'if_' in vars(cls_schema):
 *             if_path_to_schemas = _get_if_path_to_schemas(
 *                 arg,
 *                 vars(cls_schema)['if_'],
 *                 validation_metadata,
 *             )
 *         validated_pattern_properties: typing.Optional[PathToSchemasType] = None
 *         if 'pattern_properties' in vars(cls_schema):
 *              validated_pattern_properties = _get_validated_pattern_properties(
 *                  arg,
 *                  vars(cls_schema)['pattern_properties'],
 *                  cls,
 *                  validation_metadata
 *              )
 *         prefix_items_length = 0
 *         if 'prefix_items' in vars(cls_schema):
 *             prefix_items_length = len(vars(cls_schema)['prefix_items'])
 *         for keyword, val in json_schema_data.items():
 *             used_val: typing.Any
 *             if keyword in {'contains', 'min_contains', 'max_contains'}:
 *                 used_val = (val, contains_path_to_schemas)
 *             elif keyword == 'items':
 *                 used_val = (val, prefix_items_length)
 *             elif keyword in {'unevaluated_items', 'unevaluated_properties'}:
 *                 used_val = (val, path_to_schemas)
 *             elif keyword in {'types'}:
 *                 format: typing.Optional[str] = vars(cls_schema).get('format', None)
 *                 used_val = (val, format)
 *             elif keyword in {'pattern_properties', 'additional_properties'}:
 *                 used_val = (val, validated_pattern_properties)
 *             elif keyword in {'if_', 'then', 'else_'}:
 *                 used_val = (val, if_path_to_schemas)
 *             else:
 *                 used_val = val
 *             validator = json_schema_keyword_to_validator[keyword]
 *
 *             other_path_to_schemas = validator(
 *                 arg,
 *                 used_val,
 *                 cls,
 *                 validation_metadata,
 * 
 *             )
 *             if other_path_to_schemas:
 *                 update(path_to_schemas, other_path_to_schemas)
 *
 *         base_class = type(arg)
 *         if validation_metadata.path_to_item not in path_to_schemas:
 *             path_to_schemas[validation_metadata.path_to_item] = dict()
 *         path_to_schemas[validation_metadata.path_to_item][base_class] = None
 *         path_to_schemas[validation_metadata.path_to_item][cls] = None
 *         return path_to_schemas
 */
