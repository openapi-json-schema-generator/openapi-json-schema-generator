package org.openapijsonschematools.codegen.generators.openapimodels;

import java.util.AbstractList;
import java.util.Iterator;
import java.util.List;

/**
 * A class to store inline codegenschema definitions
 */
public class CodegenServers extends AbstractList<CodegenServer> {
    public final List<CodegenServer> servers;
    public final CodegenKey jsonPathPiece;
    public final String subpackage;

    public CodegenServers(List<CodegenServer> servers, CodegenKey jsonPathPiece, String subpackage) {
        this.servers = servers;
        this.jsonPathPiece = jsonPathPiece;
        this.subpackage = subpackage;
    }

    @Override
    public CodegenServer get(int index) {
        return this.servers.get(index);
    }

    @Override
    public int size() {
        return this.servers.size();
    }
}
