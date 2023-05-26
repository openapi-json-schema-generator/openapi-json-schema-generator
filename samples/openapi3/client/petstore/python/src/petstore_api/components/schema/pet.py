# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class Pet(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    Pet object that needs to be added to the store
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "name",
            "photoUrls",
        }
        
        class Properties:
            Id: typing_extensions.TypeAlias = schemas.Int64Schema[U]
        
            @staticmethod
            def category() -> typing.Type[category.Category]:
                return category.Category
            Name: typing_extensions.TypeAlias = schemas.StrSchema[U]
            
            
            class PhotoUrls(
                schemas.ListSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {tuple}
                    Items: typing_extensions.TypeAlias = schemas.StrSchema[U]
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                Schema_.Items,
                                str
                            ], ...
                        ],
                        typing.List[
                            typing.Union[
                                Schema_.Items,
                                str
                            ]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> Pet.Schema_.Properties.PhotoUrls[tuple]:
                    inst = super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        Pet.Schema_.Properties.PhotoUrls[tuple],
                        inst
                    )
                    return inst
            
                def __getitem__(self, name: int) -> Schema_.Items[str]:
                    return super().__getitem__(name)
            
            
            class Tags(
                schemas.ListSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    @staticmethod
                    def items() -> typing.Type[tag.Tag]:
                        return tag.Tag
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                tag.Tag,
                                dict,
                                frozendict.frozendict
                            ], ...
                        ],
                        typing.List[
                            typing.Union[
                                tag.Tag,
                                dict,
                                frozendict.frozendict
                            ]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> Pet.Schema_.Properties.Tags[tuple]:
                    inst = super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        Pet.Schema_.Properties.Tags[tuple],
                        inst
                    )
                    return inst
            
                def __getitem__(self, name: int) -> tag.Tag[frozendict.frozendict]:
                    return super().__getitem__(name)
            
            
            class Status(
                schemas.StrSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "available": "AVAILABLE",
                        "pending": "PENDING",
                        "sold": "SOLD",
                    }
                
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("available") # type: ignore
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending") # type: ignore
                
                @schemas.classproperty
                def SOLD(cls):
                    return cls("sold") # type: ignore
            __annotations__ = {
                "id": Id,
                "category": category,
                "name": Name,
                "photoUrls": PhotoUrls,
                "tags": Tags,
                "status": Status,
            }
    
    @property
    def name(self) -> Schema_.Properties.Name[str]:
        return self.__getitem__("name")
    
    @property
    def photoUrls(self) -> Schema_.Properties.PhotoUrls[tuple]:
        return self.__getitem__("photoUrls")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> Schema_.Properties.Name[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["photoUrls"]) -> Schema_.Properties.PhotoUrls[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> Schema_.Properties.Id[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> category.Category[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> Schema_.Properties.Tags[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> Schema_.Properties.Status[str]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.AnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["name"],
            typing_extensions.Literal["photoUrls"],
            typing_extensions.Literal["id"],
            typing_extensions.Literal["category"],
            typing_extensions.Literal["tags"],
            typing_extensions.Literal["status"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        name: typing.Union[Schema_.Properties.Name, str],
        photoUrls: typing.Union[Schema_.Properties.PhotoUrls, list, tuple],
        id: typing.Union[Schema_.Properties.Id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        category: typing.Union['category.Category', dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        tags: typing.Union[Schema_.Properties.Tags, list, tuple, schemas.Unset] = schemas.unset,
        status: typing.Union[Schema_.Properties.Status, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> Pet[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            name=name,
            photoUrls=photoUrls,
            id=id,
            category=category,
            tags=tags,
            status=status,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            Pet[frozendict.frozendict],
            inst
        )
        return inst

from petstore_api.components.schema import category
from petstore_api.components.schema import tag
