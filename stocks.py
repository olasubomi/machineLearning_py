import pandas as pd, numpy as np, time
import os, dotenv
from dotenv import load_dotenv

load_dotenv()
#import matplotlib.pyplot as plt, seaborn as sn
#from decimal import *

##Import robin-stocks module
import robin_stocks
from robin_stocks import *
##robin_stocks documentation: http://www.robin-stocks.com/en/latest/robinhood.html

##Robinhood login credentials
robin_stocks.login(username='olualade1@gmail.com',password='')

##Ignore SettingWithCopyWarning
#import warnings
#from pandas.core.common import SettingWithCopyWarning
#warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

##Change defalut display settings
#pd.set_option("display.max_rows", None, "display.max_columns", None)

def Sma20(symbol='TSLA'):
    sma20=(np.sum((pd.DataFrame(robin_stocks.stocks.get_stock_historicals(symbol, span='year', interval='day'))[::]['close_price'][233:252]).array.astype(float))+\
    float(robin_stocks.stocks.get_latest_price(symbol, includeExtendedHours=False)[0]))/20
    # may need to delete '252' and 'addition of latest price' above to get the full range of past 20 trading days

    print('sma20 price:', sma20)
    print('current price:', float(robin_stocks.stocks.get_latest_price(symbol)[0]))

    run=True 
    t=0
    while run==True:
        if float(robin_stocks.stocks.get_latest_price(symbol)[0]) > sma20:
            print('ALERT, stock is greater than sma20')
        elif t==3:
            print('end after limited iterations')
            break
        else: 
            print('below sma20, wait 5 sec')


        t+=1
        time.sleep(5)

Sma20()

