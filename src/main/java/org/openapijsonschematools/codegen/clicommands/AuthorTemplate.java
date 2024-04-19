package org.openapijsonschematools.codegen.clicommands;

import io.airlift.airline.Command;
import io.airlift.airline.Option;
import org.apache.commons.lang3.StringUtils;
import org.openapijsonschematools.codegen.generators.Generator;
import org.openapijsonschematools.codegen.generators.generatorloader.GeneratorLoader;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.*;
import java.nio.file.spi.FileSystemProvider;
import java.util.*;
import java.util.regex.Pattern;
import java.util.stream.Stream;

@SuppressWarnings({"FieldMayBeFinal", "FieldCanBeLocal", "unused"})
@Command(name = "template", description = "Retrieve templates for local modification")
public class AuthorTemplate extends AbstractCommand {

    private final Logger LOGGER = LoggerFactory.getLogger(AuthorTemplate.class);

    @Option(name = {"-g", "--generator-name"}, title = "generator name",
            description = "generator to use (see list command for list)",
            required = true)
    private String generatorName;

    @Option(name = {"-o", "--output"}, title = "output directory",
            description = "where to write the template files (defaults to 'out')")
    private String output = "";

    @Option(name = {"-v", "--verbose"}, description = "verbose mode")
    private boolean verbose;

    private Pattern pattern = null;

    @Override
    void execute() {
        Generator config = GeneratorLoader.getGenerator(generatorName, null, null);
        String templateDirectory = config.generatorSettings().embeddedTemplateDir;

        log("Requesting '{}' from embedded resource directory '{}'", generatorName, templateDirectory);

        Path embeddedTemplatePath;
        try {
            URI uri = Objects.requireNonNull(this.getClass().getClassLoader().getResource(templateDirectory)).toURI();

            if ("jar".equals(uri.getScheme())) {
                Optional<FileSystemProvider> provider = FileSystemProvider.installedProviders()
                        .stream()
                        .filter(p -> p.getScheme().equalsIgnoreCase("jar"))
                        .findFirst();

                if (!provider.isPresent()) {
                    throw new ProviderNotFoundException("Unable to load jar file system provider");
                }

                try {
                    provider.get().getFileSystem(uri);
                } catch (FileSystemNotFoundException ex) {
                    // File system wasn't loaded, so create it.
                    provider.get().newFileSystem(uri, Collections.emptyMap());
                }
            }

            embeddedTemplatePath = Paths.get(uri);

            log("Copying from jar location {}", embeddedTemplatePath.toAbsolutePath().toString());

            File outputDir;
            if (StringUtils.isNotEmpty(output)) {
                outputDir = new File(output);
            } else {
                outputDir = new File("out");
            }

            Path outputDirPath = outputDir.toPath();
            if (!Files.exists(outputDirPath)) {
                Files.createDirectories(outputDirPath);
            }
            List<Path> generatedFiles = new ArrayList<>();
            try (final Stream<Path> templates = Files.walk(embeddedTemplatePath)) {
                templates.forEach(template -> {
                    log("Found template: {}", template.toAbsolutePath());
                    Path relativePath = embeddedTemplatePath.relativize(template);
                    Path target = outputDirPath.resolve(relativePath.toString());
                    generatedFiles.add(target);
                    try {
                        if (Files.isDirectory(template)) {
                            if (Files.notExists(target)) {
                                log("Creating directory: {}", target.toAbsolutePath());
                                Files.createDirectories(target);
                            }
                        } else {
                            if (target.getParent() != null && Files.notExists(target.getParent())) {
                                log("Creating directory: {}", target.getParent());
                                Files.createDirectories(target.getParent());
                            }
                            log("Copying to: {}", target.toAbsolutePath());
                            Files.copy(template, target, StandardCopyOption.REPLACE_EXISTING);
                        }
                    } catch (IOException e) {
                        LOGGER.error("Unable to create target location '{}'.", target);
                    }
                });
            }

            LOGGER.info("Extracted templates to '{}' directory. Refer to https://openapi-generator.tech/docs/templating for customization details.", outputDirPath);
        } catch (URISyntaxException | IOException e) {
            LOGGER.error("Unable to load embedded template directory.", e);
        }
    }

    private void log(String format, Object... arguments) {
        if (verbose) {
            LOGGER.info(format, arguments);
        }
    }
}
