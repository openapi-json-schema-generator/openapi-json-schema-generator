# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class EnumStringEnums:

    @schemas.classproperty
    def UPPER(cls) -> typing.Literal["UPPER"]:
        return EnumString.validate("UPPER")

    @schemas.classproperty
    def LOWER(cls) -> typing.Literal["lower"]:
        return EnumString.validate("lower")

    @schemas.classproperty
    def EMPTY(cls) -> typing.Literal[""]:
        return EnumString.validate("")


@dataclasses.dataclass(frozen=True)
class EnumString(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "UPPER": "UPPER",
            "lower": "LOWER",
            "": "EMPTY",
        }
    )
    enums = EnumStringEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["UPPER"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["UPPER"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["lower"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["lower"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[""],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[""]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["UPPER","lower","",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "UPPER",
        "lower",
        "",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "UPPER",
                "lower",
                "",
            ],
            validated_arg
        )


class EnumStringRequiredEnums:

    @schemas.classproperty
    def UPPER(cls) -> typing.Literal["UPPER"]:
        return EnumStringRequired.validate("UPPER")

    @schemas.classproperty
    def LOWER(cls) -> typing.Literal["lower"]:
        return EnumStringRequired.validate("lower")

    @schemas.classproperty
    def EMPTY(cls) -> typing.Literal[""]:
        return EnumStringRequired.validate("")


@dataclasses.dataclass(frozen=True)
class EnumStringRequired(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "UPPER": "UPPER",
            "lower": "LOWER",
            "": "EMPTY",
        }
    )
    enums = EnumStringRequiredEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["UPPER"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["UPPER"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["lower"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["lower"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[""],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[""]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["UPPER","lower","",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "UPPER",
        "lower",
        "",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "UPPER",
                "lower",
                "",
            ],
            validated_arg
        )


class EnumIntegerEnums:

    @schemas.classproperty
    def POSITIVE_1(cls) -> typing.Literal[1]:
        return EnumInteger.validate(1)

    @schemas.classproperty
    def NEGATIVE_1(cls) -> typing.Literal[-1]:
        return EnumInteger.validate(-1)


@dataclasses.dataclass(frozen=True)
class EnumInteger(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        int,
    })
    format: str = 'int32'
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            1: "POSITIVE_1",
            -1: "NEGATIVE_1",
        }
    )
    enums = EnumIntegerEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[1],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[1]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[-1],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[-1]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[1,-1,]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        1,
        -1,
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                1,
                -1,
            ],
            validated_arg
        )


class EnumNumberEnums:

    @schemas.classproperty
    def POSITIVE_1_PT_1(cls) -> typing.Union[int, float]:
        return EnumNumber.validate(1.1)

    @schemas.classproperty
    def NEGATIVE_1_PT_2(cls) -> typing.Union[int, float]:
        return EnumNumber.validate(-1.2)


