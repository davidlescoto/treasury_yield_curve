import pandas as pd
import nasdaqdatalink

nasdaqdatalink.read_key(filename="/data/.corporatenasdaqdatalinkapikey")
data = nasdaqdatalink.get("FED/PARAMS")
data.to_csv("data/data_params.csv")
