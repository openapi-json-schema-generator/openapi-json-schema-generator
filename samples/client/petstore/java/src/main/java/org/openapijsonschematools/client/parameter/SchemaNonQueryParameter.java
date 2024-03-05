package org.openapijsonschematools.client.parameter;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.header.PrefixSeparatorIterator;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;

import java.util.Map;

public class SchemaNonQueryParameter extends SchemaParameter implements NonQueryParameter {

    public SchemaNonQueryParameter(String name, ParameterInType inType, boolean required, @Nullable ParameterStyle style, @Nullable Boolean explode, @Nullable Boolean allowReserved, JsonSchema<?> schema) {
        super(name, inType, required, style, explode, allowReserved, schema);
    }

    @Override
    public Map<String, String> serialize(@Nullable Object inData, boolean validate, SchemaConfiguration configuration) {
        return super.serialize(inData, validate, configuration, null);
    }
}