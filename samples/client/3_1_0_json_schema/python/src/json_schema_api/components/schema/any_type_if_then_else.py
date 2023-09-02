# coding: utf-8

"""
    Example
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from json_schema_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class CountryConst:

    @schemas.classproperty
    def UNITED_STATES_OF_AMERICA(cls) -> typing.Literal["United States of America"]:
        return Country2.validate("United States of America")


@dataclasses.dataclass(frozen=True)
class Country2(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    const_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "United States of America": "UNITED_STATES_OF_AMERICA",
        }
    )
    const = CountryConst

Properties3 = typing.TypedDict(
    'Properties3',
    {
        "country": typing.Type[Country2],
    }
)


class IfDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "country",
    })
    
    def __new__(
        cls,
        *,
        country: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("country", country),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(IfDictInput, arg_)
        return _If.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            IfDictInput,
            IfDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> IfDict:
        return _If.validate(arg, configuration=configuration)
    
    @property
    def country(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("country", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
IfDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class _If(
    schemas.AnyTypeSchema[IfDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    properties: Properties3 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties3)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: IfDict,
        }
    )

StreetAddress: typing_extensions.TypeAlias = schemas.StrSchema


class CountryEnums:

    @schemas.classproperty
    def UNITED_STATES_OF_AMERICA(cls) -> typing.Literal["United States of America"]:
        return Country.validate("United States of America")

    @schemas.classproperty
    def CANADA(cls) -> typing.Literal["Canada"]:
        return Country.validate("Canada")


@dataclasses.dataclass(frozen=True)
class Country(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: typing.Literal["United States of America"] = "United States of America"
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "United States of America": "UNITED_STATES_OF_AMERICA",
            "Canada": "CANADA",
        }
    )
    enums = CountryEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["United States of America"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["United States of America"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["Canada"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["Canada"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["United States of America","Canada",]: ...
    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "United States of America",
        "Canada",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "United States of America",
                "Canada",
            ],
            validated_arg
        )
Properties2 = typing.TypedDict(
    'Properties2',
    {
        "street_address": typing.Type[StreetAddress],
        "country": typing.Type[Country],
    }
)


class AnyTypeIfThenElseDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "street_address",
        "country",
    })
    
    def __new__(
        cls,
        *,
        street_address: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        country: typing.Union[
            typing.Literal[
                "United States of America",
                "Canada"
            ],
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("street_address", street_address),
            ("country", country),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(AnyTypeIfThenElseDictInput, arg_)
        return AnyTypeIfThenElse.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            AnyTypeIfThenElseDictInput,
            AnyTypeIfThenElseDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AnyTypeIfThenElseDict:
        return AnyTypeIfThenElse.validate(arg, configuration=configuration)
    
    @property
    def street_address(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("street_address", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def country(self) -> typing.Union[typing.Literal["United States of America", "Canada"], schemas.Unset]:
        val = self.get("country", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal["United States of America", "Canada"],
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
AnyTypeIfThenElseDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class PostalCode(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    pattern: schemas.PatternInfo = schemas.PatternInfo(
        pattern=r'[0-9]{5}(-[0-9]{4})?'  # noqa: E501
    )
Properties = typing.TypedDict(
    'Properties',
    {
        "postal_code": typing.Type[PostalCode],
    }
)


class ThenDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "postal_code",
    })
    
    def __new__(
        cls,
        *,
        postal_code: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("postal_code", postal_code),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(ThenDictInput, arg_)
        return Then.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            ThenDictInput,
            ThenDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ThenDict:
        return Then.validate(arg, configuration=configuration)
    
    @property
    def postal_code(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("postal_code", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
ThenDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Then(
    schemas.AnyTypeSchema[ThenDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ThenDict,
        }
    )



@dataclasses.dataclass(frozen=True)
class AnyTypeIfThenElse(
    schemas.AnyTypeSchema[AnyTypeIfThenElseDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    properties: Properties2 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties2)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AnyTypeIfThenElseDict,
        }
    )

