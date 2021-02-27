from datetime import datetime

from getCryptocurrencyRate import CryptoCurrencyRate

product = "BTC_JPY"
# ["BTC_JPY", "XRP_JPY", "ETH_JPY", "XTZ_JPY", "XLM_JPY", "XEM_JPY", "BAT_JPY", "ETC_JPY", "LTC_JPY", "BCH_JPY", "MONA_JPY", "LSK_JPY"]
scale = "hour"
# ["hour","day","week","month","year"]

res = CryptoCurrencyRate(product, scale).get()

print("\n***情報***")
print("リクエストステータス " + str(res.status))
print("現在 " + res.prices_list[-1].price_str + "JPY")
print("推移 " + res.change_str + "%")
print("\n***一覧***")
for price_info in res.price_info_list:
    print(datetime.fromtimestamp(price_info.timestamp))
    print(price_info.price_str + "JPY")
