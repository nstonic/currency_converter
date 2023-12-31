import requests


class Converter:

    def __init__(self, currency_rate_source: str = 'https://www.cbr-xml-daily.ru/latest.js'):
        self.currency_rate_source = currency_rate_source

    def get_rates(self) -> dict:
        response = requests.get(self.currency_rate_source)
        response.raise_for_status()
        return response.json()['rates'] | {'RUB': 1}

    def convert(self, from_: str, to: str, value: int) -> float:
        from_ = from_.upper()
        to = to.upper()
        rates = self.get_rates()

        if from_ not in rates or to not in rates:
            raise ValueError('Unknown currency')

        result = rates[to] * value / rates[from_]

        return round(result, 2)
