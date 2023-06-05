# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class SelfReferencingObjectModel(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
        additional_properties: typing.Type[SelfReferencingObjectModel] = dataclasses.field(default_factory=lambda: SelfReferencingObjectModel) # type: ignore
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selfRef"]) -> SelfReferencingObjectModel[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> SelfReferencingObjectModel[frozendict.frozendict]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["selfRef"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        selfRef: typing.Union[
            SelfReferencingObjectModel[frozendict.frozendict],
            schemas.Unset,
            dict,
            frozendict.frozendict
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            SelfReferencingObjectModel[frozendict.frozendict],
            dict,
            frozendict.frozendict
        ],
    ) -> SelfReferencingObjectModel[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            selfRef=selfRef,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            SelfReferencingObjectModel[frozendict.frozendict],
            inst
        )
        return inst

Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "selfRef": typing.Type[SelfReferencingObjectModel],
    }
)