# coding: utf-8
"""
    discriminator-test

    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import abc
import base64
import dataclasses
import enum
import typing
import typing_extensions

from urllib3 import _collections


class SecuritySchemeType(enum.Enum):
    API_KEY = 'apiKey'
    HTTP = 'http'
    MUTUAL_TLS = 'mutualTLS'
    OAUTH_2 = 'oauth2'
    OPENID_CONNECT = 'openIdConnect'


class ApiKeyInLocation(enum.Enum):
    QUERY = 'query'
    HEADER = 'header'
    COOKIE = 'cookie'


class __SecuritySchemeBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apply_auth(
        self,
        headers: _collections.HTTPHeaderDict,
        resource_path: str,
        method: str,
        body: typing.Optional[typing.Union[str, bytes]]
    ) -> None:
        pass


@dataclasses.dataclass
class ApiKeySecurityScheme(__SecuritySchemeBase, abc.ABC):
    api_key: str  # this must be set by the developer
    name: str = ''
    in_location: ApiKeyInLocation = ApiKeyInLocation.QUERY
    type: SecuritySchemeType = SecuritySchemeType.API_KEY

    def apply_auth(
        self,
        headers: _collections.HTTPHeaderDict,
        resource_path: str,
        method: str,
        body: typing.Optional[typing.Union[str, bytes]]
    ) -> None:
        if self.in_location is ApiKeyInLocation.COOKIE:
            headers.add('Cookie', self.api_key)
        elif self.in_location is ApiKeyInLocation.HEADER:
            headers.add(self.name, self.api_key)
        elif self.in_location is ApiKeyInLocation.QUERY:
            # todo add query handling
            raise NotImplementedError("ApiKeySecurityScheme in query not yet implemented")
        return


class HTTPSchemeType(enum.Enum):
    BASIC = 'basic'
    BEARER = 'bearer'
    DIGEST = 'digest'
    SIGNATURE = 'signature' # https://datatracker.ietf.org/doc/draft-cavage-http-signatures/


@dataclasses.dataclass
class HTTPBasicSecurityScheme(__SecuritySchemeBase):
    user_id: str  # user name
    password: str
    scheme: HTTPSchemeType = HTTPSchemeType.BASIC
    encoding: str = 'utf-8'
    type: SecuritySchemeType = SecuritySchemeType.HTTP
    """
    https://www.rfc-editor.org/rfc/rfc7617.html
    """

    def apply_auth(
        self,
        headers: _collections.HTTPHeaderDict,
        resource_path: str,
        method: str,
        body: typing.Optional[typing.Union[str, bytes]]
    ) -> None:
        user_pass = f"{self.user_id}:{self.password}"
        b64_user_pass = base64.b64encode(user_pass.encode(encoding=self.encoding))
        headers.add('Authorization', f"Basic {b64_user_pass.decode()}")


@dataclasses.dataclass
class HTTPBearerSecurityScheme(__SecuritySchemeBase):
    bearer_token: str
    bearer_format: typing.Optional[str] = None
    scheme: HTTPSchemeType = HTTPSchemeType.BEARER
    type: SecuritySchemeType = SecuritySchemeType.HTTP

    def apply_auth(
        self,
        headers: _collections.HTTPHeaderDict,
        resource_path: str,
        method: str,
        body: typing.Optional[typing.Union[str, bytes]]
    ) -> None:
        headers.add('Authorization', f"Bearer {self.bearer_token}")


@dataclasses.dataclass
class HTTPDigestSecurityScheme(__SecuritySchemeBase):
    scheme: HTTPSchemeType = HTTPSchemeType.DIGEST
    type: SecuritySchemeType = SecuritySchemeType.HTTP

    def apply_auth(
        self,
        headers: _collections.HTTPHeaderDict,
        resource_path: str,
        method: str,
        body: typing.Optional[typing.Union[str, bytes]]
    ) -> None:
        raise NotImplementedError("HTTPDigestSecurityScheme not yet implemented")


@dataclasses.dataclass
class MutualTLSSecurityScheme(__SecuritySchemeBase):
    type: SecuritySchemeType = SecuritySchemeType.MUTUAL_TLS

    def apply_auth(
        self,
        headers: _collections.HTTPHeaderDict,
        resource_path: str,
        method: str,
        body: typing.Optional[typing.Union[str, bytes]]
    ) -> None:
        raise NotImplementedError("MutualTLSSecurityScheme not yet implemented")


@dataclasses.dataclass
class ImplicitOAuthFlow:
    authorization_url: str
    scopes: typing.Dict[str, str]
    refresh_url: typing.Optional[str] = None


@dataclasses.dataclass
class TokenUrlOauthFlow:
    token_url: str
    scopes: typing.Dict[str, str]
    refresh_url: typing.Optional[str] = None


@dataclasses.dataclass
class AuthorizationCodeOauthFlow:
    authorization_url: str
    token_url: str
    scopes: typing.Dict[str, str]
    refresh_url: typing.Optional[str] = None


@dataclasses.dataclass
class OAuthFlows:
    implicit: typing.Optional[ImplicitOAuthFlow] = None
    password: typing.Optional[TokenUrlOauthFlow] = None
    client_credentials: typing.Optional[TokenUrlOauthFlow] = None
    authorization_code: typing.Optional[AuthorizationCodeOauthFlow] = None


class OAuth2SecurityScheme(__SecuritySchemeBase, abc.ABC):
    flows: OAuthFlows
    type: SecuritySchemeType = SecuritySchemeType.OAUTH_2

    def apply_auth(
        self,
        headers: _collections.HTTPHeaderDict,
        resource_path: str,
        method: str,
        body: typing.Optional[typing.Union[str, bytes]]
    ) -> None:
        raise NotImplementedError("OAuth2SecurityScheme not yet implemented")


class OpenIdConnectSecurityScheme(__SecuritySchemeBase, abc.ABC):
    openid_connect_url: str
    type: SecuritySchemeType = SecuritySchemeType.OPENID_CONNECT

    def apply_auth(
        self,
        headers: _collections.HTTPHeaderDict,
        resource_path: str,
        method: str,
        body: typing.Optional[typing.Union[str, bytes]]
    ) -> None:
        raise NotImplementedError("OpenIdConnectSecurityScheme not yet implemented")

"""
Key is the Security scheme class
Value is the list of scopes
"""
SecurityRequirementObject = typing_extensions.TypedDict(
    'SecurityRequirementObject',
    {
    }
)