package unit_test_api.response;

import java.net.http.HttpResponse;

public interface ApiResponse<SealedBodyOutputClass, HeaderOutputClass> {
    HttpResponse<byte[]> response();
    SealedBodyOutputClass body();
    HeaderOutputClass headers();
}