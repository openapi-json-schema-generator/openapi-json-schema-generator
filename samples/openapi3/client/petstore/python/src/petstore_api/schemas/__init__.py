# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import typing

import typing_extensions

from .schema import (
    get_class,
    none_type_,
    classproperty,
    Bool,
    FileIO,
    Schema,
    SingletonMeta,
    AnyTypeSchema,
    UnsetAnyTypeSchema,
    INPUT_TYPES_ALL
)

from .schemas import (
    ListSchema,
    NoneSchema,
    NumberSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    StrSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BytesSchema,
    FileSchema,
    BinarySchema,
    BoolSchema,
    NotAnyTypeSchema,
    OUTPUT_BASE_TYPES,
    DictSchema
)
from .validation import (
    PatternInfo,
    ValidationMetadata,
    immutabledict
)
from .format import (
    as_date_,
    as_datetime_,
    as_decimal_,
    as_uuid_
)

def typed_dict_to_instance(t_dict: typing_extensions._TypedDictMeta) -> typing.Mapping: # type: ignore
    res = {}
    for key, val in t_dict.__annotations__.items():
        if isinstance(val, typing._GenericAlias): # type: ignore
            # typing.Type[W] -> W
            val_cls = typing_extensions.get_args(val)[0]
            res[key] = val_cls
    return res

X = typing.TypeVar('X', bound=typing.Tuple)

def tuple_to_instance(tup: typing.Type[X]) -> X:
    res = []
    for arg in typing_extensions.get_args(tup):
        if isinstance(arg, typing._GenericAlias): # type: ignore
            # typing.Type[Schema] -> Schema
            arg_cls = typing_extensions.get_args(arg)[0]
            res.append(arg_cls)
    return tuple(res) # type: ignore


class Unset:
    """
    An instance of this class is set as the default value for object type(dict) properties that are optional
    When a property has an unset value, that property will not be assigned in the dict
    """
    pass

unset: Unset = Unset()
