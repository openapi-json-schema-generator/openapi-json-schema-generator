import dataclasses
import typing

import urllib3

from unit_test_api import api_client
from unit_test_api import schemas

from unit_test_api.components.schema import required_default_validation


@dataclasses.dataclass
class ApiResponse(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        required_default_validation.RequiredDefaultValidation,
    ]
    headers: schemas.Unset = schemas.unset


response = api_client.OpenApiResponse(
    response_cls=ApiResponse,
    content={
        'application/json': api_client.MediaType(
            required_default_validation.RequiredDefaultValidation,
        ),
    },
)
