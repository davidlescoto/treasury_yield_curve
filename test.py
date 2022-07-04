import pandas as pd
from yield_curve import Yield_Curve

#data = Yield_Curve().data
rate = Yield_Curve().svensson_rate()
curve  = Yield_Curve().svensson_curve(date = '2022-06-30')