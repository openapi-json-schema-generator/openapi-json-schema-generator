package org.openapijsonschematools.client.header;

import org.checkerframework.checker.nullness.qual.Nullable;

public class StyleSerializer extends Rfc6570Serializer {
    public static String serializeSimple(
            @Nullable Object inData,
            String name,
            boolean explode,
            boolean percentEncode
    ) {
        var prefixSeparatorIterator = new PrefixSeparatorIterator("", ",");
        return rfc6570Expansion(
                name,
                inData,
                explode,
                percentEncode,
                prefixSeparatorIterator
        );
    }

    public static String serializeForm(
            @Nullable Object inData,
            String name,
            boolean explode,
            boolean percentEncode,
            @Nullable PrefixSeparatorIterator iterator,
            boolean isCookie
    ) {
        // todo check that the prefix and suffix matches this one
        String prefix = isCookie ? "" : "?";
        PrefixSeparatorIterator usedIterator = iterator == null ? new PrefixSeparatorIterator(prefix, "&") : iterator;
        return rfc6570Expansion(
            name,
            inData,
            explode,
            percentEncode,
            usedIterator
        );
    }

    public static String serializeMatrix(
            @Nullable Object inData,
            String name,
            boolean explode
    ) {
        PrefixSeparatorIterator usedIterator = new PrefixSeparatorIterator(";", ";");
        return rfc6570Expansion(
            name,
            inData,
            explode,
            true,
            usedIterator
        );
    }

    public static String serializeLabel(
            @Nullable Object inData,
            String name,
            boolean explode
    ) {
        PrefixSeparatorIterator usedIterator = new PrefixSeparatorIterator(".", ".");
        return rfc6570Expansion(
            name,
            inData,
            explode,
            true,
            usedIterator
        );
    }

    public static String serializeSpaceDelimited(
            @Nullable Object inData,
            String name,
            boolean explode,
            @Nullable PrefixSeparatorIterator iterator
    ) {
        PrefixSeparatorIterator usedIterator = iterator == null ? new PrefixSeparatorIterator("", "%20") : iterator;
        return rfc6570Expansion(
            name,
            inData,
            explode,
            true,
            usedIterator
        );
    }

    public static String serializePipeDelimited(
            @Nullable Object inData,
            String name,
            boolean explode,
            @Nullable PrefixSeparatorIterator iterator
    ) {
        PrefixSeparatorIterator usedIterator = iterator == null ? new PrefixSeparatorIterator("", "|") : iterator;
        return rfc6570Expansion(
            name,
            inData,
            explode,
            true,
            usedIterator
        );
    }
}