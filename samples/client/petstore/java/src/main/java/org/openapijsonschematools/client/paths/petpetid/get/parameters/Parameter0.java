package org.openapijsonschematools.client.paths.petpetid.get.parameters;

import org.openapijsonschematools.client.parameter.ParameterStyle;
import org.openapijsonschematools.client.parameter.ParameterInType;
import org.openapijsonschematools.client.parameter.SchemaNonQueryParameter;
import org.openapijsonschematools.client.paths.petpetid.get.parameters.parameter0.Schema0;

public class Parameter0 {

    public static class Parameter01 extends SchemaNonQueryParameter {
        public Parameter01() {
            super(
                "petId",
                ParameterInType.PATH,
                true,
                ParameterStyle.SIMPLE,
                false,
                false,
                Schema0.Schema01.getInstance()
            );
        }
    }
}
