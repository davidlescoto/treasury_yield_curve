import pandas as pd
from yield_curve import Yield_Curve
from datetime import date
data = Yield_Curve().data
#rate = Yield_Curve().svensson_rate()
curve  = Yield_Curve().svensson_curve(date = date(2022,6,24))