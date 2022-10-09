import pandas as pd
import plac
from  sklearn.model_selection import train_test_split
@plac.annotations(T_type=("loc key from Conf.yaml"))
def process_data(T_type):
	if T_type =='Train':
		df= pd.read_csv("data/raw.csv")
		df.Age.fillna(df.Age.mean(),inplace =True)
		df.Sex =df.Sex.apply(lambda x: 1 if x=='male' else 0)
		columns =['Pclass','Sex','Age','Survived']
		df_new=df[columns].copy()
		df_new['Age']=df_new['Age'].astype('int')
		df_new.to_csv('data/processed.csv',index =False)
	else:
		df= pd.read_csv("data/test_data.csv")
		df.Age.fillna(df.Age.mean(),inplace =True)
		df.Sex =df.Sex.apply(lambda x: 1 if x=='male' else 0)
		columns =['Pclass','Sex','Age']
		df_new=df[columns].copy()
		df_new.to_csv('data/processed_test.csv',index =False)
if __name__=="__main__":
    plac.call(process_data)