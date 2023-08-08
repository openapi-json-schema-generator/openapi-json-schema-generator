# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Id: typing_extensions.TypeAlias = schemas.Int64Schema
Name: typing_extensions.TypeAlias = schemas.StrSchema
Items: typing_extensions.TypeAlias = schemas.StrSchema


class PhotoUrlsTuple(
    typing.Tuple[
        str,
        ...
    ]
):

    def __new__(cls, arg: PhotoUrlsTupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return PhotoUrls.validate(arg, configuration=configuration)
PhotoUrlsTupleInput = typing.Union[
    typing.List[
        str,
    ],
    typing.Tuple[
        str,
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class PhotoUrls(
    schemas.Schema[schemas.immutabledict, PhotoUrlsTuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: PhotoUrlsTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            PhotoUrlsTupleInput,
            PhotoUrlsTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PhotoUrlsTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )


class StatusEnums:

    @schemas.classproperty
    def AVAILABLE(cls) -> typing_extensions.Literal["available"]:
        return Status.validate("available")

    @schemas.classproperty
    def PENDING(cls) -> typing_extensions.Literal["pending"]:
        return Status.validate("pending")

    @schemas.classproperty
    def SOLD(cls) -> typing_extensions.Literal["sold"]:
        return Status.validate("sold")


@dataclasses.dataclass(frozen=True)
class Status(
    schemas.Schema[schemas.immutabledict, str]
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "available": "AVAILABLE",
            "pending": "PENDING",
            "sold": "SOLD",
        }
    )
    enums = StatusEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["available"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["available"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["pending"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["pending"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["sold"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["sold"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["available","pending","sold",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "available",
        "pending",
        "sold",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "available",
                "pending",
                "sold",
            ],
            validated_arg
        )

from petstore_api.components.schema import category
from petstore_api.components.schema import tag


class TagsTuple(
    typing.Tuple[
        tag.TagDict,
        ...
    ]
):

    def __new__(cls, arg: TagsTupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Tags.validate(arg, configuration=configuration)
TagsTupleInput = typing.Union[
    typing.List[
        typing.Union[
            tag.TagDictInput,
            tag.TagDict,
        ],
    ],
    typing.Tuple[
        typing.Union[
            tag.TagDictInput,
            tag.TagDict,
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class Tags(
    schemas.Schema[schemas.immutabledict, TagsTuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[tag.Tag] = dataclasses.field(default_factory=lambda: tag.Tag) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: TagsTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            TagsTupleInput,
            TagsTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> TagsTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "id": typing.Type[Id],
        "category": typing.Type[category.Category],
        "name": typing.Type[Name],
        "photoUrls": typing.Type[PhotoUrls],
        "tags": typing.Type[Tags],
        "status": typing.Type[Status],
    }
)


class PetDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "name",
        "photoUrls",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "id",
        "category",
        "tags",
        "status",
    })
    
    def __new__(
        cls,
        *,
        name: str,
        photoUrls: typing.Union[
            PhotoUrlsTupleInput,
            PhotoUrlsTuple
        ],
        id: typing.Union[
            int,
            schemas.Unset
        ] = schemas.unset,
        category: typing.Union[
            category.CategoryDictInput,
            category.CategoryDict,
            schemas.Unset
        ] = schemas.unset,
        tags: typing.Union[
            TagsTupleInput,
            TagsTuple,
            schemas.Unset
        ] = schemas.unset,
        status: typing.Union[
            typing_extensions.Literal[
                "available",
                "pending",
                "sold"
            ],
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "name": name,
            "photoUrls": photoUrls,
        }
        for key, val in (
            ("id", id),
            ("category", category),
            ("tags", tags),
            ("status", status),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(PetDictInput, arg_)
        return Pet.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            PetDictInput,
            PetDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PetDict:
        return Pet.validate(arg, configuration=configuration)
    
    @property
    def name(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("name")
        )
    
    @property
    def photoUrls(self) -> PhotoUrlsTuple:
        return typing.cast(
            PhotoUrlsTuple,
            self.__getitem__("photoUrls")
        )
    
    @property
    def id(self) -> typing.Union[int, schemas.Unset]:
        val = self.get("id", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            int,
            val
        )
    
    @property
    def category(self) -> typing.Union[category.CategoryDict, schemas.Unset]:
        val = self.get("category", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            category.CategoryDict,
            val
        )
    
    @property
    def tags(self) -> typing.Union[TagsTuple, schemas.Unset]:
        val = self.get("tags", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            TagsTuple,
            val
        )
    
    @property
    def status(self) -> typing.Union[typing_extensions.Literal["available", "pending", "sold"], schemas.Unset]:
        val = self.get("status", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing_extensions.Literal["available", "pending", "sold"],
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
PetDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Pet(
    schemas.Schema[PetDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    Pet object that needs to be added to the store
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "name",
        "photoUrls",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: PetDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            PetDictInput,
            PetDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PetDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

