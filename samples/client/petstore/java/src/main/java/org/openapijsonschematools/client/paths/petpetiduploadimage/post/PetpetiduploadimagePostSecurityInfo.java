package org.openapijsonschematools.client.paths.petpetiduploadimage.post;

import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.paths.petpetiduploadimage.post.security.PetpetiduploadimagePostSecurityRequirementObject0;
import org.openapijsonschematools.client.securityrequirementobjects.SecurityRequirementObject;
import org.openapijsonschematools.client.securityrequirementobjects.SecurityRequirementObjectProvider;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.AbstractMap;
import java.util.Map;
import java.util.EnumMap;

public class PetpetiduploadimagePostSecurityInfo implements SecurityRequirementObjectProvider<PetpetiduploadimagePostSecurityInfo.SecurityIndex> {
    final private Securities securities;
    final private SecurityIndex securityIndex;

    public PetpetiduploadimagePostSecurityInfo(Securities securities, SecurityIndex securityIndex) {
        this.securities = securities;
        this.securityIndex = securityIndex;
    }

    public interface SetterForPetpetiduploadimagePostSecurityRequirementObject0 <T> {
        Map<SecurityIndex, SecurityRequirementObject> getInstance();
        T getBuilderAfterPetpetiduploadimagePostSecurityRequirementObject0(Map<SecurityIndex, SecurityRequirementObject> instance);
        default T petpetiduploadimagePostSecurityRequirementObject0(PetpetiduploadimagePostSecurityRequirementObject0 security0) {
            var instance = getInstance();
            instance.put(SecurityIndex.SECURITY_0, security0);
            return getBuilderAfterPetpetiduploadimagePostSecurityRequirementObject0(instance);
        }
    }

    public static class Securities {
        private final EnumMap<SecurityIndex, SecurityRequirementObject> securities;

        public Securities(PetpetiduploadimagePostSecurityRequirementObject0 security0) {
            securities = new EnumMap<>(
                Map.ofEntries(
                    new AbstractMap.SimpleEntry<>(
                        SecurityIndex.SECURITY_0,
                        security0
                    )
                )
            );
        }

        public SecurityRequirementObject get(SecurityIndex securityIndex) {
            if (securities.containsKey(securityIndex)) {
                return get(securityIndex);
            }
            throw new UnsetPropertyException(securityIndex+" is unset");
        }
    }

    public enum SecurityIndex {
        SECURITY_0
    }

    public SecurityRequirementObject getSecurityRequirementObject(@Nullable SecurityIndex securityIndex) {
        if (securityIndex == null) {
            return securities.get(this.securityIndex);
        }
        return securities.get(securityIndex);
    }
}