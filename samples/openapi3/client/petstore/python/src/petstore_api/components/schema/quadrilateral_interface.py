# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class ShapeTypeEnums:

    @schemas.classproperty
    def QUADRILATERAL(cls) -> str:
        return ShapeType.validate("Quadrilateral")


@dataclasses.dataclass(frozen=True)
class ShapeType(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "Quadrilateral": "QUADRILATERAL",
        }
    )
    enums = ShapeTypeEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["Quadrilateral"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["Quadrilateral"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["Quadrilateral",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "Quadrilateral",
    ]:
        validated_arg = super().validate(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "Quadrilateral",
            ],
            validated_arg
        )
QuadrilateralType: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "shapeType": typing.Type[ShapeType],
        "quadrilateralType": typing.Type[QuadrilateralType],
    }
)


class QuadrilateralInterfaceDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def quadrilateralType(self) -> str:
        return self.__getitem__("quadrilateralType")
    
    @property
    def shapeType(self) -> str:
        return self.__getitem__("shapeType")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quadrilateralType"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapeType"]) -> str:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["quadrilateralType"],
            typing_extensions.Literal["shapeType"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: QuadrilateralInterfaceDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return QuadrilateralInterface.validate(arg, configuration=configuration)
QuadrilateralInterfaceDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class QuadrilateralInterface(
    schemas.AnyTypeSchema[QuadrilateralInterfaceDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    required: typing.FrozenSet[str] = frozenset({
        "quadrilateralType",
        "shapeType",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: QuadrilateralInterfaceDict,
        }
    )

