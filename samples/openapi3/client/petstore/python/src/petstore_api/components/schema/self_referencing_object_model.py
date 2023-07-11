# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "selfRef": typing.Type['SelfReferencingObjectModel'],
    }
)


class SelfReferencingObjectModelDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selfRef"]) -> SelfReferencingObjectModelDict:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> SelfReferencingObjectModelDict:
        ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["selfRef"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: SelfReferencingObjectModelDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return SelfReferencingObjectModel.validate(arg, configuration=configuration)
SelfReferencingObjectModelDictInput = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            SelfReferencingObjectModelDict,
            dict,
            schemas.immutabledict
        ],
        typing.Union[
            SelfReferencingObjectModelDict,
            dict,
            schemas.immutabledict
        ],
    ]
]


@dataclasses.dataclass(frozen=True)
class SelfReferencingObjectModel(
    schemas.Schema[SelfReferencingObjectModelDict, typing.Tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[SelfReferencingObjectModel] = dataclasses.field(default_factory=lambda: SelfReferencingObjectModel) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: SelfReferencingObjectModelDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            SelfReferencingObjectModelDictInput,
            SelfReferencingObjectModelDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SelfReferencingObjectModelDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

