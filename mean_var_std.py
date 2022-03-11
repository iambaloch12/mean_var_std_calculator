import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        array_list = np.array(list).reshape(3, 3)

    mean_value = [(array_list.mean(axis=0).tolist()), (array_list.mean(axis=1).tolist()),
            (array_list.flatten().mean())]

    var_value = [(array_list.var(axis=0).tolist()), (array_list.var(axis=1).tolist()),
           (array_list.flatten().var())]

    std_value = [(array_list.std(axis=0).tolist()), (array_list.std(axis=1).tolist()),
           (array_list.flatten().std())]

    max_value = [(array_list.max(axis=0).tolist()), (array_list.max(axis=1).tolist()),
           (array_list.flatten().max())]

    min_value = [(array_list.min(axis=0).tolist()), (array_list.min(axis=1).tolist()),
           (array_list.flatten().min())]

    sum_value = [(array_list.sum(axis=0).tolist()), (array_list.sum(axis=1).tolist()),
           (array_list.flatten().sum())]

    calculations = {
        "mean": mean_value,
        "variance": var_value,
        "standard deviation": std_value,
        "max": max_value,
        "min": min_value,
        "sum": sum_value,
    }
    return calculations