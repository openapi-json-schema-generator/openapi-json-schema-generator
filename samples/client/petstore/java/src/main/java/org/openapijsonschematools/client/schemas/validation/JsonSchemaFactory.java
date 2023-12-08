package org.openapijsonschematools.client.schemas.validation;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.HashMap;
import java.util.Map;


public class JsonSchemaFactory {
    static Map<Class<? extends JsonSchema>, JsonSchema> classToInstance = new HashMap<>();

    public static <V extends JsonSchema> V getInstance(Class<V> schemaCls) {
        if (classToInstance.containsKey(schemaCls)) {
            return (V) classToInstance.get(schemaCls);
        }
        try {
            Constructor<V> constructor = schemaCls.getConstructor();
            V inst = constructor.newInstance();
            classToInstance.put(schemaCls, inst);
            return inst;
        } catch (NoSuchMethodException | InstantiationException | IllegalAccessException | InvocationTargetException e) {
            throw new RuntimeException(e);
        }
    }
}