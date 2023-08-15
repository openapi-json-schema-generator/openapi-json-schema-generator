import typing
import typing_extensions

from this_package.apis.paths.operators import Operators

PathToApi = typing.TypedDict(
    'PathToApi',
    {
    "/operators": typing.Type[Operators],
    }
)

path_to_api = PathToApi(
    {
    "/operators": Operators,
    }
)
