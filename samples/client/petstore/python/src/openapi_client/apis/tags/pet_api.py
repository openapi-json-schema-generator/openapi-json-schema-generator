# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.paths.pet_find_by_status.get.operation import FindPetsByStatus
from openapi_client.paths.fake_pet_id_upload_image_with_required_file.post.operation import UploadFileWithRequiredFile
from openapi_client.paths.pet.post.operation import AddPet
from openapi_client.paths.pet.put.operation import UpdatePet
from openapi_client.paths.pet_pet_id.delete.operation import DeletePet
from openapi_client.paths.pet_pet_id.get.operation import GetPetById
from openapi_client.paths.pet_pet_id.post.operation import UpdatePetWithForm
from openapi_client.paths.pet_pet_id_upload_image.post.operation import UploadImage
from openapi_client.paths.pet_find_by_tags.get.operation import FindPetsByTags


class PetApi(
    FindPetsByStatus,
    UploadFileWithRequiredFile,
    AddPet,
    UpdatePet,
    DeletePet,
    GetPetById,
    UpdatePetWithForm,
    UploadImage,
    FindPetsByTags,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    pass
