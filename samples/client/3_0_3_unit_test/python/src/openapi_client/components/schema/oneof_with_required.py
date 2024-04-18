# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from openapi_client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class _0Dict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "bar",
        "foo",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        bar: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
        foo: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "bar": bar,
            "foo": foo,
        }
        arg_.update(kwargs)
        used_arg_ = typing.cast(_0DictInput, arg_)
        return _0.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            _0DictInput,
            _0Dict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> _0Dict:
        return _0.validate(arg, configuration=configuration)
    
    @property
    def bar(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("bar")
    
    @property
    def foo(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("foo")
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
_0DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class _0(
    schemas.AnyTypeSchema[_0Dict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    required: typing.FrozenSet[str] = frozenset({
        "bar",
        "foo",
    })
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: _0Dict,
        }
    )



class _1Dict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "baz",
        "foo",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        baz: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
        foo: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "baz": baz,
            "foo": foo,
        }
        arg_.update(kwargs)
        used_arg_ = typing.cast(_1DictInput, arg_)
        return _1.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            _1DictInput,
            _1Dict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> _1Dict:
        return _1.validate(arg, configuration=configuration)
    
    @property
    def baz(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("baz")
    
    @property
    def foo(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("foo")
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
_1DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class _1(
    schemas.AnyTypeSchema[_1Dict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    required: typing.FrozenSet[str] = frozenset({
        "baz",
        "foo",
    })
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: _1Dict,
        }
    )

OneOf = typing.Tuple[
    typing.Type[_0],
    typing.Type[_1],
]


@dataclasses.dataclass(frozen=True)
class OneofWithRequired(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore

    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, schemas.INPUT_TYPES_ALL],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

