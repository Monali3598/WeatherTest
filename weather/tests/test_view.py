import unittest
import json
from unittest import mock
from django.test import Client


class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.api_response = {'coord': {'lon': 72.85, 'lat': 19.01}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}]}


    @mock.patch('weather.views.get_data')
    def test_details(self, get_data):
        get_data.return_value = {"coord": {"lon": 72.85,"lat": 19.01\
        },"weather": [{ "id": 721, "main": "Haze", "description": "haze", "icon": "50n"}]}
        # Issue a GET request.
        response = self.client.get('/search/mumbai/IN')
        # Check that the response is 201 OK.
        self.assertEqual(response.status_code, 201)
        # Check json response
        self.assertEqual(response.json(), self.api_response)