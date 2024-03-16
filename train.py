import mlflow
import numpy as np
import pandas as pd
from data import x_train, y_train, x_val, y_val, x_test, y_test
from params import bagging_param_grid
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import ParameterGrid
from utils import eval_metrics

for params in ParameterGrid(bagging_param_grid):
    with mlflow.start_run():
        bagging = BaggingRegressor(**params)
        bagging.fit(x_train, y_train)
        y_pred_val = bagging.predict(x_val)
        metrics = eval_metrics(y_val, y_pred_val)

        mlflow.log_input(mlflow.data.from_numpy(
            features=x_train, targets=y_train), context="training data")

        mlflow.log_input(mlflow.data.from_numpy(
            features=x_val, targets=y_val), context="validation data")

        mlflow.log_params(params)

        mlflow.log_metrics(metrics)

        mlflow.sklearn.log_model(
            bagging,
            'BaggingRegressor',
            input_example=x_train,
            code_paths=['train.py', 'data.py', 'params.py', 'utils.py']
        )
