# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class ShapeTypeEnums:

    @schemas.classproperty
    def QUADRILATERAL(cls) -> typing_extensions.Literal["Quadrilateral"]:
        return ShapeType.validate("Quadrilateral")


@dataclasses.dataclass(frozen=True)
class ShapeType(
    schemas.Schema[schemas.immutabledict, str]
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
        validated_arg = super().validate_base(
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


class QuadrilateralInterfaceDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "quadrilateralType",
        "shapeType",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def quadrilateralType(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("quadrilateralType")
        )
    
    @property
    def shapeType(self) -> typing_extensions.Literal["Quadrilateral"]:
        return typing.cast(
            typing_extensions.Literal["Quadrilateral"],
            self.__getitem__("shapeType")
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)

    @staticmethod
    def from_dict_(
        arg: QuadrilateralInterfaceDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QuadrilateralInterfaceDict:
        return QuadrilateralInterface.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        quadrilateralType: str,
        shapeType: typing_extensions.Literal["Quadrilateral"],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_ = {
            "quadrilateralType": quadrilateralType,
            "shapeType": shapeType,
        }
        arg_.update(kwargs)
        return QuadrilateralInterface.validate(arg_, configuration=configuration_)
QuadrilateralInterfaceDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


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