@dataclasses.dataclass(frozen=True)
class EnumNumber(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        float,
        int,
    })
    format: str = 'double'
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            1.1: "POSITIVE_1_PT_1",
            -1.2: "NEGATIVE_1_PT_2",
        }
    )
    enums = EnumNumberEnums

    @classmethod
    def validate(
        cls,
        arg: typing.Union[int, float],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Union[int, float]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return validated_arg

from petstore_api.components.schema import integer_enum
from petstore_api.components.schema import integer_enum_one_value
from petstore_api.components.schema import integer_enum_with_default_value
from petstore_api.components.schema import string_enum
from petstore_api.components.schema import string_enum_with_default_value
Properties = typing.TypedDict(
    'Properties',
    {
        "enum_string": typing.Type[EnumString],
        "enum_string_required": typing.Type[EnumStringRequired],
        "enum_integer": typing.Type[EnumInteger],
        "enum_number": typing.Type[EnumNumber],
        "stringEnum": typing.Type[string_enum.StringEnum],
        "IntegerEnum": typing.Type[integer_enum.IntegerEnum],
        "StringEnumWithDefaultValue": typing.Type[string_enum_with_default_value.StringEnumWithDefaultValue],
        "IntegerEnumWithDefaultValue": typing.Type[integer_enum_with_default_value.IntegerEnumWithDefaultValue],
        "IntegerEnumOneValue": typing.Type[integer_enum_one_value.IntegerEnumOneValue],
    }
)


class EnumTestDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "enum_string_required",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "enum_string",
        "enum_integer",
        "enum_number",
        "stringEnum",
        "IntegerEnum",
        "StringEnumWithDefaultValue",
        "IntegerEnumWithDefaultValue",
        "IntegerEnumOneValue",
    })
    
    def __new__(
        cls,
        *,
        enum_string_required: typing.Literal[
            "UPPER",
            "lower",
            ""
        ],
        enum_string: typing.Union[
            typing.Literal[
                "UPPER",
                "lower",
                ""
            ],
            schemas.Unset
        ] = schemas.unset,
        enum_integer: typing.Union[
            typing.Literal[
                1,
                -1
            ],
            schemas.Unset
        ] = schemas.unset,
        enum_number: typing.Union[
            int,
            float,
            schemas.Unset
        ] = schemas.unset,
        stringEnum: typing.Union[
            None,
            typing.Literal[
                "placed",
                "approved",
                "delivered",
                "single quoted",
                "multiple\nlines",
                "double quote \n with newline"
            ],
            schemas.Unset
        ] = schemas.unset,
        IntegerEnum: typing.Union[
            typing.Literal[
                0,
                1,
                2
            ],
            schemas.Unset
        ] = schemas.unset,
        StringEnumWithDefaultValue: typing.Union[
            typing.Literal[
                "placed",
                "approved",
                "delivered"
            ],
            schemas.Unset
        ] = schemas.unset,
        IntegerEnumWithDefaultValue: typing.Union[
            typing.Literal[
                0,
                1,
                2
            ],
            schemas.Unset
        ] = schemas.unset,
        IntegerEnumOneValue: typing.Union[
            typing.Literal[
                0
            ],
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "enum_string_required": enum_string_required,
        }
        for key_, val in (
            ("enum_string", enum_string),
            ("enum_integer", enum_integer),
            ("enum_number", enum_number),
            ("stringEnum", stringEnum),
            ("IntegerEnum", IntegerEnum),
            ("StringEnumWithDefaultValue", StringEnumWithDefaultValue),
            ("IntegerEnumWithDefaultValue", IntegerEnumWithDefaultValue),
            ("IntegerEnumOneValue", IntegerEnumOneValue),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(EnumTestDictInput, arg_)
        return EnumTest.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            EnumTestDictInput,
            EnumTestDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> EnumTestDict:
        return EnumTest.validate(arg, configuration=configuration)
    
    @property
    def enum_string_required(self) -> typing.Literal["UPPER", "lower", ""]:
        return typing.cast(
            typing.Literal["UPPER", "lower", ""],
            self.__getitem__("enum_string_required")
        )
    
    @property
    def enum_string(self) -> typing.Union[typing.Literal["UPPER", "lower", ""], schemas.Unset]:
        val = self.get("enum_string", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal["UPPER", "lower", ""],
            val
        )
    
    @property
    def enum_integer(self) -> typing.Union[typing.Literal[1, -1], schemas.Unset]:
        val = self.get("enum_integer", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal[1, -1],
            val
        )
    
    @property
    def enum_number(self) -> typing.Union[int, float, schemas.Unset]:
        val = self.get("enum_number", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Union[int, float],
            val
        )
    
    @property
    def stringEnum(self) -> typing.Union[
        typing.Union[None, schemas.Unset],
        typing.Union[typing.Literal["placed", "approved", "delivered", "single quoted", "multiple\nlines", "double quote \n with newline"], schemas.Unset],
    ]:
        val = self.get("stringEnum", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Union[
                None,
                typing.Literal["placed", "approved", "delivered", "single quoted", "multiple\nlines", "double quote \n with newline"],
            ],
            val
        )
    
    @property
    def IntegerEnum(self) -> typing.Union[typing.Literal[0, 1, 2], schemas.Unset]:
        val = self.get("IntegerEnum", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal[0, 1, 2],
            val
        )
    
    @property
    def StringEnumWithDefaultValue(self) -> typing.Union[typing.Literal["placed", "approved", "delivered"], schemas.Unset]:
        val = self.get("StringEnumWithDefaultValue", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal["placed", "approved", "delivered"],
            val
        )
    
    @property
    def IntegerEnumWithDefaultValue(self) -> typing.Union[typing.Literal[0, 1, 2], schemas.Unset]:
        val = self.get("IntegerEnumWithDefaultValue", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal[0, 1, 2],
            val
        )
    
    @property
    def IntegerEnumOneValue(self) -> typing.Union[typing.Literal[0], schemas.Unset]:
        val = self.get("IntegerEnumOneValue", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal[0],
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
EnumTestDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class EnumTest(
    schemas.Schema[EnumTestDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "enum_string_required",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: EnumTestDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            EnumTestDictInput,
            EnumTestDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> EnumTestDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

