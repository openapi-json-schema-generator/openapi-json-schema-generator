# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema
Path: typing_extensions.TypeAlias = schemas.StrSchema
Value: typing_extensions.TypeAlias = schemas.AnyTypeSchema


class OpEnums:

    @schemas.classproperty
    def ADD(cls) -> str:
        return Op.validate("add")

    @schemas.classproperty
    def REPLACE(cls) -> str:
        return Op.validate("replace")

    @schemas.classproperty
    def TEST(cls) -> str:
        return Op.validate("test")


@dataclasses.dataclass(frozen=True)
class Op(
    schemas.Schema[schemas.immutabledict, str]
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "add": "ADD",
            "replace": "REPLACE",
            "test": "TEST",
        }
    )
    enums = OpEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["add"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["add"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["replace"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["replace"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["test"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["test"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["add","replace","test",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "add",
        "replace",
        "test",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "add",
                "replace",
                "test",
            ],
            validated_arg
        )
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "path": typing.Type[Path],
        "value": typing.Type[Value],
        "op": typing.Type[Op],
    }
)


class JSONPatchRequestAddReplaceTestDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "op",
        "path",
        "value",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def get_property(self, name: typing_extensions.Literal["op"]) -> typing_extensions.Literal["add", "replace", "test"]:
        if name == "op":
            return typing.cast(
                typing_extensions.Literal["add", "replace", "test"],
                self.__getitem__(name)
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    @property
    def get_property(self, name: typing_extensions.Literal["path"]) -> str:
        if name == "path":
            return typing.cast(
                str,
                self.__getitem__(name)
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    @property
    def get_property(self, name: typing_extensions.Literal["value"]) -> schemas.OUTPUT_BASE_TYPES:
        if name == "value":
            return typing.cast(
                schemas.OUTPUT_BASE_TYPES,
                self.__getitem__(name)
            )
        raise ValueError(schemas.key_unknown_error_msg(name))

    def __new__(cls, arg: JSONPatchRequestAddReplaceTestDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return JSONPatchRequestAddReplaceTest.validate(arg, configuration=configuration)
JSONPatchRequestAddReplaceTestDictInput = typing_extensions.TypedDict(
    'JSONPatchRequestAddReplaceTestDictInput',
    {
        "op": str,
        "path": str,
        "value": typing.Union[
            dict,
            schemas.immutabledict,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            int,
            float,
            bool,
            None,
            list,
            tuple,
            bytes,
            io.FileIO,
            io.BufferedReader
        ],
    }
)


@dataclasses.dataclass(frozen=True)
class JSONPatchRequestAddReplaceTest(
    schemas.Schema[JSONPatchRequestAddReplaceTestDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "op",
        "path",
        "value",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: JSONPatchRequestAddReplaceTestDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            JSONPatchRequestAddReplaceTestDictInput,
            JSONPatchRequestAddReplaceTestDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> JSONPatchRequestAddReplaceTestDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

