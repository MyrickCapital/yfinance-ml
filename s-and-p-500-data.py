import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import pandas_datareader as pdr


sp500 = pd.read_csv('PATH TO FILE WITH ALL S&P 500 TICKERS')
sp500 = sp500['Symbol'] 

uploaded = []
failed = []

for stonk in sp500:
    try:
        data = yf.download(  # or pdr.get_data_yahoo(...
                tickers = stonk,
                period = "2y",
                interval = "1d",
                group_by = 'ticker',
                auto_adjust = True,
                prepost = True,
                threads = True,
                proxy = None
            )
        data['Ticker'] = stonk
        data.to_csv('PATH TO CREATED FILE', mode='a', header=False)
        uploaded.append(stonk)
    except:
        print('Error for ' + stonk)
        failed.append(stonk)

df = pd.read_csv('PATH TO CREATED FILE')
