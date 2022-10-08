import pandas as pd
from sklearn.metrics import accuracy_score
import json
df =pd.read_csv("data/results.csv")
y_true=df['Survived']
y_pred=df['Prediction']
auc = accuracy_score(y_true, y_pred)


with open("scores.json", 'w+') as f:
    json.dump({'auc': auc}, f)