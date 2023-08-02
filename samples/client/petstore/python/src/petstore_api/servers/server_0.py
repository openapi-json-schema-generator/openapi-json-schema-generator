# coding: utf-8
"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from petstore_api.shared_imports.server_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema


class ServerEnums:

    @schemas.classproperty
    def PETSTORE(cls) -> typing_extensions.Literal["petstore"]:
        return Server.validate("petstore")

    @schemas.classproperty
    def QA_HYPHEN_MINUS_PETSTORE(cls) -> typing_extensions.Literal["qa-petstore"]:
        return Server.validate("qa-petstore")

    @schemas.classproperty
    def DEV_HYPHEN_MINUS_PETSTORE(cls) -> typing_extensions.Literal["dev-petstore"]:
        return Server.validate("dev-petstore")


@dataclasses.dataclass(frozen=True)
class Server(
    schemas.Schema[schemas.immutabledict, str]
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: str = "petstore"
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "petstore": "PETSTORE",
            "qa-petstore": "QA_HYPHEN_MINUS_PETSTORE",
            "dev-petstore": "DEV_HYPHEN_MINUS_PETSTORE",
        }
    )
    enums = ServerEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["petstore"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["petstore"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["qa-petstore"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["qa-petstore"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["dev-petstore"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["dev-petstore"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["petstore","qa-petstore","dev-petstore",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "petstore",
        "qa-petstore",
        "dev-petstore",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "petstore",
                "qa-petstore",
                "dev-petstore",
            ],
            validated_arg
        )


class PortEnums:

    @schemas.classproperty
    def POSITIVE_80(cls) -> typing_extensions.Literal["80"]:
        return Port.validate("80")

    @schemas.classproperty
    def POSITIVE_8080(cls) -> typing_extensions.Literal["8080"]:
        return Port.validate("8080")


@dataclasses.dataclass(frozen=True)
class Port(
    schemas.Schema[schemas.immutabledict, str]
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: str = "80"
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "80": "POSITIVE_80",
            "8080": "POSITIVE_8080",
        }
    )
    enums = PortEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["80"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["80"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["8080"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["8080"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["80","8080",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "80",
        "8080",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "80",
                "8080",
            ],
            validated_arg
        )
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "server": typing.Type[Server],
        "port": typing.Type[Port],
    }
)


class VariablesDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "port",
        "server",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def port(self) -> typing_extensions.Literal["80", "8080"]:
        return typing.cast(
            typing_extensions.Literal["80", "8080"],
            self.__getitem__("port")
        )
    
    @property
    def server(self) -> typing_extensions.Literal["petstore", "qa-petstore", "dev-petstore"]:
        return typing.cast(
            typing_extensions.Literal["petstore", "qa-petstore", "dev-petstore"],
            self.__getitem__("server")
        )

    @staticmethod
    def from_dict_(
        arg: VariablesDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> VariablesDict:
        return Variables.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        port: typing_extensions.Literal["80", "8080"],
        server: typing_extensions.Literal["petstore", "qa-petstore", "dev-petstore"],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_ = {
            "port": port,
            "server": server,
        }
        return Variables.validate(arg_, configuration=configuration_)
VariablesDictInput = typing_extensions.TypedDict(
    'VariablesDictInput',
    {
        "port": str,
        "server": str,
    }
)


@dataclasses.dataclass(frozen=True)
class Variables(
    schemas.Schema[VariablesDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "port",
        "server",
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
class Server0(server.ServerWithVariables):
    '''
    petstore server
    '''
    variables: VariablesDict = dataclasses.field(
        default_factory=lambda: Variables.validate({
            "server": Server.default,
            "port": Port.default,
        })
    )
    variables_schema: typing.Type[Variables] = Variables
    _url: str = "http://{server}.swagger.io:{port}/v2"
