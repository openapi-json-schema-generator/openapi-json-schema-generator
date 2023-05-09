# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.schema_imports import *


class Tag(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            Id = schemas.Int64Schema
            Name = schemas.StrSchema
            __annotations__ = {
                "id": Id,
                "name": Name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> Schema_.Properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> Schema_.Properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["id"],
            typing_extensions.Literal["name"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        id: typing.Union[Schema_.Properties.Id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[Schema_.Properties.Name, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'Tag':
        return super().__new__(
            cls,
            *args_,
            id=id,
            name=name,
            configuration_=configuration_,
            **kwargs,
        )
