import numpy as np


def calculate(lst: list):

    if len(lst) == 9:

        one_dim = np.array(lst)
        matrix = one_dim.reshape((3, 3))

        mean = [
            list(np.mean(matrix, axis=0)),
            list(np.mean(matrix, axis=1)),
            one_dim.mean()
        ]
        variance = [
            list(np.var(matrix, axis=0)),
            list(np.var(matrix, axis=1)),
            one_dim.var()
        ]
        std = [
            list(np.std(matrix, axis=0)),
            list(np.std(matrix, axis=1)),
            one_dim.std()
        ]
        maximum = [
            list(np.max(matrix, axis=0)),
            list(np.max(matrix, axis=1)),
            np.max(one_dim)
        ]
        minimum = [
            list(np.min(matrix, axis=0)),
            list(np.min(matrix, axis=1)),
            np.min(one_dim)
        ]
        total = [
            list(np.sum(matrix, axis=0)),
            list(np.sum(matrix, axis=1)),
            one_dim.sum()
        ]

        calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': std,
            'max': maximum,
            'min': minimum,
            'sum': total
        }

        return calculations

    else:
        raise ValueError('List must contain nine numbers.')


array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(calculate(array))
