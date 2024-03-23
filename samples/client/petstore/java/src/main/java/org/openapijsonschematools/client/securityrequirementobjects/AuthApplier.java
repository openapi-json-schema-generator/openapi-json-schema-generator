package org.openapijsonschematools.client.securityrequirementobjects;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.securityschemes.SecurityScheme;

import java.net.http.HttpRequest;
import java.util.List;
import java.util.Map;

public class AuthApplier {
    protected static void updateParamsForAuth(
        @Nullable SecurityRequirementObject securityRequirementObject,
        Map<String, List<String>> headers,
        String resourcePath,
        String method,
        HttpRequest.BodyPublisher bodyPublisher,
        Map<String, String> queryMap
    ) {
        if (securityRequirementObject == null) {
            return;
        }
        // TODO change securityRequirementObject to be a map of enum to scopes
        // TODO store the SecurityScheme instances in a map in apiConfiguration
        for (Map.Entry<SecurityScheme, List<String>> entry: securityRequirementObject.securitySchemeToScopes.entrySet()) {
            SecurityScheme securityScheme = entry.getKey();
            List<String> scopeNames = entry.getValue();
            securityScheme.applyAuth(
                headers,
                resourcePath,
                method,
                bodyPublisher,
                queryMap,
                scopeNames
            );
        }
    }
}
