from getCryptocurrencyRate import getCryptocurrencyRate
from datetime import datetime

product = "BTC_JPY"
# ["BTC_JPY", "XRP_JPY", "ETH_JPY", "XTZ_JPY", "XLM_JPY", "XEM_JPY", "BAT_JPY", "ETC_JPY", "LTC_JPY", "BCH_JPY", "MONA_JPY", "LSK_JPY"]
scale = "hour"
# ["hour","day","week","month","year"]

res = getCryptocurrencyRate(product, scale).get()

print("\n***情報***")
print("リクエストステータス " + str(res.status()))
print("現在 " + res.prices(-1).price_str() + "JPY")
print("推移 " + res.change_str() + "%")
print("\n***一覧***")
for i in range(len(res.prices_list())):
    print(datetime.fromtimestamp(res.prices(i).timestamp()))
    print(res.prices(i).price_str() + "JPY")
