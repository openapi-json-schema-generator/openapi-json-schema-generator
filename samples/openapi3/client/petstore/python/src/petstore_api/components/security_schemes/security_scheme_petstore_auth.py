# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import dataclasses
import typing
import typing_extensions
from urllib import parse

from petstore_api import security_schemes


@dataclasses.dataclass
class ImplicitOAuthFlow(security_schemes.ImplicitOAuthFlow):
    authorization_url: parse.ParseResult = parse.ParseResult(
        scheme="http",
        netloc="petstore.swagger.io",
        path="/api/oauth/dialog",
        params='',
        query='',
        fragment=''
    )
    scopes: typing.Dict[str, str] = dataclasses.field(default_factory=lambda: {
        "write:pets": "modify pets in your account",
        "read:pets": "read your pets",
    })


class OAuthFlows(security_schemes.OAuthFlows):
    implicit: ImplicitOAuthFlow = ImplicitOAuthFlow()



@dataclasses.dataclass
class PetstoreAuth(security_schemes.OAuth2SecurityScheme):
    '''
    oauth2 implicit flow with two scopes
    '''
    flows: OAuthFlows = OAuthFlows()
