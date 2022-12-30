# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
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
from petstore_api.components.responses import response_success_description_only as response_for_200

from .. import path
from . import response_for_404
from . import request_body
from . import parameter_0
from . import parameter_1
from . import parameter_2
from . import parameter_3
from . import parameter_4
from . import parameter_5



class RequestQueryParameters:
    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
            'enum_query_string_array': typing.Union[parameter_2.schema.Schema, list, tuple, ],
            'enum_query_string': typing.Union[parameter_3.schema.Schema, str, ],
            'enum_query_integer': typing.Union[parameter_4.schema.Schema, decimal.Decimal, int, ],
            'enum_query_double': typing.Union[parameter_5.schema.Schema, decimal.Decimal, int, float, ],
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        parameter_2._2,
        parameter_3._3,
        parameter_4._4,
        parameter_5._5,
    ]

class RequestHeaderParameters:
    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
            'enum_header_string_array': typing.Union[parameter_0.schema.Schema, list, tuple, ],
            'enum_header_string': typing.Union[parameter_1.schema.Schema, str, ],
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        parameter_0._0,
        parameter_1._1,
    ]

__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': response_for_200.SuccessDescriptionOnly,
        '404': response_for_404._404,
    }
)
_status_code_to_response = __StatusCodeToResponse({
    '200': response_for_200.SuccessDescriptionOnly,
    '404': response_for_404._404,
})
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _enum_parameters(
        self,
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"] = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...

    @typing.overload
    def _enum_parameters(
        self,
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...


    @typing.overload
    def _enum_parameters(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _enum_parameters(
        self,
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _enum_parameters(
        self,
        content_type: str = 'application/x-www-form-urlencoded',
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        To test enum parameters
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParameters.Params, query_params)
        self._verify_typed_dict_inputs(RequestHeaderParameters.Params, header_params)
        used_path = path

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
            serialized_data = request_body.RequestBody.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            status = str(response.status)
            if status in _status_code_to_response:
                status: typing_extensions.Literal[
                    '200',
                    '404',
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


class EnumParameters(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def enum_parameters(
        self,
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"] = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...

    @typing.overload
    def enum_parameters(
        self,
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...


    @typing.overload
    def enum_parameters(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def enum_parameters(
        self,
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def enum_parameters(
        self,
        content_type: str = 'application/x-www-form-urlencoded',
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._enum_parameters(
            body=body,
            query_params=query_params,
            header_params=header_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"] = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...

    @typing.overload
    def get(
        self,
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
    ]: ...


    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        content_type: str = ...,
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_for_200.ApiResponse,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        content_type: str = 'application/x-www-form-urlencoded',
        body: typing.Union[request_body.application_x_www_form_urlencoded.ApplicationXWwwFormUrlencoded, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        query_params: RequestQueryParameters.Params = frozendict.frozendict(),
        header_params: RequestHeaderParameters.Params = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._enum_parameters(
            body=body,
            query_params=query_params,
            header_params=header_params,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


