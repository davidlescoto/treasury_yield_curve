import pandas as pd
from datetime import datetime as dt

from functions import  fed_svensson_rate

class Yield_Curve:
    
    def __init__(self):
        self.data = pd.read_csv('data/data_params.csv', index_col = 'Date')
        self.data.index = pd.DatetimeIndex(self.data.index)


    def svensson_rate(self, days = 365, date = None):

        if date == None:
            params = self.data.iloc[-1]
        else:
            #date = pd.Timestamp(dt.strptime(date, '%Y-%m-%d'))
            try:
                params = self.data.loc[date]
            except:
                params = self.data.iloc[self.data.index.get_loc(date,method='nearest')]

        return fed_svensson_rate(days, 
                beta_0= params[0],
                beta_1=params[1],
                beta_2=params[2],
                beta_3=params[3],
                tau_1=params[4],
                tau_2=params[5]
                )

    def svensson_curve(self, date = None, length = 7300):
        curve = [self.svensson_rate(days = i, date = date) for i in range(1, length)]
        return curve
