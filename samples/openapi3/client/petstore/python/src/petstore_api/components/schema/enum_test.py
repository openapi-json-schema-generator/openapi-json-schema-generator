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
    def UPPER(cls) -> str:
        return EnumString.validate("UPPER")

    @schemas.classproperty
    def LOWER(cls) -> str:
        return EnumString.validate("lower")

    @schemas.classproperty
    def EMPTY(cls) -> str:
        return EnumString.validate("")


@dataclasses.dataclass(frozen=True)
class EnumString(
    schemas.Schema[schemas.immutabledict, str]
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
        arg: typing_extensions.Literal["UPPER"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["UPPER"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["lower"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["lower"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal[""],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[""]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["UPPER","lower","",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "UPPER",
        "lower",
        "",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "UPPER",
                "lower",
                "",
            ],
            validated_arg
        )


class EnumStringRequiredEnums:

    @schemas.classproperty
    def UPPER(cls) -> str:
        return EnumStringRequired.validate("UPPER")

    @schemas.classproperty
    def LOWER(cls) -> str:
        return EnumStringRequired.validate("lower")

    @schemas.classproperty
    def EMPTY(cls) -> str:
        return EnumStringRequired.validate("")


@dataclasses.dataclass(frozen=True)
class EnumStringRequired(
    schemas.Schema[schemas.immutabledict, str]
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
        arg: typing_extensions.Literal["UPPER"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["UPPER"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["lower"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["lower"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal[""],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[""]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["UPPER","lower","",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "UPPER",
        "lower",
        "",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "UPPER",
                "lower",
                "",
            ],
            validated_arg
        )


class EnumIntegerEnums:

    @schemas.classproperty
    def POSITIVE_1(cls) -> int:
        return EnumInteger.validate(1)

    @schemas.classproperty
    def NEGATIVE_1(cls) -> int:
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
        arg: typing_extensions.Literal[1],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[1]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal[-1],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[-1]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[1,-1,]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        1,
        -1,
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
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
Properties = typing_extensions.TypedDict(
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
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["enum_string_required"]) -> typing_extensions.Literal["UPPER", "lower", ""]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["enum_string"]) -> typing_extensions.Literal["UPPER", "lower", ""]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["enum_integer"]) -> typing_extensions.Literal[1, -1]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["enum_number"]) -> typing.Union[int, float]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["stringEnum"]) -> typing.Union[
        None,
        typing_extensions.Literal["placed", "approved", "delivered", "single quoted", "multiple\nlines", "double quote \n with newline"],
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["IntegerEnum"]) -> typing_extensions.Literal[0, 1, 2]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["StringEnumWithDefaultValue"]) -> typing_extensions.Literal["placed", "approved", "delivered"]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["IntegerEnumWithDefaultValue"]) -> typing_extensions.Literal[0, 1, 2]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["IntegerEnumOneValue"]) -> typing_extensions.Literal[0]:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "enum_string_required":
            return typing.cast(
                typing_extensions.Literal["UPPER", "lower", ""],
                val
            )
        elif name == "enum_string":
            return val if val is schemas.unset else typing.cast(
                typing_extensions.Literal["UPPER", "lower", ""],
                val
            )
        elif name == "enum_integer":
            return val if val is schemas.unset else typing.cast(
                typing_extensions.Literal[1, -1],
                val
            )
        elif name == "enum_number":
            return val if val is schemas.unset else typing.cast(
                typing.Union[int, float],
                val
            )
        elif name == "stringEnum":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    typing_extensions.Literal["placed", "approved", "delivered", "single quoted", "multiple\nlines", "double quote \n with newline"],
                ],
                val
            )
        elif name == "IntegerEnum":
            return val if val is schemas.unset else typing.cast(
                typing_extensions.Literal[0, 1, 2],
                val
            )
        elif name == "StringEnumWithDefaultValue":
            return val if val is schemas.unset else typing.cast(
                typing_extensions.Literal["placed", "approved", "delivered"],
                val
            )
        elif name == "IntegerEnumWithDefaultValue":
            return val if val is schemas.unset else typing.cast(
                typing_extensions.Literal[0, 1, 2],
                val
            )
        elif name == "IntegerEnumOneValue":
            return val if val is schemas.unset else typing.cast(
                typing_extensions.Literal[0],
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: EnumTestDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return EnumTest.validate(arg, configuration=configuration)
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

