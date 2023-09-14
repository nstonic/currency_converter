from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from converter.services import Converter


def mock_get_rates(self):
    return {
        'RUB': 1,
        'USD': 0.01,
    }


class ConverterTestCase(TestCase):
    def test_converter(self):
        Converter.get_rates = mock_get_rates

        assert Converter().convert('RUB', 'USD', '100') == 1
        assert Converter().convert('USD', 'RUB', '100') == 10000
        assert Converter().convert('RUB', 'RUB', '100') == 100
        assert Converter().convert('USD', 'USD', '100') == 100


class RateTestCase(APITestCase):

    def test_rate(self):
        Converter.get_rates = mock_get_rates
        response = self.client.get('/api/rates/usd/rub/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'result': 100.0})

        response = self.client.get('/api/rates?from=USD&to=RUB&value=1', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'result': 100.0})
