from joblib import dump, load
import pandas as pd
import plac
from pathlib import Path

def predict():
    model_folder = Path(f"model")
    model = load(model_folder / "model.pkl")
    test_data=pd.read_csv("data/X_test.csv")
    actual_survived=pd.read_csv("data/Y_test.csv")
    pred_y = model.predict(test_data.values)
    test_result=test_data.join(actual_survived)
    test_result["Prediction"] =pred_y
    test_result.to_csv("data/results.csv",index=False)
if __name__=="__main__":
    plac.call(predict)