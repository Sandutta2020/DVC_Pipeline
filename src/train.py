from pathlib import Path

import pandas as pd
import plac
from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, StratifiedKFold
import numpy as np

from utilities import dump_yaml, read_yaml

def get_grid_search(estimator):
    grid_params = read_yaml("conf.yaml", "grid_search")
    model_params = read_yaml("conf.yaml", "model_parameters")

    grid_search = GridSearchCV(
        estimator,
        grid_params,
        cv=StratifiedKFold(
            n_splits=model_params["cv"],
            random_state=42,
            shuffle=True,
        ),
        scoring=model_params["scoring"],
        verbose=1,
        n_jobs=-1,
    )
    return grid_search

def train(x, y):
    estimator = RandomForestClassifier(random_state=42)
    grid_search = get_grid_search(estimator)
    grid_search.fit(x, y.ravel())
    return grid_search

def evaluate(model, test_data,test_data_y) -> dict:
    pred_y = model.predict(test_data.values)
    print(classification_report(test_data_y, pred_y))
    return classification_report(test_data_y, pred_y, output_dict=True)


def start_train():
    office_folder = Path(f"data/")
    train_data = pd.read_csv(office_folder / "X_train.csv")
    train_Y = pd.read_csv(office_folder / "Y_train.csv")
    feature_columns = train_data.columns
    grid_search = train(train_data, train_Y.values)
    model = grid_search.best_estimator_
    feature_importances = model.feature_importances_.tolist()
    best_params = dict(
        best_params=grid_search.best_params_,
        feature_importance={
            feature: importance
            for feature, importance in zip(feature_columns, feature_importances)
        },
    )

    model_folder = Path(f"model")
    dump(model, model_folder / "model.pkl")
    dump_yaml(best_params, model_folder / "best_paramer.yaml")

    report_folder = Path(f"metric/")
    dump_yaml(evaluate(model, train_data,train_Y), report_folder / "train.yaml")

    test_data_x = pd.read_csv(office_folder / "X_test.csv")
    test_data_y = pd.read_csv(office_folder / "Y_test.csv")
    model = load(model_folder / "model.pkl")
    dump_yaml(evaluate(model, test_data_x,test_data_y), report_folder / "test.yaml")

if __name__=="__main__":
    plac.call(start_train)