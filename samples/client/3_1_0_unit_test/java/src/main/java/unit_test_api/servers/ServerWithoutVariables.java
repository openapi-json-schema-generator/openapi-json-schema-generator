package unit_test_api.servers;

public abstract class ServerWithoutVariables implements Server {
    public final String url;

    protected ServerWithoutVariables(String url) {
        this.url = url;
    }

    public String url(){
        return url;
    }
}

