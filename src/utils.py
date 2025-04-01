import os
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models: dict, params: dict):
    try:
        report = {}

        for model_name, model in models.items():
            print(f"\n Tuning: {model_name}")
            param_grid = params.get(model_name, {})  # Safe default

            if param_grid:
                grid_search = GridSearchCV(
                    model, param_grid, cv=3, n_jobs=-1, verbose=0
                )
                grid_search.fit(X_train, y_train)
                best_params = grid_search.best_params_
                print(f"Best Params for {model_name}: {best_params}")
                model.set_params(**best_params)

            # Fit final model
            model.fit(X_train, y_train)

            # Predict
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # R² Scores
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            print(
                f"{model_name} - Train R²: {train_score:.4f} | Test R²: {test_score:.4f}"
            )

            report[model_name] = test_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
