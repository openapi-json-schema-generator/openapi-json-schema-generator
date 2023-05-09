# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.schema_imports import *


class ObjectModelWithArgAndArgsProperties(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "arg",
            "args",
        }
        
        class Properties:
            Arg = schemas.StrSchema
            Args = schemas.StrSchema
            __annotations__ = {
                "arg": Arg,
                "args": Args,
            }
    
    @property
    def arg(self) -> Schema_.Properties.Arg:
        return self.__getitem__("arg")
    
    @property
    def args(self) -> Schema_.Properties.Args:
        return self.__getitem__("args")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["arg"]) -> Schema_.Properties.Arg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["args"]) -> Schema_.Properties.Args: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["arg"],
            typing_extensions.Literal["args"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        arg: typing.Union[Schema_.Properties.Arg, str],
        args: typing.Union[Schema_.Properties.Args, str],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ObjectModelWithArgAndArgsProperties':
        return super().__new__(
            cls,
            *args_,
            arg=arg,
            args=args,
            configuration_=configuration_,
            **kwargs,
        )
