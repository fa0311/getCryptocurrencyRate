import urllib.parse
import urllib.request
import json


class getCryptocurrencyRate:
    def __init__(self, product_code='BTC_JPY', scale='hour'):
        self.url = 'https://bitflyer.com/api/app/market/line_chart'
        self.product_code = product_code
        self.scale = scale

    def get(self):
        param = {
            'product_code': self.product_code,
            'scale': self.scale
        }
        paramStr = urllib.parse.urlencode(param)
        readObj = urllib.request.urlopen(self.url + "?" + paramStr)
        response = readObj.read()
        data = json.loads(response)
        return self.parse(data)

    class parse:
        def __init__(self, data):
            self.data = data

        def status(self):
            return self.data["status"]

        def label(self):
            return self.data["label"]

        def message(self):
            return self.data["message"]

        def errors(self):
            return self.data["errors"]

        def change_str(self):
            return self.data["data"]["change_str"]

        def change(self):
            return self.data["data"]["change"]

        def prices_list(self):
            return self.data["data"]["prices"]

        def prices(self, i):
            return self.parse(self.data["data"]["prices"][i])

        class parse:
            def __init__(self, data):
                self.data = data

            def price(self):
                return self.data["price"]

            def price_str(self):
                return self.data["price_str"]

            def timestamp(self):
                return self.data["timestamp"]
