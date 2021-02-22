# getCryptocurrencyRate

仮想通貨のレートを取得するライブラリ<br>
bitflyer.com の WEBAPI を勝手に取得します<br>
対応通貨はBTC XRP ETH XTZ XLM XEM BAT ETC LTC BCH MONA LSK です<br>

# import

```python
from getCryptocurrencyRate import getCryptocurrencyRate
```

# use

```python
getCryptocurrencyRate("BTC_JPY", "hour").get() #取得する通貨 間隔
```

# License

getCryptocurrencyRate is under MIT License
