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
# Obtain cryptocurrencies symbol list
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
    price[crypto_symbol_list[i]]=end_price
