package org.openapijsonschematools.client.apis.paths;

import org.openapijsonschematools.client.apiclient.ApiClient;
import org.openapijsonschematools.client.configurations.ApiConfiguration;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.paths.fake.Delete;
import org.openapijsonschematools.client.paths.fake.Get;
import org.openapijsonschematools.client.paths.fake.Patch;
import org.openapijsonschematools.client.paths.fake.Post;

public class Fake extends ApiClient implements
    Delete.DeleteOperation,
    Get.GetOperation,
    Patch.PatchOperation,
    Post.PostOperation
{
    public Fake(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration) {
        super(apiConfiguration, schemaConfiguration);
    }
}