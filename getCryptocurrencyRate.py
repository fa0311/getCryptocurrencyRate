import json
from dataclasses import dataclass
from urllib import parse, request

BASE_URL = "https://bitflyer.com/api/app/market/line_chart"


class CryptoCurrencyRate:
    def __init__(self, currency: str = "BTC_JPY", scale: str = "hour"):
        self.currency = currency
        self.scale = scale

    def get(self):
        query: str = parse.urlencode(
            {"product_code": self.currency, "scale": self.scale}
        )
        data: bytes = request.urlopen(f"{BASE_URL}?{query}").read()
        json_data: dict = json.loads(data)
        return CurrencyData(**json_data)


@dataclass
class CurrencyData:
    data: dict = None
    status: int = None
    message: str = None
    errors: str = None

    @property
    def change_str(self):
        return self.data["change_str"]

    @property
    def change_str(self):
        return self.data["change_str"]

    @property
    def change(self):
        return self.data["change"]

    @property
    def price_info_list(self):
        return [PriceInfo(**price) for price in self.data["prices"]]


@dataclass
class PriceInfo:
    price: float
    price_str: str
    timestamp: int
