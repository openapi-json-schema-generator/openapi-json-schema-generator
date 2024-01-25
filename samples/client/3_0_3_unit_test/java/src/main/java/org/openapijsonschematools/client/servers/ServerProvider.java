package org.openapijsonschematools.client.servers;

import org.checkerframework.checker.nullness.qual.Nullable;

public interface ServerProvider<T> {
    Server getServer(@Nullable T serverIndex);
}

