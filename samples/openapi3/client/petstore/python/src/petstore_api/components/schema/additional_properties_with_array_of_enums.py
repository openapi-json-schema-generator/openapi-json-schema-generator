# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.schema_imports import *


class AdditionalPropertiesWithArrayOfEnums(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        
        class AdditionalProperties(
            schemas.ListSchema
        ):
        
        
            class Schema_:
                types = {tuple}
                
                @staticmethod
                def items() -> typing.Type['enum_class.EnumClass']:
                    return enum_class.EnumClass
        
            def __new__(
                cls,
                arg_: typing.Union[
                    typing.Tuple[
                        typing.Union['enum_class.EnumClass', str], ...
                    ],
                    typing.List[
                        typing.Union['enum_class.EnumClass', str]
                    ],
                ],
                configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
            ) -> 'AdditionalPropertiesWithArrayOfEnums.Schema_.AdditionalProperties':
                return super().__new__(
                    cls,
                    arg_,
                    configuration_=configuration_,
                )
        
            def __getitem__(self, i: int) -> 'enum_class.EnumClass':
                return super().__getitem__(i)
    
    def __getitem__(self, name: str) -> Schema_.AdditionalProperties:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[Schema_.AdditionalProperties, list, tuple],
    ) -> 'AdditionalPropertiesWithArrayOfEnums':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import enum_class
