# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class User(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class Properties:
            User = schemas.Int64Schema
            User = schemas.StrSchema
            User = schemas.StrSchema
            User = schemas.StrSchema
            User = schemas.StrSchema
            User = schemas.StrSchema
            User = schemas.StrSchema
            User = schemas.Int32Schema
            User = schemas.DictSchema
            
            
            class User(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
            
                test code generation for nullable objects. Value must be a map of strings to values or the 'null' value.
                """
            
            
                class MetaOapg:
                    types = {
                        schemas.NoneClass,
                        frozendict.frozendict,
                    }
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'User':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            User = schemas.AnyTypeSchema
            
            
            class User(
                schemas.AnyTypeSchema,
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
            
                any type except 'null' Here the 'type' attribute is not specified, which means the value can be anything, including the null value, string, number, boolean, array or object.
                """
            
            
                class MetaOapg:
                    # any type
                    User = schemas.NoneSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'User':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            User = schemas.AnyTypeSchema
            __annotations__ = {
                "id": User,
                "username": User,
                "firstName": User,
                "lastName": User,
                "email": User,
                "password": User,
                "phone": User,
                "userStatus": User,
                "objectWithNoDeclaredProps": User,
                "objectWithNoDeclaredPropsNullable": User,
                "anyTypeProp": User,
                "anyTypeExceptNullProp": User,
                "anyTypePropNullable": User,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userStatus"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectWithNoDeclaredProps"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectWithNoDeclaredPropsNullable"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anyTypeProp"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anyTypeExceptNullProp"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anyTypePropNullable"]) -> MetaOapg.Properties.User: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["id"],
            typing_extensions.Literal["username"],
            typing_extensions.Literal["firstName"],
            typing_extensions.Literal["lastName"],
            typing_extensions.Literal["email"],
            typing_extensions.Literal["password"],
            typing_extensions.Literal["phone"],
            typing_extensions.Literal["userStatus"],
            typing_extensions.Literal["objectWithNoDeclaredProps"],
            typing_extensions.Literal["objectWithNoDeclaredPropsNullable"],
            typing_extensions.Literal["anyTypeProp"],
            typing_extensions.Literal["anyTypeExceptNullProp"],
            typing_extensions.Literal["anyTypePropNullable"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userStatus"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectWithNoDeclaredProps"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectWithNoDeclaredPropsNullable"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anyTypeProp"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anyTypeExceptNullProp"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anyTypePropNullable"]) -> typing.Union[MetaOapg.Properties.User, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal["id"],
            typing_extensions.Literal["username"],
            typing_extensions.Literal["firstName"],
            typing_extensions.Literal["lastName"],
            typing_extensions.Literal["email"],
            typing_extensions.Literal["password"],
            typing_extensions.Literal["phone"],
            typing_extensions.Literal["userStatus"],
            typing_extensions.Literal["objectWithNoDeclaredProps"],
            typing_extensions.Literal["objectWithNoDeclaredPropsNullable"],
            typing_extensions.Literal["anyTypeProp"],
            typing_extensions.Literal["anyTypeExceptNullProp"],
            typing_extensions.Literal["anyTypePropNullable"],
            str
        ]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.Properties.User, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.Properties.User, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.Properties.User, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.Properties.User, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.Properties.User, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.Properties.User, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.Properties.User, str, schemas.Unset] = schemas.unset,
        userStatus: typing.Union[MetaOapg.Properties.User, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        objectWithNoDeclaredProps: typing.Union[MetaOapg.Properties.User, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        objectWithNoDeclaredPropsNullable: typing.Union[MetaOapg.Properties.User, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        anyTypeProp: typing.Union[MetaOapg.Properties.User, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        anyTypeExceptNullProp: typing.Union[MetaOapg.Properties.User, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        anyTypePropNullable: typing.Union[MetaOapg.Properties.User, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *_args,
            id=id,
            username=username,
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password,
            phone=phone,
            userStatus=userStatus,
            objectWithNoDeclaredProps=objectWithNoDeclaredProps,
            objectWithNoDeclaredPropsNullable=objectWithNoDeclaredPropsNullable,
            anyTypeProp=anyTypeProp,
            anyTypeExceptNullProp=anyTypeExceptNullProp,
            anyTypePropNullable=anyTypePropNullable,
            _configuration=_configuration,
            **kwargs,
        )
