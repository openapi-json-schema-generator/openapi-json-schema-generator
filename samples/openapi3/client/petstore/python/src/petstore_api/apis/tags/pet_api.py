# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.paths.pet_find_by_status.get.operation import FindPetsByStatus
from petstore_api.paths.pet_find_by_tags.get.operation import FindPetsByTags
from petstore_api.paths.pet_pet_id_upload_image.post.operation import UploadImage
from petstore_api.paths.fake_pet_id_upload_image_with_required_file.post.operation import UploadFileWithRequiredFile
from petstore_api.paths.pet_pet_id.get.operation import GetPetById
from petstore_api.paths.pet_pet_id.post.operation import UpdatePetWithForm
from petstore_api.paths.pet_pet_id.delete.operation import DeletePet
from petstore_api.paths.pet.put.operation import UpdatePet
from petstore_api.paths.pet.post.operation import AddPet


class PetApi(
    FindPetsByStatus,
    FindPetsByTags,
    UploadImage,
    UploadFileWithRequiredFile,
    GetPetById,
    UpdatePetWithForm,
    DeletePet,
    UpdatePet,
    AddPet,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    pass
