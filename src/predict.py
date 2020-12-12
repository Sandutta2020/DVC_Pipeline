from joblib import dump, load
import pandas as pd
import plac
from pathlib import Path

def predict():
    model_folder = Path(f"model")
    model = load(model_folder / "model.pkl")
    test_data=pd.read_csv("data/processed_test.csv")
    pred_y = model.predict(test_data.values)
    test_data["Prediction"] =pred_y
    test_data.to_csv("data/results.csv")
if __name__=="__main__":
    plac.call(predict)