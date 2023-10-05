# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class JustSymbolEnums:

    @schemas.classproperty
    def GREATER_THAN_SIGN_EQUALS_SIGN(cls) -> typing.Literal[">="]:
        return JustSymbol.validate(">=")

    @schemas.classproperty
    def DOLLAR_SIGN(cls) -> typing.Literal["$"]:
        return JustSymbol.validate("$")


@dataclasses.dataclass(frozen=True)
class JustSymbol(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            ">=": "GREATER_THAN_SIGN_EQUALS_SIGN",
            "$": "DOLLAR_SIGN",
        }
    )
    enums = JustSymbolEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[">="],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[">="]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["$"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["$"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[">=","$",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        ">=",
        "$",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                ">=",
                "$",
            ],
            validated_arg
        )


class ItemsEnums:

    @schemas.classproperty
    def FISH(cls) -> typing.Literal["fish"]:
        return Items.validate("fish")

    @schemas.classproperty
    def CRAB(cls) -> typing.Literal["crab"]:
        return Items.validate("crab")


@dataclasses.dataclass(frozen=True)
class Items(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "fish": "FISH",
            "crab": "CRAB",
        }
    )
    enums = ItemsEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["fish"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["fish"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["crab"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["crab"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["fish","crab",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "fish",
        "crab",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "fish",
                "crab",
            ],
            validated_arg
        )


class ArrayEnumTuple(
    typing.Tuple[
        typing.Literal["fish", "crab"],
        ...
    ]
):

    def __new__(cls, arg: typing.Union[ArrayEnumTupleInput, ArrayEnumTuple], configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ArrayEnum.validate(arg, configuration=configuration)
ArrayEnumTupleInput = typing.Union[
    typing.List[
        typing.Literal[
            "fish",
            "crab"
        ],
    ],
    typing.Tuple[
        typing.Literal[
            "fish",
            "crab"
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class ArrayEnum(
    schemas.Schema[schemas.immutabledict, ArrayEnumTuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: ArrayEnumTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ArrayEnumTupleInput,
            ArrayEnumTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ArrayEnumTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
Properties = typing.TypedDict(
    'Properties',
    {
        "just_symbol": typing.Type[JustSymbol],
        "array_enum": typing.Type[ArrayEnum],
    }
)


class EnumArraysDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "just_symbol",
        "array_enum",
    })
    
    def __new__(
        cls,
        *,
        just_symbol: typing.Union[
            typing.Literal[
                ">=",
                "$"
            ],
            schemas.Unset
        ] = schemas.unset,
        array_enum: typing.Union[
            ArrayEnumTupleInput,
            ArrayEnumTuple,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("just_symbol", just_symbol),
            ("array_enum", array_enum),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(EnumArraysDictInput, arg_)
        return EnumArrays.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            EnumArraysDictInput,
            EnumArraysDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> EnumArraysDict:
        return EnumArrays.validate(arg, configuration=configuration)
    
    @property
    def just_symbol(self) -> typing.Union[typing.Literal[">=", "$"], schemas.Unset]:
        val = self.get("just_symbol", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal[">=", "$"],
            val
        )
    
    @property
    def array_enum(self) -> typing.Union[ArrayEnumTuple, schemas.Unset]:
        val = self.get("array_enum", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            ArrayEnumTuple,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
EnumArraysDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class EnumArrays(
    schemas.Schema[EnumArraysDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: EnumArraysDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            EnumArraysDictInput,
            EnumArraysDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> EnumArraysDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

