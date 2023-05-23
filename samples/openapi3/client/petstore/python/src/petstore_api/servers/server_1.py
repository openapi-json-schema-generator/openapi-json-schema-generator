# coding: utf-8
"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.server_imports import *


class _Variables:
    
    
    class Version(
        schemas.StrSchema[schemas.T]
    ):
    
    
        class Schema_:
            types = {
                str,
            }
            default = "v2"
            enum_value_to_name = {
                "v1": "V1",
                "v2": "V2",
            }
        
        @schemas.classproperty
        def V1(cls):
            return cls("v1")
        
        @schemas.classproperty
        def V2(cls):
            return cls("v2")

_VariablesSchemas = typing_extensions.TypedDict(
    '_VariablesSchemas',
    {
        "version": typing.Type[_Variables.Version],
    },
    total=False
)

Variables = typing_extensions.TypedDict(
    'Variables',
    {
        "version": typing_extensions.Literal[
            "v1",
            "v2",
        ],
    },
    total=False
)

def _default_variable_schemas() -> _VariablesSchemas:
    return {
        "version": _Variables.Version,
    }


@dataclasses.dataclass
class Server1(server.Server):
    '''
    The local server
    '''
    variables: typing.Optional[Variables] = None
    variable_schemas: _VariablesSchemas = dataclasses.field(default_factory=_default_variable_schemas)
    _url: str = "https://localhost:8080/{version}"
