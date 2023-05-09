# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.schema_imports import *


class Schema(
    schemas.DictSchema
):


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "file",
        }
        
        class Properties:
            AdditionalMetadata = schemas.StrSchema
            File = schemas.BinarySchema
            __annotations__ = {
                "additionalMetadata": AdditionalMetadata,
                "file": File,
            }
    
    file: Schema_.Properties.File
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> Schema_.Properties.File: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalMetadata"]) -> Schema_.Properties.AdditionalMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["file"],
            typing_extensions.Literal["additionalMetadata"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        file: typing.Union[Schema_.Properties.File, bytes, io.FileIO, io.BufferedReader],
        additionalMetadata: typing.Union[Schema_.Properties.AdditionalMetadata, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'Schema':
        return super().__new__(
            cls,
            *args_,
            file=file,
            additionalMetadata=additionalMetadata,
            configuration_=configuration_,
            **kwargs,
        )
