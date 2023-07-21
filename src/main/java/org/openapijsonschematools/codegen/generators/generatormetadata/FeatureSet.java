/*
 * Copyright 2019 OpenAPI-Generator Contributors (https://openapi-generator.tech)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.openapijsonschematools.codegen.generators.generatormetadata;

import org.openapijsonschematools.codegen.generators.generatormetadata.features.ClientModificationFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.ComponentsFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.DataTypeFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.DocumentationFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.GlobalFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.OperationFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.ParameterFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.SchemaFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.SecurityFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.WireFormatFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.annotations.AnnotationType;
import org.slf4j.Logger;

import java.lang.annotation.Annotation;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Defines the feature set for a target generator.
 */
@SuppressWarnings({"unused", "WeakerAccess"})
public class FeatureSet {
    public static FeatureSet UNSPECIFIED = FeatureSet.newBuilder().build();

    private EnumSet<ClientModificationFeature> clientModificationFeatures;
    private EnumSet<DataTypeFeature> dataTypeFeatures;
    private EnumSet<ComponentsFeature> componentsFeatures;
    private EnumSet<DocumentationFeature> documentationFeatures;
    private EnumSet<GlobalFeature> globalFeatures;
    private EnumSet<SchemaFeature> schemaFeatures;
    private EnumSet<ParameterFeature> parameterFeatures;
    private EnumSet<SecurityFeature> securityFeatures;
    private EnumSet<OperationFeature> operationFeatures;
    private EnumSet<WireFormatFeature> wireFormatFeatures;

    private FeatureSet(Builder builder) {
        if (builder != null) {
            clientModificationFeatures = builder.clientModificationFeatures;
            dataTypeFeatures = builder.dataTypeFeatures;
            documentationFeatures = builder.documentationFeatures;
            schemaFeatures = builder.schemaFeatures;
            componentsFeatures = builder.componentsFeatures;
            globalFeatures = builder.globalFeatures;
            parameterFeatures = builder.parameterFeatures;
            securityFeatures = builder.securityFeatures;
            wireFormatFeatures = builder.wireFormatFeatures;
            operationFeatures = builder.operationFeatures;
        }
    }

    public Builder modify() {
        return FeatureSet.newBuilder(this);
    }

    public static Builder newBuilder() {
        return new Builder();
    }

    public static Builder newBuilder(FeatureSet copy) {
        Builder builder = new Builder();
        if (copy != null) {
            builder.clientModificationFeatures = copy.getClientModificationFeatures();
            builder.dataTypeFeatures = copy.getDataTypeFeatures();
            builder.documentationFeatures = copy.getDocumentationFeatures();
            builder.schemaFeatures = copy.getSchemaSupportFeatures();
            builder.globalFeatures = copy.getGlobalFeatures();
            builder.parameterFeatures = copy.getParameterFeatures();
            builder.securityFeatures = copy.getSecurityFeatures();
            builder.wireFormatFeatures = copy.getWireFormatFeatures();
            builder.operationFeatures = copy.getOperationFeatures();
        }
        return builder;
    }

    public EnumSet<OperationFeature> getOperationFeatures() {
        if (operationFeatures != null) {
            return EnumSet.copyOf(operationFeatures);
        } else {
            return EnumSet.noneOf(OperationFeature.class);
        }
    }

    /**
     * Returns the set of client modification features supported by the generator.
     *
     * @return A new copy of the defined feature set. Changes to this instance are not promoted.
     */
    public EnumSet<ClientModificationFeature> getClientModificationFeatures() {
        if (clientModificationFeatures != null) {
            return EnumSet.copyOf(clientModificationFeatures);
        } else {
            return EnumSet.noneOf(ClientModificationFeature.class);
        }
    }

    /**
     * Returns the set of common data types supported by the generator
     *
     * @return A new copy of the defined feature set. Changes to this instance are not promoted.
     */
    public EnumSet<DataTypeFeature> getDataTypeFeatures() {
        if (dataTypeFeatures != null) {
            return EnumSet.copyOf(dataTypeFeatures);
        } else {
            return EnumSet.noneOf(DataTypeFeature.class);
        }
    }

