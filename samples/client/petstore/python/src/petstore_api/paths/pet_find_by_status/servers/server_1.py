# coding: utf-8
"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from petstore_api.shared_imports.server_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema


class VersionEnums:

    @schemas.classproperty
    def V1(cls) -> typing.Literal["v1"]:
        return Version.validate("v1")

    @schemas.classproperty
    def V2(cls) -> typing.Literal["v2"]:
        return Version.validate("v2")


@dataclasses.dataclass(frozen=True)
class Version(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: typing.Literal["v1"] = "v1"
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "v1": "V1",
            "v2": "V2",
        }
    )
    enums = VersionEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["v1"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["v1"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["v2"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["v2"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["v1","v2",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "v1",
        "v2",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "v1",
                "v2",
            ],
            validated_arg
        )
Properties = typing.TypedDict(
    'Properties',
    {
        "version": typing.Type[Version],
    }
)


class VariablesDict(schemas.immutabledict[str, typing.Literal["v1", "v2"]]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "version",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        version: typing.Literal[
            "v1",
            "v2"
        ],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "version": version,
        }
        used_arg_ = typing.cast(VariablesDictInput, arg_)
        return Variables.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            VariablesDictInput,
            VariablesDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> VariablesDict:
        return Variables.validate(arg, configuration=configuration)
    
    @property
    def version(self) -> typing.Literal["v1", "v2"]:
        return self.__getitem__("version")
VariablesDictInput = typing.TypedDict(
    'VariablesDictInput',
    {
        "version": typing.Literal[
            "v1",
            "v2"
        ],
    }
)


@dataclasses.dataclass(frozen=True)
class Variables(
    schemas.Schema[VariablesDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "version",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: VariablesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            VariablesDictInput,
            VariablesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> VariablesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass
class Server1(server.ServerWithVariables):
    variables: VariablesDict = dataclasses.field(
        default_factory=lambda: Variables.validate({
            "version": Version.default,
        })
    )
    variables_schema: typing.Type[Variables] = Variables
    _url: str = "https://petstore.swagger.io/{version}"
