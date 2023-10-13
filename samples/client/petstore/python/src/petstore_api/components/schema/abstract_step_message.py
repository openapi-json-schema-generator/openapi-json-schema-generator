# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Discriminator: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "discriminator": typing.Type[Discriminator],
    }
)


class AbstractStepMessageDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "description",
        "discriminator",
        "sequenceNumber",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        description: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
        discriminator: str,
        sequenceNumber: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "description": description,
            "discriminator": discriminator,
            "sequenceNumber": sequenceNumber,
        }
        arg_.update(kwargs)
        used_arg_ = typing.cast(AbstractStepMessageDictInput, arg_)
        return AbstractStepMessage.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            AbstractStepMessageDictInput,
            AbstractStepMessageDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AbstractStepMessageDict:
        return AbstractStepMessage.validate(arg, configuration=configuration)
    
    @property
    def description(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("description")
    
    @property
    def discriminator(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("discriminator")
        )
    
    @property
    def sequenceNumber(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("sequenceNumber")
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
AbstractStepMessageDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class AbstractStepMessage(
    schemas.Schema[AbstractStepMessageDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    Abstract Step
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "description",
        "discriminator",
        "sequenceNumber",
    })
    discriminator: typing.Mapping[str, typing.Mapping[str, typing.Type[schemas.Schema]]] = dataclasses.field(
        default_factory=lambda: {
            'discriminator': {
                'AbstractStepMessage': AbstractStepMessage,
            }
        }
    )
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    any_of: AnyOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AnyOf)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AbstractStepMessageDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            AbstractStepMessageDictInput,
            AbstractStepMessageDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AbstractStepMessageDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

AnyOf = typing.Tuple[
    typing.Type[AbstractStepMessage],
]
