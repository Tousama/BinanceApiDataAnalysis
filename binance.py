# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:21:58 2022

@author: mgune
"""

from binance.client import Client
import pandas as pd
import numpy as np
import timeit


APIKEY=''
APISECRET=''


# =============================================================================
# Connection Api
# =============================================================================
client = Client(APIKEY, APISECRET) 


# =============================================================================
# Obtain cryptocurrencies symbol and price list
# =============================================================================
info = client.get_all_tickers()
crypto_symbol_list=[]
for i in range(len(info)):
    crypto_symbol_list.append(info[i]['symbol'])

# =============================================================================
# Obtain historical price data of cryptocurrencies
# =============================================================================
price={}
for i in range(len(crypto_symbol_list)):
    klines=client.get_klines(symbol=crypto_symbol_list[i],
                             interval="1d", limit="365")
    end_price=[float(entry[4]) for entry in klines]
    #Reverse the price list. The list starts to past, finish to present data. 
    end_price=end_price[::-1]
    price[crypto_symbol_list[i]]=end_price
    

# =============================================================================
# Function of Exponential Moving Avarage
# =============================================================================
def ema(data, num):
    """

    Parameters
    ----------
    data : Data for calculate Ema
    num : Number of Ema's period 

    Returns
    -------
    ema : Exponential moving avarage

    """
    ema=0
    k = 2 / (num+1)
    if ema == 0:
        first_ema = sum(data[-num : -1]) / (num-1)
        ema = data[-1] * k + first_ema * (1-k)
    else:
        ema = data[-1]* k + ema * (1-k)
    return ema


# =============================================================================
# Function of MACD signal
# =============================================================================
def MACD(data):
    """


    Parameters
    ----------
    data : Data for calculate Macd
    
    Returns
    -------
    macdIndicator : signal of Macd

    """
    closeVal = pd.DataFrame(data)
    ema12 = closeVal.ewm(span=12).mean()
    ema26 = closeVal.ewm(span=26).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9).mean()
    macd = macd.values.tolist()
    signal = signal.values.tolist()
    if macd[-1] > signal[-1] and macd[-2] < signal[-2]:
        macdIndicator = 'BUY'
    elif macd[-1] < signal[-1] and macd[-2] > signal[-2]:
        macdIndicator = 'SELL'
    else:
        macdIndicator = 'HOLD'
    return macdIndicator
