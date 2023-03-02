# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
import datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from .. import path
from .responses import response_400
from .parameters import parameter_0
from .parameters import parameter_1



class RequestHeaderParameters:
    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
            'api_key': typing.Union[parameter_0.Parameter0.schema, str, ],
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        parameter_0.Parameter0,
    ]

class RequestPathParameters:
    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
            'petId': typing.Union[parameter_1.Parameter1.schema, decimal.Decimal, int, ],
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        parameter_1.Parameter1,
    ]
_security: typing.List[security_schemes.SecurityRequirementObject] = [
    {
        "petstore_auth": ["write:pets", "read:pets", ],
    },
]


__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '400': response_400.ResponseFor400,
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '400': response_400.ResponseFor400,
}


class BaseApi(api_client.Api):
    @typing.overload
    def _delete_pet(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _delete_pet(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _delete_pet(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _delete_pet(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Deletes a pet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestHeaderParameters.Params, header_params)
        self._verify_typed_dict_inputs(RequestPathParameters.Params, path_params)
        used_path = path

        _path_params = {}
        for parameter in RequestPathParameters.parameters:
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()
        for parameter in RequestHeaderParameters.parameters:
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling

        response = self.api_client.call_api(
            resource_path=used_path,
            method='delete',
            headers=_headers,
            security=_security,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            status = str(response.status)
            if status in _status_code_to_response:
                status: typing_extensions.Literal[
                    '400',
                ]
                api_response = _status_code_to_response[status].deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class DeletePet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names

    @typing.overload
    def delete_pet(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def delete_pet(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def delete_pet(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def delete_pet(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._delete_pet(
            header_params=header_params,
            path_params=path_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForDelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def delete(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def delete(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def delete(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def delete(
        self,
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._delete_pet(
            header_params=header_params,
            path_params=path_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


