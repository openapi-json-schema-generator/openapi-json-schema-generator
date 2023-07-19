# coding: utf-8

# flake8: noqa

"""
Run the tests.
$ pip install nose (optional)
$ cd OpenAPIPetstore-python
$ nosetests -v
"""
from collections import namedtuple
from decimal import Decimal
import json
import typing
import unittest

import urllib3

import petstore_api
from petstore_api import exceptions
from petstore_api import api_client, schemas, api_response
from petstore_api.configurations import schema_configuration


MockResponse = namedtuple('MockResponse', 'data')


class DeserializationTests(unittest.TestCase):
    json_content_type = 'application/json'
    json_content_type_headers = {'content-type': json_content_type}
    configuration = schema_configuration.SchemaConfiguration()

    @classmethod
    def __response(cls, data: typing.Any) -> urllib3.HTTPResponse:
        return urllib3.HTTPResponse(
            json.dumps(data).encode('utf-8'),
            headers=cls.json_content_type_headers
        )

    def test_deserialize_shape(self):
        """

        deserialize Shape to an instance of:
        - EquilateralTriangle
        - IsoscelesTriangle
        - IsoscelesTriangle
        - ScaleneTriangle
        - ComplexQuadrilateral
        - SimpleQuadrilateral
        by traveling through 2 discriminators
        """
        from petstore_api.components.schema import shape, equilateral_triangle
        class ApiResponse(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: shape.Shape
            headers: schemas.Unset

        class MediaType(api_client.MediaType):
            schema = shape.Shape

        class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
            content={
                self.json_content_type: MediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponse(response=response, headers=headers, body=body)

        data = {
            'shapeType': 'Triangle',
            'triangleType': 'EquilateralTriangle',
        }
        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, self.configuration)
        body = deserialized.body
        assert isinstance(body, schemas.immutabledict)
        self.assertEqual(body['shapeType'], 'Triangle')
        self.assertEqual(body['triangleType'], 'EquilateralTriangle')

        # invalid quadrilateralType, second discriminator value
        data = {
            'shapeType': 'Quadrilateral',
            'quadrilateralType': 'Triangle',
        }
        response = self.__response(data)

        err_msg = (
            r"Invalid discriminator value was passed in to Quadrilateral.quadrilateralType Only the values "
            r"\['ComplexQuadrilateral', 'SimpleQuadrilateral'\] are allowed at \('args\[0\]', 'quadrilateralType'\)"
        )
        with self.assertRaisesRegex(petstore_api.ApiValueError, err_msg):
            ResponseFor200.deserialize(response, self.configuration)

    def test_deserialize_animal(self):
        """
        deserialize Animal to a Dog instance
        Animal uses a discriminator which has a map built of child classes
        that inherrit from Animal
        This is the swagger (v2) way of doing something like oneOf composition
        """
        from petstore_api.components.schema import animal, dog
        class ApiResponse(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: animal.Animal
            headers: schemas.Unset

        class MediaType(api_client.MediaType):
            schema=animal.Animal

        class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
            content={
                self.json_content_type: MediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponse(response=response, headers=headers, body=body)

        data = {
            'className': 'Dog',
            'color': 'white',
            'breed': 'Jack Russel Terrier'
        }
        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, self.configuration)
        body = deserialized.body
        assert isinstance(body, animal.AnimalDict)
        self.assertEqual(body['className'], 'Dog')
        self.assertEqual(body['color'], 'white')
        self.assertEqual(body['breed'], 'Jack Russel Terrier')

    def test_regex_constraint(self):
        """
        Test regex pattern validation.
        """
        from petstore_api.components.schema import apple

        # Test with valid regex pattern.
        inst = apple.Apple.validate(
            {'cultivar': "Akane"}
        )
        assert isinstance(inst, apple.AppleDict)

        inst = apple.Apple.validate({
            'cultivar': "Golden Delicious",
            'origin': "cHiLe"
        })
        assert isinstance(inst, apple.AppleDict)

        # Test with invalid regex pattern.
        err_regex = r"Invalid value `.+?`, must match regular expression `.+?` at \('args\[0\]', 'cultivar'\)"
        with self.assertRaisesRegex(
            petstore_api.ApiValueError,
            err_regex
        ):
            inst = apple.Apple.validate({
                'cultivar': "!@#%@$#Akane"
            })

        err_regex = r"Invalid value `.+?`, must match regular expression `.+?` at \('args\[0\]', 'origin'\)"
        with self.assertRaisesRegex(
            petstore_api.ApiValueError,
            err_regex
        ):
            inst = apple.Apple.validate({
                'cultivar': "Golden Delicious",
                'origin': "!@#%@$#Chile"
            })

    def test_deserialize_mammal(self):
        """
        deserialize mammal
        mammal is a oneOf composed schema model with discriminator
        """

        # whale test
        from petstore_api.components.schema import mammal, zebra, whale
        class ApiResponse(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: mammal.Mammal
            headers: schemas.Unset

        class MediaType(api_client.MediaType):
            schema=mammal.Mammal

        class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
            content={
                self.json_content_type: MediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponse(response=response, headers=headers, body=body)

        has_baleen = True
        has_teeth = False
        class_name = 'whale'
        data = {
            'hasBaleen': has_baleen,
            'hasTeeth': has_teeth,
            'className': class_name
        }
        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, self.configuration)
        body = deserialized.body
        assert isinstance(body, schemas.immutabledict)
        self.assertEqual(body['hasBaleen'], has_baleen)
        self.assertEqual(body['hasTeeth'], has_teeth)
        self.assertEqual(body['className'], class_name)

        # zebra test
        zebra_type = 'plains'
        class_name = 'zebra'
        data = {
            'type': zebra_type,
            'className': class_name
        }
        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, self.configuration)
        body = deserialized.body
        assert isinstance(body, schemas.immutabledict)
        self.assertEqual(body['type'], zebra_type)
        self.assertEqual(body['className'], class_name)

    def test_deserialize_float_value(self):
        """
        Deserialize floating point values.
        """
        from petstore_api.components.schema import banana
        class ApiResponse(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: banana.Banana
            headers: schemas.Unset

        class MediaType(api_client.MediaType):
            schema=banana.Banana

        class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
            content={
                self.json_content_type: MediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponse(response=response, headers=headers, body=body)

        data = {
          'lengthCm': 3.1415
        }
        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, self.configuration)
        body = deserialized.body
        assert isinstance(body, banana.BananaDict)
        assert isinstance(body.lengthCm, float)
        self.assertEqual(body.lengthCm, 3.1415)

        """
        Float value is serialized without decimal point
        The client receive it as an integer, which work because Banana.lengthCm is type number without format
        Which accepts int AND float
        """
        data = {
          'lengthCm': 3
        }
        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, self.configuration)
        body = deserialized.body
        assert isinstance(body, banana.BananaDict)
        self.assertTrue(isinstance(body.lengthCm, int))
        self.assertEqual(body.lengthCm, 3)

    def test_deserialize_fruit_null_value(self):
        """
        deserialize fruit with null value.
        fruitReq is a oneOf composed schema model with discriminator, including 'null' type.
        """
        from petstore_api.components.schema import fruit_req
        class ApiResponse(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: fruit_req.FruitReq
            headers: schemas.Unset

        class MediaType(api_client.MediaType):
            schema=fruit_req.FruitReq

        class ResponseFor200(api_client.OpenApiResponse):
            content={
                self.json_content_type: MediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponse(response=response, headers=headers, body=body)

        data = None
        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, self.configuration)
        self.assertTrue(isinstance(deserialized.body, schemas.none_type_))

    def test_deserialize_with_additional_properties(self):
        """
        Deserialize data with schemas that have the additionalProperties keyword.
        Test conditions when additional properties are allowed, not allowed, have
        specific types...
        """

        # Dog is allOf with two child schemas.
        # The OAS document for Dog does not specify the 'additionalProperties' keyword,
        # which means that by default, the Dog schema must allow undeclared properties.
        # The additionalProperties keyword is used to control the handling of extra stuff,
        # that is, properties whose names are not listed in the properties keyword.
        # By default any additional properties are allowed.
        from petstore_api.components.schema import dog, mammal, zebra, banana_req
        data = {
            'className': 'Dog',
            'color': 'brown',
            'breed': 'golden retriever',
            # Below are additional, undeclared properties.
            'group': 'Terrier Group',
            'size': 'medium',
        }
        response = self.__response(data)
        class ApiResponseA(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: dog.Dog
            headers: schemas.Unset

        class ThirdMediaType(api_client.MediaType):
            schema=dog.Dog

        class ResponseFor200A(api_client.OpenApiResponse[ApiResponseA]):
            content={
                self.json_content_type: ThirdMediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponseA(response=response, headers=headers, body=body)

        deserialized = ResponseFor200A.deserialize(response, self.configuration)
        body = deserialized.body
        assert isinstance(body, schemas.immutabledict)
        self.assertEqual(body['className'], 'Dog')
        self.assertEqual(body['color'], 'brown')
        self.assertEqual(body['breed'], 'golden retriever')
        self.assertEqual(body['group'], 'Terrier Group')
        self.assertEqual(body['size'], 'medium')

        # The 'zebra' schema allows additional properties by explicitly setting
        # additionalProperties: true.
        # This is equivalent to 'additionalProperties' not being present.
        data = {
            'className': 'zebra',
            'type': 'plains',
            # Below are additional, undeclared properties
            'group': 'abc',
            'size': 3,
            'p1': True,
            'p2': ['a', 'b', 123],
        }
        response = self.__response(data)
        class ApiResponseB(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: mammal.Mammal
            headers: schemas.Unset

        class SecondMediaType(api_client.MediaType):
            schema=mammal.Mammal

        class ResponseFor200B(api_client.OpenApiResponse[ApiResponseB]):
            content={
                self.json_content_type: SecondMediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponseB(response=response, headers=headers, body=body)


        deserialized = ResponseFor200B.deserialize(response, self.configuration)
        body = deserialized.body
        assert isinstance(body, schemas.immutabledict)
        self.assertEqual(body['className'], 'zebra')
        self.assertEqual(body['type'], 'plains')
        self.assertEqual(body['p1'], True)

        # The 'bananaReq' schema disallows additional properties by explicitly setting
        # additionalProperties: false
        class ApiResponse(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: banana_req.BananaReq
            headers: schemas.Unset

        class MediaType(api_client.MediaType):
            schema=banana_req.BananaReq

        class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
            content={
                self.json_content_type: MediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponse(response=response, headers=headers, body=body)

        with self.assertRaises(
            exceptions.ApiValueError
        ):
            data = {
                'lengthCm': 21.2,
                'sweet': False,
                # Below are additional, undeclared properties. They are not allowed,
                # an exception must be raised.
                'unknown-group': 'abc',
            }
            response = self.__response(data)
            ResponseFor200.deserialize(response, self.configuration)

    def test_deserialize_with_additional_properties_and_reference(self):
        """
        Deserialize data with schemas that has the additionalProperties keyword
        and the schema is specified as a reference ($ref).
        """
        from petstore_api.components.schema import drawing
        class ApiResponse(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: drawing.Drawing
            headers: schemas.Unset

        class MediaType(api_client.MediaType):
            schema=drawing.Drawing

        class ResponseFor200(api_client.OpenApiResponse):
            content={
                self.json_content_type: MediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponse(response=response, headers=headers, body=body)

        data = {
            'mainShape': {
                'shapeType': 'Triangle',
                'triangleType': 'EquilateralTriangle',
            },
            'shapes': [
                {
                    'shapeType': 'Triangle',
                    'triangleType': 'IsoscelesTriangle',
                },
                {
                    'shapeType': 'Quadrilateral',
                    'quadrilateralType': 'ComplexQuadrilateral',
                },
            ],
            'an_additional_prop': {
                'lengthCm': 4,
                'color': 'yellow'
            }
        }
        response = self.__response(data)
        ResponseFor200.deserialize(response, self.configuration)

    def test_deserialize_NumberWithValidations(self):
        from petstore_api.components.schema.number_with_validations import NumberWithValidations
        from petstore_api.paths.fake_refs_number.post.responses import response_200

        # make sure that an exception is thrown on an invalid type value
        with self.assertRaises(petstore_api.ApiTypeError):
            response = self.__response('test str')
            response_200.ResponseFor200.deserialize(response, self.configuration)

        # make sure that an exception is thrown on an invalid value
        with self.assertRaises(petstore_api.ApiValueError):
            response = self.__response(21.0)
            response_200.ResponseFor200.deserialize(response, self.configuration)

        # valid value works
        number_val = 11.0
        response = self.__response(number_val)
        response = response_200.ResponseFor200.deserialize(response, self.configuration)
        self.assertTrue(isinstance(response.body, float))
        self.assertEqual(response.body, number_val)

    def test_array_of_enums(self):
        from petstore_api.components.schema import array_of_enums
        from petstore_api.paths.fake_refs_array_of_enums.post.responses import response_200
        from petstore_api.components.schema import string_enum
        data = ["placed", None]
        response = self.__response(data)
        deserialized = response_200.ResponseFor200.deserialize(response, self.configuration)
        assert isinstance(deserialized.body, array_of_enums.ArrayOfEnumsTuple)
        expected_results = array_of_enums.ArrayOfEnums.validate([string_enum.StringEnum.validate(v) for v in data])
        assert expected_results == deserialized.body

    def test_multiple_of_deserialization(self):
        data = {
            'byte': '3',
            'date': '1970-01-01',
            'password': "abcdefghijkl",
            'integer': 30,
            'number': 65.0,
            'float': 62.4,
        }
        from petstore_api.components.schema import format_test
        class ApiResponse(api_response.ApiResponse):
            response: urllib3.HTTPResponse
            body: format_test.FormatTest
            headers: schemas.Unset

        class MediaType(api_client.MediaType):
            schema=format_test.FormatTest

        class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
            content={
                self.json_content_type: MediaType,
            }
            @classmethod
            def get_response(cls, response, headers, body):
                return ApiResponse(response=response, headers=headers, body=body)

        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, self.configuration)
        assert isinstance(deserialized.body, format_test.FormatTestDict)

        with self.assertRaisesRegex(
            exceptions.ApiValueError,
            r"Invalid value `31`, value must be a multiple of `2` at \('args\[0\]', 'integer'\)"
        ):
            data = {
                'byte': '3',
                'date': '1970-01-01',
                'password': "abcdefghijkl",
                'integer': 31,  # Value is supposed to be multiple of '2'. An error must be raised
                'number': 65.0,
                'float': 62.4,
            }
            response = self.__response(data)
            ResponseFor200.deserialize(response, self.configuration)

        # Disable JSON schema validation. No error should be raised during deserialization.
        configuration = schema_configuration.SchemaConfiguration(
            disabled_json_schema_keywords={"multipleOf"}
        )

        data = {
            'byte': '3',
            'date': '1970-01-01',
            'password': "abcdefghijkl",
            'integer': 31, # Value is supposed to be multiple of '2'
            'number': 65.0,
            'float': 62.4,
        }
        response = self.__response(data)
        deserialized = ResponseFor200.deserialize(response, configuration)
        assert isinstance(deserialized.body, format_test.FormatTestDict)

        # Disable JSON schema validation but for a different keyword.
        # An error should be raised during deserialization.
        configuration = schema_configuration.SchemaConfiguration(
            disabled_json_schema_keywords={"maxItems"}
        )

        with self.assertRaisesRegex(
            exceptions.ApiValueError,
            r"Invalid value `31`, value must be a multiple of `2` at \('args\[0\]', 'integer'\)"
        ):
            data = {
                'byte': '3',
                'date': '1970-01-01',
                'password': "abcdefghijkl",
                'integer': 31, # Value is supposed to be multiple of '2'
                'number': 65.0,
                'float': 62.4,
            }
            response = self.__response(data)
            ResponseFor200.deserialize(response, configuration)
