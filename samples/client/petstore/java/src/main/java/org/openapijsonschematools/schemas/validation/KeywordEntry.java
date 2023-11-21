package org.openapijsonschematools.schemas.validation;

import java.util.AbstractMap;

public class KeywordEntry extends AbstractMap.SimpleEntry<String, KeywordValidator> {
    public KeywordEntry(String key, KeywordValidator value) {
        super(key, value);
    }
}
