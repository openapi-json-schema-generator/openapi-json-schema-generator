package org.openapijsonschematools.codegen.templating.handlebars;

import com.github.jknack.handlebars.Helper;
import com.github.jknack.handlebars.Options;
import com.github.jknack.handlebars.TagType;
import org.apache.commons.lang3.StringUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import static org.apache.commons.lang3.Validate.isTrue;
import static org.apache.commons.lang3.Validate.notNull;

public enum CustomHelpers implements Helper<Object> {

    /**
     * Indicates the set or map contains the given key
     * For example:
     *
     * <pre>
     * {{#contains someMap "someKey"}}
     * {{/contains}}
     * </pre>
     *
     * <pre>
     * {{#contains someSet "someItem"}}
     * {{/contains}}
     * </pre>
     */
    contains {
        @Override public Object apply(final Object a, final Options options) throws IOException {
            Object b = options.param(0, null);
            boolean result;
            if (Map.class.isInstance(a)) {
                Map mapA = (Map) a;
                result = mapA.containsKey(b);
            } else if (Set.class.isInstance(a)) {
                Set setA = (Set) a;
                result = setA.contains(b);
            } else {
                result = false;
            }
            if (options.tagType == TagType.SECTION) {
                return result ? options.fn() : options.inverse();
            }
            return result
                    ? options.hash("yes", true)
                    : options.hash("no", false);
        }
    },

    /**
     * Makes an empty array of strings
     */
    newArray {
        @Override public Object apply(final Object a, final Options options) throws IOException {
            return new ArrayList<String>();
        }
    },

    /**
     * Adds items on to an ArrayList
     *
     * <pre>
     * {{join value " // " [prefix=""] [suffix=""]}}
     * </pre>
     *
     * <p>
     * If value is the list ['a', 'b', 'c'], the output will be the string "a // b // c".
     * </p>
     * Or:
     *
     * <pre>
     * {{join "a" "b" "c" " // " [prefix=""] [suffix=""]}}
     * Join the "a", "b", "c", the output will be the string "a // b // c".
     * </pre>
     */
    add {
        @Override
        public Object apply(final Object context, final Options options) {
            if (!(context instanceof ArrayList)) {
                return "";
            }
            return safeApply((ArrayList<String>) context, options);
        }

        protected CharSequence safeApply(final ArrayList<String> context, final Options options) {
            // join everything as single values
            Object[] values = new Object[options.params.length];
            for (Object item: options.params) {
                context.add((String) item);
            }
            return null;
        }
    }
}
