import pandas as pd
import plac
from utilities import read_yaml

@plac.annotations(T_type=("loc key from Conf.yaml"))
def get_data(T_type: str) -> None:
	data_config = read_yaml("Conf.yaml", T_type)
	print(data_config)
	data_src =data_config["url"]
	df =pd.read_csv(data_src)
	if T_type =='Train':
		df.to_csv("data/raw.csv",index =False)
	else:
		df.to_csv("data/test_data.csv",index =False)
if __name__=="__main__":
    plac.call(get_data)