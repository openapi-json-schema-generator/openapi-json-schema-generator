# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from openapi_client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Bar: typing_extensions.TypeAlias = schemas.IntSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "bar": typing.Type[Bar],
    }
)


class _0Dict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "bar",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        bar: int,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "bar": bar,
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
    def bar(self) -> int:
        return typing.cast(
            int,
            self.__getitem__("bar")
        )
    
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
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: _0Dict,
        }
    )

Foo: typing_extensions.TypeAlias = schemas.StrSchema
Properties2 = typing.TypedDict(
    'Properties2',
    {
        "foo": typing.Type[Foo],
    }
)


class _1Dict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "foo",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        foo: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
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
    def foo(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("foo")
        )
    
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
        "foo",
    })
    properties: Properties2 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties2)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: _1Dict,
        }
    )

AllOf2 = typing.Tuple[
    typing.Type[_0],
    typing.Type[_1],
]


@dataclasses.dataclass(frozen=True)
class Allof(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    all_of: AllOf2 = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AllOf2)) # type: ignore

