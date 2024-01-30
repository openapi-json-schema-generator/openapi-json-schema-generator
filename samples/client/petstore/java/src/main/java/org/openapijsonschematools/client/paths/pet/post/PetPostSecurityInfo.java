package org.openapijsonschematools.client.paths.pet.post;

import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.paths.pet.post.security.PetPostSecurityRequirementObject0;
import org.openapijsonschematools.client.paths.pet.post.security.PetPostSecurityRequirementObject1;
import org.openapijsonschematools.client.paths.pet.post.security.PetPostSecurityRequirementObject2;
import org.openapijsonschematools.client.securityrequirementobjects.SecurityRequirementObject;
import org.openapijsonschematools.client.securityrequirementobjects.SecurityRequirementObjectProvider;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.AbstractMap;
import java.util.Map;
import java.util.EnumMap;

public class PetPostSecurityInfo implements SecurityRequirementObjectProvider<PetPostSecurityInfo.SecurityIndex> {
    final private Securities securities;
    final private SecurityIndex securityIndex;

    public PetPostSecurityInfo(Securities securities, SecurityIndex securityIndex) {
        this.securities = securities;
        this.securityIndex = securityIndex;
    }

    public static class Securities {
        private final EnumMap<SecurityIndex, @Nullable SecurityRequirementObject> securities;

        // todo make multiple constructors for this use case

        public SecurityRequirementObject get(SecurityIndex securityIndex) {
            @Nullable SecurityRequirementObject securityRequirementObject = get(securityIndex);
            if (securityRequirementObject == null) {
                throw new UnsetPropertyException(securityIndex+" is unset");
            }
            return securityRequirementObject;
        }
    }

    public enum SecurityIndex {
        SECURITY_0,
        SECURITY_1,
        SECURITY_2
    }

    public SecurityRequirementObject getSecurityRequirementObject(@Nullable SecurityIndex securityIndex) {
        if (securityIndex == null) {
            return securities.get(this.securityIndex);
        }
        return securities.get(securityIndex);
    }
}