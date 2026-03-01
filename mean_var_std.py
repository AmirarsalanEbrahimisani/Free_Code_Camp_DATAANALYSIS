import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    matrix_3_3 = np.array(list).reshape(3, 3)

    dict_names = {
        "mean": np.mean,
        "variance": np.var,
        "standard deviation": np.std,
        "max": np.max,
        "min": np.min,
        "sum": np.sum,
    }

    result = {}

    for stat, func in dict_names.items():
        axis1 = func(matrix_3_3, axis=0).tolist()
        axis2 = func(matrix_3_3, axis=1).tolist()
        flattened = func(matrix_3_3).tolist()

        result[stat] = [axis1, axis2, flattened]

    return result
