package org.openapijsonschematools.client.paths.petfindbytags;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.petfindbytags.get.PetfindbytagsGetSecurityInfo;
import org.openapijsonschematools.client.paths.petfindbytags.get.QueryParameters;
import org.openapijsonschematools.client.paths.petfindbytags.get.Parameters;
import org.openapijsonschematools.client.paths.petfindbytags.get.Responses;

public class Get {

    public static class GetRequest {
        public QueryParameters.QueryParametersMap queryParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
        public PetfindbytagsGetSecurityInfo.@Nullable SecurityIndex securityIndex;

        public GetRequest(
            QueryParameters.QueryParametersMap queryParameters,
            RootServerInfo.@Nullable ServerIndex serverIndex,
            PetfindbytagsGetSecurityInfo.@Nullable SecurityIndex securityIndex
        ) {
            this.queryParameters = queryParameters;
            this.serverIndex = serverIndex;
            this.securityIndex = securityIndex;
        }
    }

    public static class GetNullableRequest {
        public RootServerInfo.@Nullable ServerIndex serverIndex;
        public PetfindbytagsGetSecurityInfo.@Nullable SecurityIndex securityIndex;
        public QueryParameters.@Nullable QueryParametersMap queryParameters;
    }

    public interface SetterForServerIndex <T> {
        GetNullableRequest getInstance();
        T getBuilderAfterServerIndex(GetNullableRequest instance);
        default T serverIndex(RootServerInfo.ServerIndex serverIndex) {
            var instance = getInstance();
            instance.serverIndex = serverIndex;
            return getBuilderAfterServerIndex(instance);
        }
    }

    public interface SetterForSecurityIndex <T> {
        GetNullableRequest getInstance();
        T getBuilderAfterSecurityIndex(GetNullableRequest instance);
        default T securityIndex(PetfindbytagsGetSecurityInfo.SecurityIndex securityIndex) {
            var instance = getInstance();
            instance.securityIndex = securityIndex;
            return getBuilderAfterSecurityIndex(instance);
        }
    }

    public interface SetterForQueryParameters <T> {
        GetNullableRequest getInstance();
        T getBuilderAfterQueryParameters(GetNullableRequest instance);
        default T queryParameters(QueryParameters.QueryParametersMap queryParameters) {
            var instance = getInstance();
            instance.queryParameters = queryParameters;
            return getBuilderAfterQueryParameters(instance);
        }
    }

    public static class Get0RequestBuilder {
        private final GetNullableRequest instance;

        public Get0RequestBuilder(GetNullableRequest instance) {
            this.instance = instance;
        }

        public GetRequest build() {
            // todo casting code here
        }
    }
    public static class GetRequestBuilder {
        private final GetNullableRequest instance;

        public GetRequestBuilder() {
            this.instance = new GetNullableRequest();
        }
    }
}
