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


class ObjectWithAllOfWithReqTestPropFromUnsetAddProp(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        # any type
        
        class AllOf:
        
            @staticmethod
            def object_with_all_of_with_req_test_prop_from_unset_add_prop() -> typing.Type['object_with_optional_test_prop.ObjectWithOptionalTestProp']:
                return object_with_optional_test_prop.ObjectWithOptionalTestProp
            
            
            class ObjectWithAllOfWithReqTestPropFromUnsetAddProp(
                schemas.DictSchema
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
                """
            
            
                class MetaOapg:
                    required = {
                        "test",
                    }
                    
                    class Properties:
                        ObjectWithAllOfWithReqTestPropFromUnsetAddProp = schemas.StrSchema
                        __annotations__ = {
                            "name": ObjectWithAllOfWithReqTestPropFromUnsetAddProp,
                        }
                
                test: schemas.AnyTypeSchema
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["test"]) -> schemas.AnyTypeSchema: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.Properties.ObjectWithAllOfWithReqTestPropFromUnsetAddProp: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["test"],
                        typing_extensions.Literal["name"],
                        str
                    ]
                ):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["test"]) -> schemas.AnyTypeSchema: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.Properties.ObjectWithAllOfWithReqTestPropFromUnsetAddProp, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["test"],
                        typing_extensions.Literal["name"],
                        str
                    ]
                ):
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    test: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    name: typing.Union[MetaOapg.Properties.ObjectWithAllOfWithReqTestPropFromUnsetAddProp, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'ObjectWithAllOfWithReqTestPropFromUnsetAddProp':
                    return super().__new__(
                        cls,
                        *_args,
                        test=test,
                        name=name,
                        _configuration=_configuration,
                        **kwargs,
                    )
            classes = [
                object_with_all_of_with_req_test_prop_from_unset_add_prop,
                ObjectWithAllOfWithReqTestPropFromUnsetAddProp,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ObjectWithAllOfWithReqTestPropFromUnsetAddProp':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )
