package org.openapijsonschematools.client.paths.storeorderorderid.delete.parameters;

import org.openapijsonschematools.client.parameter.ParameterStyle;
import org.openapijsonschematools.client.parameter.ParameterInType;
import org.openapijsonschematools.client.parameter.SchemaNonQueryParameter;
import org.openapijsonschematools.client.paths.storeorderorderid.delete.parameters.parameter0.Schema0;

public class Parameter0 {

    public static class Parameter01 extends SchemaNonQueryParameter {
        public Parameter01() {
            super(
                "order_id",
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
