import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def eval_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true,y_pred)
    rmse = np.sqrt(mean_squared_error(y_true,y_pred))
    r2= r2_score(y_true, y_pred)

    metrics = {
        'mse':mse,
        'mae':mae,
        'rmse':rmse,
        'r2':r2
    }
    
    return metrics
