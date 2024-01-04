package org.openapijsonschematools.client.schemas;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class ListBuilderTest {
    public static class NullableListWithNullableItemsListBuilder {
        // class to build List<@Nullable List<Number>>
        private final List<@Nullable List<Number>> list;

        public NullableListWithNullableItemsListBuilder() {
            list = new ArrayList<>();
        }

        public NullableListWithNullableItemsListBuilder(List<@Nullable List<Number>> list) {
            this.list = list;
        }

        public NullableListWithNullableItemsListBuilder add(Void item) {
            list.add(null);
            return this;
        }

        public NullableListWithNullableItemsListBuilder add(List<Number> item) {
            list.add(item);
            return this;
        }

        public List<@Nullable List<Number>> build() {
            return list;
        }
    }

    @Test
    public void testSucceedsWithNullInput() {
        List<@Nullable List<Number>> inList = new ArrayList<>();
        inList.add(null);
        var builder = new NullableListWithNullableItemsListBuilder(inList);
        Assert.assertEquals(inList, builder.build());

        builder = new NullableListWithNullableItemsListBuilder();
        builder.add((Void) null);
        Assert.assertEquals(inList, builder.build());
    }

    @Test
    public void testSucceedsWithNonNullInput() {
        List<@Nullable List<Number>> inList = new ArrayList<>();
        inList.add(List.of(1));
        var builder = new NullableListWithNullableItemsListBuilder(inList);
        Assert.assertEquals(inList, builder.build());

        builder = new NullableListWithNullableItemsListBuilder();
        builder.add(List.of(1));
        Assert.assertEquals(inList, builder.build());
    }
}