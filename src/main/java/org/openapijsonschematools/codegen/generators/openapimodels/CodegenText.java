package org.openapijsonschematools.codegen.generators.openapimodels;

import com.github.jknack.handlebars.Handlebars;

import java.util.Objects;

public class CodegenText  {
    public final String original;
    public final String codeEscaped;
    public final Handlebars.SafeString originalWithBr;

    public CodegenText(String original, String codeEscaped) {
        this.original = original;
        this.codeEscaped = codeEscaped;
        String escaped = (String) Handlebars.Utils.escapeExpression(original);
        escaped = escaped.replaceAll("(\r\n|\n)", "<br>");
        this.originalWithBr =  new Handlebars.SafeString(escaped);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        CodegenText that = (CodegenText) o;
        return Objects.equals(original, that.original) &&
                Objects.equals(codeEscaped, that.codeEscaped) &&
                Objects.equals(originalWithBr, that.originalWithBr);
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("CodegenText{");
        sb.append("original=").append(original);
        sb.append(", codeEscaped=").append(codeEscaped);
        sb.append(", originalWithBr=").append(originalWithBr);
        sb.append('}');
        return sb.toString();
    }

    @Override
    public int hashCode() {
        return Objects.hash(original, codeEscaped, originalWithBr);
    }
}
