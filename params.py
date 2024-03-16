import numpy as np
# bagging regressor parameter grids

bagging_param_grid = {
    "max_samples": [0.1, 0.3, 0.6, 0.8, 1.0],
    "n_estimators": list(np.arange(50, 1000, 50, dtype=int))
}
