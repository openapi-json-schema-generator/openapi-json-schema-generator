# coding: utf-8
"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *
from petstore_api.shared_imports.server_imports import *
AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema


class VersionEnums:

    @schemas.classproperty
    def V1(cls) -> str:
        return Version.validate("v1")

    @schemas.classproperty
    def V2(cls) -> str:
        return Version.validate("v2")


@dataclasses.dataclass(frozen=True)
class Version(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: str = "v2"
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, bool, schemas.none_type_], str] = dataclasses.field(
        default_factory=lambda: {
            "v1": "V1",
            "v2": "V2",
        }
    )
    enums = VersionEnums
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "version": typing.Type[Version],
    }
)


class VariablesDict(immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def version(self) -> str:
        return self.__getitem__("version")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> str:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["version"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
VariablesDictInput = typing_extensions.TypedDict(
    'VariablesDictInput',
    {
        "version": str,
    }
)


@dataclasses.dataclass(frozen=True)
class Variables(
    schemas.DictSchema[VariablesDict]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
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
            immutabledict.immutabledict: VariablesDict
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
        return super().validate(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass
class Server1(server.ServerWithVariables):
    '''
    The local server
    '''
    variables: VariablesDict = dataclasses.field(
        default_factory=lambda: Variables.validate({
            "version": Version.default,
        })
    )
    variables_schema: typing.Type[Variables] = Variables
    _url: str = "https://localhost:8080/{version}"
