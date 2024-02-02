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

package org.openapijsonschematools.codegen.generators.generatormetadata.features;

import org.openapijsonschematools.codegen.generators.generatormetadata.features.annotations.OAS2;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.annotations.OAS3;

/**
 * Defines Operation features supported in the generated code.
 */
public enum OperationFeature {
    @OAS3
    Responses_HttpStatusCode,

    @OAS3
    Responses_RangedResponseCodes,

    @OAS3
    Responses_Default,

    @OAS3
    Responses_RedirectionResponse,

    @OAS2 @OAS3
    Security,

    @OAS3
    Servers,
}
