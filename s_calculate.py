import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date, timedelta


CONSTANT = {'CCI': 0.015}
WINDOW = {'MACD_1': 12,
          'MACD_2': 26,
          'CCI': 20,
          'CMF': 21}

STOCK = '^NSEI'
START_DATE = str(date.today() - timedelta(700))
TODAY = str(date.today())


def download_data(stock = STOCK, start_date = START_DATE, end_date = TODAY):
	data = yf.download(stock, start_date, end_date)
	return data

def all_indicators(stock_data):
	data = stock_data.copy()
	data['MACD'] = MACD(data)
	data['CCI'] = CCI(data)
	data['CMF'] = CMF(data)
	return data[['Close', 'MACD', 'CCI', 'CMF']]

def MACD(data):
	ema_w1 = data['Close'].ewm(span = WINDOW['MACD_1']).mean()
	ema_w2 = data['Close'].ewm(span = WINDOW['MACD_2']).mean()
	macd = ema_w1 - ema_w2
	return macd

def CCI(data):
	tpt = (data['High'] + data['Low'] + data['Close'])/3
	tpt_sma = tpt.rolling(window = WINDOW['CCI']).mean()
	md_t = np.array([])
	s = 0
	for n in range(WINDOW['CCI']):
	    a = list(abs(tpt_sma - tpt.shift(n)))
	    md_t = np.append(md_t, a)
	md_t = md_t.reshape(WINDOW['CCI'], len(tpt))
	md = np.mean(md_t.T, axis = 1)
	md = pd.Series(md, index = tpt.index)
	cci = (tpt - tpt_sma)/(CONSTANT['CCI'] * md)
	return cci

def CMF(data):
	mf_mul = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (data['High'] - data['Low'])
	mf_vol = mf_mul * data['Volume']
	mf_vol_sma = mf_vol.rolling(window = WINDOW['CMF']).mean()
	vol_sma = data['Volume'].rolling(window = WINDOW['CMF']).mean()
	cmf = mf_vol_sma / vol_sma
	return cmf
