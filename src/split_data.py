import pandas as pd
import plac
from  sklearn.model_selection import train_test_split

def split_data():
	df= pd.read_csv("data/processed.csv")
	x =df.drop(columns=['Survived'])
	y=df['Survived']
	X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.10, random_state=42)
	X_train.to_csv("data/X_train.csv",index =False)
	Y_train.to_csv("data/Y_train.csv",index =False)
	X_test.to_csv("data/X_test.csv",index =False)
	Y_test.to_csv("data/Y_test.csv",index =False)
if __name__=="__main__":
    plac.call(split_data)