    /**
     * Returns the documentation type available in generated output.
     *
     * @return A new copy of the defined feature set. Changes to this instance are not promoted.
     */
    public EnumSet<DocumentationFeature> getDocumentationFeatures() {
        if (documentationFeatures != null) {
            return EnumSet.copyOf(documentationFeatures);
        } else {
            return EnumSet.noneOf(DocumentationFeature.class);
        }
    }

    /**
     * Returns special circumstances handled by the generator.
     *
     * @return A new copy of the defined feature set. Changes to this instance are not promoted.
     */
    public EnumSet<SchemaFeature> getSchemaSupportFeatures() {
        if (schemaFeatures != null) {
            return EnumSet.copyOf(schemaFeatures);
        } else {
            return EnumSet.noneOf(SchemaFeature.class);
        }
    }

    public EnumSet<ComponentsFeature> getComponentsFeatures() {
        if (componentsFeatures != null) {
            return EnumSet.copyOf(componentsFeatures);
        } else {
            return EnumSet.noneOf(ComponentsFeature.class);
        }
    }

    /**
     * Returns the spec features supported "globally" for a document (shared across all operations and/or models).
     *
     * @return A new copy of the defined feature set. Changes to this instance are not promoted.
     */
    public EnumSet<GlobalFeature> getGlobalFeatures() {
        if (globalFeatures != null) {
            return EnumSet.copyOf(globalFeatures);
        } else {
            return EnumSet.noneOf(GlobalFeature.class);
        }
    }

    /**
     * Returns the types of parameters supported by endpoints in the generated code.
     *
     * @return A new copy of the defined feature set. Changes to this instance are not promoted.
     */
    public EnumSet<ParameterFeature> getParameterFeatures() {
        if (parameterFeatures != null) {
            return EnumSet.copyOf(parameterFeatures);
        } else {
            return EnumSet.noneOf(ParameterFeature.class);
        }
    }

    /**
     * Returns the security features supported in the generated code.
     *
     * @return A new copy of the defined feature set. Changes to this instance are not promoted.
     */
    public EnumSet<SecurityFeature> getSecurityFeatures() {
        if (securityFeatures != null) {
            return EnumSet.copyOf(securityFeatures);
        } else {
            return EnumSet.noneOf(SecurityFeature.class);
        }
    }

    /**
     * Returns the wire format options officially supported by the generated code.
     *
     * @return A new copy of the defined feature set. Changes to this instance are not promoted.
     */
    public EnumSet<WireFormatFeature> getWireFormatFeatures() {
        if (wireFormatFeatures != null) {
            return EnumSet.copyOf(wireFormatFeatures);
        } else {
            return EnumSet.noneOf(WireFormatFeature.class);
        }
    }

    /**
     * Displays a flattened or "normalized" view of the featureSet. This is for simplifying user-facing display only.
     */
    public static class FeatureSetFlattened {
        String featureCategory;
        String featureName;
        boolean isSupported;

        List<AnnotationType> source = new ArrayList<>(3);

        public String getFeatureCategory() {
            return featureCategory;
        }

        public String getFeatureName() {
            return featureName;
        }

        public boolean isSupported() {
            return isSupported;
        }

        public List<AnnotationType> getSource() {
            return Collections.unmodifiableList(source);
        }
    }

