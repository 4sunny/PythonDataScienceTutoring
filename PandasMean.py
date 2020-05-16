import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime  as dt
import calendar  as cl
#https://stackoverflow.com/questions/44102794/input-missed-values-with-mean-of-nearest-neighbors-in-column#comment75226198_44102947

pd.set_option('display.max_rows', 1000)

dfb = pd.read_csv("Book_Values.csv")
dfb['Date'] = pd.to_datetime(dfb['Date'])

dfb['sum'] = dfb['Amount'].cumsum()
dfb.head()

dfm = pd.read_csv("Market_Values.csv")
month_dict = {name: num for num, name in enumerate(cl.month_abbr) if num}

dfm['Month'] = dfm['Month'].map(month_dict)

dfm['Date'] = pd.to_datetime((dfm['Year']*10000+dfm['Month']*100+1).apply(str),format='%Y%m%d')
dfm['Date'] = pd.to_datetime(dfm['Date'], format="%Y%m") + pd.tseries.offsets.MonthEnd(1)

dfm.head()

dfmp = dfm.set_index('Date')
dfmp['Market_Value'].plot()


dft = dfb.merge(dfm, on=["Date"], how='outer')
dft = dft[['Date', 'sum', 'Market_Value']]
dft.rename(columns={'sum' : 'Book_Value'}, inplace=True)
dft.set_index('Date', inplace=True)
#dft = dft.groupby(['Date']).sum()
dft = dft.loc['2019-01-01':]

dft.sort_index(inplace=True)

#dft.head()
#dftt = dft
#dftt = dftt.reset_index()
#dftt.head(20)
#dfc = dft
#print(dft)

#Easy Way with interpolate function

#dft["Market_Value"] = dft['Market_Value'].interpolate(method="pad")
#print(dftS)
dft.where(dft.values==np.nan, other=(dft.fillna(method='ffill') + dft.fillna(method='bfill'))/2, inplace=True)
#dft = dft.fillna(method='ffill') + dft.fillna(method='bfill'))/2
#dft = dft.replace(to_replace=np.float64(0.0), value=np.nan).isna() == False
print(dft)



'''inValue = 0
inIndex = 0
firstValue = 0
firstIndex = 0
lastValue = 0
lastIndex = 0
inValueFound = False
for i, row in dft.iterrows():
    #This wouldnt work because of duplicate indexes
    #so we have to group by
    currentValue = dfc.loc[i].Market_Value
    if inValueFound == False and pd.isna(currentValue) == False:
        inValue = currentValue
        firstValue = currentValue
        inIndex = i
        firstIndex = i
        inValueFound = True
    elif inValueFound == False and pd.isna(currentValue):
        pass'''