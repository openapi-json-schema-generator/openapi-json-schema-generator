import dataclasses
import datetime
import decimal
import io
import numbers
import re
import typing
import typing_extensions
import uuid

from petstore_api import schemas
from petstore_api.configurations import schema_configuration

U = typing.TypeVar('U')
