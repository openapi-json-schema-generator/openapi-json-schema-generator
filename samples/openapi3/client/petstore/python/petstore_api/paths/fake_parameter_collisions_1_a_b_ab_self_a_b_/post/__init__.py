# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
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
from . import response_for_200



class RequestQueryParameters:
    class Schemas:
        _1 = schemas.StrSchema
        aB = schemas.StrSchema
        Ab = schemas.StrSchema
        _self = schemas.StrSchema
        a_b = schemas.StrSchema


    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
            '1': typing.Union[Schemas._1, str, ],
            'aB': typing.Union[Schemas.aB, str, ],
            'Ab': typing.Union[Schemas.Ab, str, ],
            'self': typing.Union[Schemas._self, str, ],
            'A-B': typing.Union[Schemas.a_b, str, ],
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        api_client.QueryParameter(
            name="1",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas._1,
            explode=True,
        ),
        api_client.QueryParameter(
            name="aB",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas.aB,
            explode=True,
        ),
        api_client.QueryParameter(
            name="Ab",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas.Ab,
            explode=True,
        ),
        api_client.QueryParameter(
            name="self",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas._self,
            explode=True,
        ),
        api_client.QueryParameter(
            name="A-B",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas.a_b,
            explode=True,
        ),
    ]

class RequestHeaderParameters:
    class Schemas:
        _1 = schemas.StrSchema
        aB = schemas.StrSchema
        _self = schemas.StrSchema
        a_b = schemas.StrSchema


    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
            '1': typing.Union[Schemas._1, str, ],
            'aB': typing.Union[Schemas.aB, str, ],
            'self': typing.Union[Schemas._self, str, ],
            'A-B': typing.Union[Schemas.a_b, str, ],
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        api_client.HeaderParameter(
            name="1",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas._1,
        ),
        api_client.HeaderParameter(
            name="aB",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas.aB,
        ),
        api_client.HeaderParameter(
            name="self",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas._self,
        ),
        api_client.HeaderParameter(
            name="A-B",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas.a_b,
        ),
    ]

class RequestPathParameters:
    class Schemas:
        _1 = schemas.StrSchema
        aB = schemas.StrSchema
        Ab = schemas.StrSchema
        _self = schemas.StrSchema
        a_b = schemas.StrSchema


    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
            '1': typing.Union[Schemas._1, str, ],
            'aB': typing.Union[Schemas.aB, str, ],
            'Ab': typing.Union[Schemas.Ab, str, ],
            'self': typing.Union[Schemas._self, str, ],
            'A-B': typing.Union[Schemas.a_b, str, ],
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
        api_client.PathParameter(
            name="1",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas._1,
            required=True,
        ),
        api_client.PathParameter(
            name="aB",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas.aB,
            required=True,
        ),
        api_client.PathParameter(
            name="Ab",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas.Ab,
            required=True,
        ),
        api_client.PathParameter(
            name="self",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas._self,
            required=True,
        ),
        api_client.PathParameter(
            name="A-B",
            style=api_client.ParameterStyle.SIMPLE,
            schema=Schemas.a_b,
            required=True,
        ),
    ]

class RequestCookieParameters:
    class Schemas:
        _1 = schemas.StrSchema
        aB = schemas.StrSchema
        Ab = schemas.StrSchema
        _self = schemas.StrSchema
        a_b = schemas.StrSchema


    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
            '1': typing.Union[Schemas._1, str, ],
            'aB': typing.Union[Schemas.aB, str, ],
            'Ab': typing.Union[Schemas.Ab, str, ],
            'self': typing.Union[Schemas._self, str, ],
            'A-B': typing.Union[Schemas.a_b, str, ],
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        api_client.CookieParameter(
            name="1",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas._1,
            explode=True,
        ),
        api_client.CookieParameter(
            name="aB",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas.aB,
            explode=True,
        ),
        api_client.CookieParameter(
            name="Ab",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas.Ab,
            explode=True,
        ),
        api_client.CookieParameter(
            name="self",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas._self,
            explode=True,
        ),
        api_client.CookieParameter(
            name="A-B",
            style=api_client.ParameterStyle.FORM,
            schema=Schemas.a_b,
            explode=True,
        ),
    ]

class RequestBody:
    class Schemas:
        application_json = schemas.AnyTypeSchema

    parameter = api_client.RequestBody(
        content={
            'application/json': api_client.MediaType(
                schema=Schemas.application_json
            ),
        },
    )

_status_code_to_response = {
    '200': response_for_200.response,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _parameter_collisions_oapg(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...

    @typing.overload
    def _parameter_collisions_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...


    @typing.overload
    def _parameter_collisions_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _parameter_collisions_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _parameter_collisions_oapg(
        self,
        content_type: str = 'application/json',
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        parameter collision case
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParameters.Params, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParameters.Params, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParameters.Params, path_params)
        self._verify_typed_dict_inputs_oapg(RequestCookieParameters.Params, cookie_params)
        used_path = path.value

        _path_params = {}
        for parameter in RequestPathParameters.parameters:
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in RequestQueryParameters.parameters:
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        for parameter in RequestHeaderParameters.parameters:
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = RequestBody.parameter.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class ParameterCollisions(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def parameter_collisions(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...

    @typing.overload
    def parameter_collisions(
        self,
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...


    @typing.overload
    def parameter_collisions(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def parameter_collisions(
        self,
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def parameter_collisions(
        self,
        content_type: str = 'application/json',
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._parameter_collisions_oapg(
            body=body,
            query_params=query_params,
            header_params=header_params,
            path_params=path_params,
            cookie_params=cookie_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...


    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        content_type: str = 'application/json',
        body: typing.Union[RequestBody.Schemas.application_json, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        path_params: RequestPathParameters.Params = frozendict.frozendict(),
        cookie_params: RequestCookieParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._parameter_collisions_oapg(
            body=body,
            query_params=query_params,
            header_params=header_params,
            path_params=path_params,
            cookie_params=cookie_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


