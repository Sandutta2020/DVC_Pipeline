import pandas as pd
from sklearn.metrics import accuracy_score
import json
df =pd.read_csv("data/results.csv")
y_true=df['Survived']
y_pred=df['Prediction']
# Calculating accuracy for metric 
auc = accuracy_score(y_true, y_pred)
with open("scores.json", 'w+') as f:
    json.dump({'auc': auc}, f)
# dumping for plot generation
df[['Survived','Prediction']].to_csv('plots.csv')