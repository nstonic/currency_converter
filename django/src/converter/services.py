

import requests
from django.conf import settings


class Converter:

    def __init__(self, currency_rate_source: str = settings.CURRENCY_RATE_SOURCE):
        self.currency_rate_source = currency_rate_source

    def get_rates(self) -> dict:
        response = requests.get(self.currency_rate_source)
        response.raise_for_status()
        return response.json().get('rates') | {'RUB': 1}

    def convert(self, from_: str, to: str, value: int | float) -> float:
        rates = self.get_rates()

        if from_ not in rates or to not in rates:
            raise ValueError('Unknown currency')

        if from_ == to:
            result = value
        else:
            result = rates.get(to, 1) * value / rates.get(from_, 1)

        return round(result, 2)
