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