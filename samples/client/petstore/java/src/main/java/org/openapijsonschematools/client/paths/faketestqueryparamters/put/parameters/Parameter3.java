package org.openapijsonschematools.client.paths.faketestqueryparamters.put.parameters;

import org.openapijsonschematools.client.parameter.ParameterStyle;
import org.openapijsonschematools.client.parameter.ParameterInType;
import org.openapijsonschematools.client.parameter.SchemaParameter;
import org.openapijsonschematools.client.paths.faketestqueryparamters.put.parameters.parameter3.Schema3;

public class Parameter3 {

    public static class Parameter31 extends SchemaParameter {
        public Parameter31() {
            super(
                "url",
                ParameterInType.QUERY,
                true,
                ParameterStyle.FORM,
                false,
                false,
                Schema3.Schema31.getInstance()
            );
        }
    }
}