    public List<FeatureSetFlattened> flatten(Logger logger) {
        // TODO: Look at making this method function more generically.
        List<FeatureSetFlattened> states = new ArrayList<>();
        EnumSet.allOf(ClientModificationFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = ClientModificationFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.clientModificationFeatures.contains(feat);

            try {
                for (Annotation an : ClientModificationFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }
            states.add(state);
        });
        EnumSet.allOf(DataTypeFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = DataTypeFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.dataTypeFeatures.contains(feat);

            try {
                for (Annotation an : DataTypeFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });
        EnumSet.allOf(DocumentationFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = DocumentationFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.documentationFeatures.contains(feat);

            try {
                for (Annotation an : DocumentationFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });
        EnumSet.allOf(SchemaFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = SchemaFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.schemaFeatures.contains(feat);

            try {
                for (Annotation an : SchemaFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });
        EnumSet.allOf(GlobalFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = GlobalFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.globalFeatures.contains(feat);

            try {
                for (Annotation an : GlobalFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });
        EnumSet.allOf(ComponentsFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = ComponentsFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.componentsFeatures.contains(feat);

            try {
                for (Annotation an : ComponentsFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });
        EnumSet.allOf(ParameterFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = ParameterFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.parameterFeatures.contains(feat);

            try {
                for (Annotation an : ParameterFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });
        EnumSet.allOf(SecurityFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = SecurityFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.securityFeatures.contains(feat);

            try {
                for (Annotation an : SecurityFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });
        EnumSet.allOf(OperationFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = OperationFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.operationFeatures.contains(feat);

            try {
                for (Annotation an : OperationFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });
        EnumSet.allOf(WireFormatFeature.class).forEach(feat -> {
            FeatureSetFlattened state = new FeatureSetFlattened();
            state.featureCategory = WireFormatFeature.class.getSimpleName();
            state.featureName = feat.name();
            state.isSupported = this.wireFormatFeatures.contains(feat);

            try {
                for (Annotation an : WireFormatFeature.class.getField(feat.name()).getAnnotations()) {
                    state.source.add(AnnotationType.fromAnnotation(an.annotationType()));
                }
            } catch (NoSuchFieldException e) {
                logger.error(e.getMessage());
            }

            states.add(state);
        });

        return states;
    }

    /**
     * {@code FeatureSet} builder static inner class.
     */
    public static final class Builder {
        private EnumSet<ClientModificationFeature> clientModificationFeatures;
        private EnumSet<DataTypeFeature> dataTypeFeatures;
        private EnumSet<DocumentationFeature> documentationFeatures;
        private EnumSet<SchemaFeature> schemaFeatures;

        private EnumSet<ComponentsFeature> componentsFeatures;
        private EnumSet<GlobalFeature> globalFeatures;
        private EnumSet<ParameterFeature> parameterFeatures;
        private EnumSet<SecurityFeature> securityFeatures;
        private EnumSet<WireFormatFeature> wireFormatFeatures;

        private EnumSet<OperationFeature> operationFeatures;

        private Builder() {
            this.clientModificationFeatures = EnumSet.noneOf(ClientModificationFeature.class);
            this.dataTypeFeatures = EnumSet.noneOf(DataTypeFeature.class);
            this.documentationFeatures = EnumSet.noneOf(DocumentationFeature.class);
            this.schemaFeatures = EnumSet.noneOf(SchemaFeature.class);
            this.parameterFeatures = EnumSet.noneOf(ParameterFeature.class);
            this.securityFeatures = EnumSet.noneOf(SecurityFeature.class);
            this.globalFeatures = EnumSet.noneOf(GlobalFeature.class);
            this.componentsFeatures = EnumSet.noneOf(ComponentsFeature.class);
            this.wireFormatFeatures = EnumSet.noneOf(WireFormatFeature.class);
            this.operationFeatures = EnumSet.noneOf(OperationFeature.class);
        }

        public Builder operationFeatures(EnumSet<OperationFeature> operationFeatures) {
            if (operationFeatures != null) {
                this.operationFeatures = operationFeatures;
            } else {
                this.operationFeatures = EnumSet.noneOf(OperationFeature.class);
            }
            return this;
        }

        public Builder includeOperationFeatures(OperationFeature... operationFeature) {
            this.operationFeatures.addAll(Arrays.stream(operationFeature).collect(Collectors.toList()));
            return this;
        }

        public Builder excludeOperationFeatures(OperationFeature... operationFeature) {
            this.operationFeatures.removeAll(Arrays.stream(operationFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Sets the {@code clientModificationFeatures} and returns a reference to this Builder so that the methods can be chained together.
         *
         * @param clientModificationFeatures the {@code clientModificationFeatures} to set
         * @return a reference to this Builder
         */
        public Builder clientModificationFeatures(EnumSet<ClientModificationFeature> clientModificationFeatures) {
            if (clientModificationFeatures != null) {
                this.clientModificationFeatures = clientModificationFeatures;
            } else {
                this.clientModificationFeatures = EnumSet.noneOf(ClientModificationFeature.class);
            }
            return this;
        }

        /**
         * Includes the defined {@link ClientModificationFeature} to the new/existing set of supported features.
         *
         * @param clientModificationFeature One or more {@code clientModificationFeature} to ensure are included in the set.
         *
         * @return a reference to this Builder
         */
        public Builder includeClientModificationFeatures(ClientModificationFeature... clientModificationFeature) {
            this.clientModificationFeatures.addAll(Arrays.stream(clientModificationFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Excludes the defined {@link ClientModificationFeature} from the set of supported features.
         *
         * @param clientModificationFeature One or more {@code clientModificationFeature} to ensure are excluded from the set.
         *
         * @return a reference to this Builder
         */
        public Builder excludeClientModificationFeatures(ClientModificationFeature... clientModificationFeature) {
            this.clientModificationFeatures.removeAll(Arrays.stream(clientModificationFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Sets the {@code dataTypeFeatures} and returns a reference to this Builder so that the methods can be chained together.
         *
         * @param dataTypeFeatures the {@code dataTypeFeatures} to set
         * @return a reference to this Builder
         */
        public Builder dataTypeFeatures(EnumSet<DataTypeFeature> dataTypeFeatures) {
            if (dataTypeFeatures != null) {
                this.dataTypeFeatures = dataTypeFeatures;
            } else {
                this.dataTypeFeatures = EnumSet.noneOf(DataTypeFeature.class);
            }
            return this;
        }

        /**
         * Includes the defined {@link DataTypeFeature} to the new/existing set of supported features.
         *
         * @param dataTypeFeature One or more {@code dataTypeFeature} to ensure are included in the set.
         *
         * @return a reference to this Builder
         */
        public Builder includeDataTypeFeatures(DataTypeFeature... dataTypeFeature) {
            this.dataTypeFeatures.addAll(Arrays.stream(dataTypeFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Excludes the defined {@link DataTypeFeature} from the set of supported features.
         *
         * @param dataTypeFeature One or more {@code dataTypeFeature} to ensure are excluded from the set.
         *
         * @return a reference to this Builder
         */
        public Builder excludeDataTypeFeatures(DataTypeFeature... dataTypeFeature) {
            this.dataTypeFeatures.removeAll(Arrays.stream(dataTypeFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Sets the {@code documentationFeature} and returns a reference to this Builder so that the methods can be chained together.
         *
         * @param documentationFeatures the {@code documentationFeature} to set
         * @return a reference to this Builder
         */
        public Builder documentationFeatures(EnumSet<DocumentationFeature> documentationFeatures) {
            if (documentationFeatures != null) {
                this.documentationFeatures = documentationFeatures;
            } else {
                this.documentationFeatures = EnumSet.noneOf(DocumentationFeature.class);
            }
            return this;
        }

        /**
         * Includes the defined {@link DocumentationFeature} to the new/existing set of supported features.
         *
         * @param documentationFeature One or more {@code documentationFeature} to ensure are included in the set.
         *
         * @return a reference to this Builder
         */
        public Builder includeDocumentationFeatures(DocumentationFeature... documentationFeature) {
            this.documentationFeatures.addAll(Arrays.stream(documentationFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Excludes the defined {@link DocumentationFeature} from the set of supported features.
         *
         * @param documentationFeature One or more {@code documentationFeature} to ensure are excluded from the set.
         *
         * @return a reference to this Builder
         */
        public Builder excludeDocumentationFeatures(DocumentationFeature... documentationFeature) {
            this.documentationFeatures.removeAll(Arrays.stream(documentationFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Sets the {@code schemaSupportFeature} and returns a reference to this Builder so that the methods can be chained together.
         *
         * @param schemaFeatures the {@code schemaSupportFeature} to set
         * @return a reference to this Builder
         */
        public Builder schemaFeatures(EnumSet<SchemaFeature> schemaFeatures) {
            if (schemaFeatures != null) {
                this.schemaFeatures = schemaFeatures;
            } else {
                this.schemaFeatures = EnumSet.noneOf(SchemaFeature.class);
            }
            return this;
        }

        /**
         * Includes the defined {@link SchemaFeature} to the new/existing set of supported features.
         *
         * @param schemaFeature One or more {@code schemaFeature} to ensure are included in the set.
         *
         * @return a reference to this Builder
         */
        public Builder includeSchemaFeatures(SchemaFeature... schemaFeature) {
            this.schemaFeatures.addAll(Arrays.stream(schemaFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Excludes the defined {@link SchemaFeature} from the set of supported features.
         *
         * @param schemaFeature One or more {@code schemaFeature} to ensure are excluded from the set.
         *
         * @return a reference to this Builder
         */
        public Builder excludeSchemaFeatures(SchemaFeature... schemaFeature) {
            this.schemaFeatures.removeAll(Arrays.stream(schemaFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Sets the {@code parameterFeature} and returns a reference to this Builder so that the methods can be chained together.
         *
         * @param parameterFeatures the {@code parameterFeature} to set
         * @return a reference to this Builder
         */
        public Builder parameterFeatures(EnumSet<ParameterFeature> parameterFeatures) {
            if (parameterFeatures != null) {
                this.parameterFeatures = parameterFeatures;
            } else {
                this.parameterFeatures = EnumSet.noneOf(ParameterFeature.class);
            }
            return this;
        }

        /**
         * Includes the defined {@link ParameterFeature} to the new/existing set of supported features.
         *
         * @param parameterFeature One or more {@code parameterFeature} to ensure are included in the set.
         *
         * @return a reference to this Builder
         */
        public Builder includeParameterFeatures(ParameterFeature... parameterFeature) {
            this.parameterFeatures.addAll(Arrays.stream(parameterFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Excludes the defined {@link ParameterFeature} from the set of supported features.
         *
         * @param parameterFeature One or more {@code parameterFeature} to ensure are excluded from the set.
         *
         * @return a reference to this Builder
         */
        public Builder excludeParameterFeatures(ParameterFeature... parameterFeature) {
            this.parameterFeatures.removeAll(Arrays.stream(parameterFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Sets the {@code securityFeature} and returns a reference to this Builder so that the methods can be chained together.
         *
         * @param securityFeatures the {@code securityFeatures} to set
         * @return a reference to this Builder
         */
        public Builder securityFeatures(EnumSet<SecurityFeature> securityFeatures) {
            if (securityFeatures != null) {
                this.securityFeatures = securityFeatures;
            } else {
                this.securityFeatures = EnumSet.noneOf(SecurityFeature.class);
            }
            return this;
        }

        /**
         * Includes the defined {@link SecurityFeature} to the new/existing set of supported features.
         *
         * @param securityFeature One or more {@code securityFeature} to ensure are included in the set.
         *
         * @return a reference to this Builder
         */
        public Builder includeSecurityFeatures(SecurityFeature... securityFeature) {
            this.securityFeatures.addAll(Arrays.stream(securityFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Excludes the defined {@link SecurityFeature} from the set of supported features.
         *
         * @param securityFeature One or more {@code securityFeature} to ensure are excluded from the set.
         *
         * @return a reference to this Builder
         */
        public Builder excludeSecurityFeatures(SecurityFeature... securityFeature) {
            this.securityFeatures.removeAll(Arrays.stream(securityFeature).collect(Collectors.toList()));
            return this;
        }

        public Builder componentsFeatures(EnumSet<ComponentsFeature> componentsFeatures) {
            if (componentsFeatures != null) {
                this.componentsFeatures = componentsFeatures;
            } else {
                this.componentsFeatures = EnumSet.noneOf(ComponentsFeature.class);
            }
            return this;
        }

        public Builder includeComponentsFeatures(ComponentsFeature... componentsFeature) {
            this.componentsFeatures.addAll(Arrays.stream(componentsFeature).collect(Collectors.toList()));
            return this;
        }

        public Builder excludeComponentsFeatures(ComponentsFeature... componentsFeature) {
            this.componentsFeatures.removeAll(Arrays.stream(componentsFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Sets the {@code globalFeatures} and return a reference to this Builder so that the methods can be chained together.
         *
         * @param globalFeatures the {@code globalFeatures} to set
         * @return a reference to this Builder
         */
        public Builder globalFeatures(EnumSet<GlobalFeature> globalFeatures) {
            if (globalFeatures != null) {
                this.globalFeatures = globalFeatures;
            } else {
                this.globalFeatures = EnumSet.noneOf(GlobalFeature.class);
            }
            return this;
        }

        /**
         * Includes the defined {@link GlobalFeature} to the new/existing set of supported features.
         *
         * @param globalFeature One or more {@code globalFeatures} to ensure are included in the set.
         *
         * @return a reference to this Builder
         */
        public Builder includeGlobalFeatures(GlobalFeature... globalFeature) {
            this.globalFeatures.addAll(Arrays.stream(globalFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Excludes the defined {@link GlobalFeature} from the set of supported features.
         *
         * @param globalFeature One or more {@code globalFeatures} to ensure are excluded from the set.
         *
         * @return a reference to this Builder
         */
        public Builder excludeGlobalFeatures(GlobalFeature... globalFeature) {
            this.globalFeatures.removeAll(Arrays.stream(globalFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Sets the {@code wireFormatFeatures} and return a reference to this Builder so that the methods can be chained together.
         *
         * @param wireFormatFeatures the {@code wireFormatFeatures} to set
         * @return a reference to this Builder
         */
        public Builder wireFormatFeatures(EnumSet<WireFormatFeature> wireFormatFeatures) {
            if (wireFormatFeatures != null) {
                this.wireFormatFeatures = wireFormatFeatures;
            } else {
                this.wireFormatFeatures = EnumSet.noneOf(WireFormatFeature.class);
            }
            return this;
        }

        /**
         * Includes the defined {@link WireFormatFeature} to the new/existing set of supported features.
         *
         * @param wireFormatFeature One or more {@code wireFormatFeatures} to ensure are included in the set.
         *
         * @return a reference to this Builder
         */
        public Builder includeWireFormatFeatures(WireFormatFeature... wireFormatFeature) {
            this.wireFormatFeatures.addAll(Arrays.stream(wireFormatFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Excludes the defined {@link WireFormatFeature} from the set of supported features.
         *
         * <p>
         * This option should only be used if something is overtly broken or not possible in a generator. Please log a warning if invoking this method.
         * </p>
         *
         * @param wireFormatFeature One or more {@code wireFormatFeatures} to ensure are excluded from the set.
         *
         * @return a reference to this Builder
         */
        public Builder excludeWireFormatFeatures(WireFormatFeature... wireFormatFeature) {
            this.wireFormatFeatures.removeAll(Arrays.stream(wireFormatFeature).collect(Collectors.toList()));
            return this;
        }

        /**
         * Returns a {@code FeatureSet} built from the parameters previously set.
         *
         * @return a {@code FeatureSet} built with parameters of this {@code FeatureSet.Builder}
         */
        public FeatureSet build() {
            return new FeatureSet(this);
        }
    }
}
