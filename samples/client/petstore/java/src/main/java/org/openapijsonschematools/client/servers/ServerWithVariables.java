package org.openapijsonschematools.client.servers;

public abstract class ServerWithVariables {
    public final String url;

    protected ServerWithVariables(String url) {
        this.url = url;
    }
}

