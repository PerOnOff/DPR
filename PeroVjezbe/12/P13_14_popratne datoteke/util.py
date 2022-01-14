# util.py
from typing import List  #omogućava "type hint" zbog bolje preglednosti koda
from math import exp


# dot product of two vectors
def dot_product(xs: List[float], ys: List[float]) -> float:
    return sum(x * y for x, y in zip(xs, ys))


# the classic sigmoid activation function
# def sigmoid(x: float) -> float:
#     return 1.0 / (1.0 + exp(-x))

def sigmoid(x: float) -> float:
    return max(0.0, x)


def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)


# pretpostavimo da su svi retci jednake duljine
# i da je "feature scale" za svaku kolonu u rasponu 0 - 1
def normalize_by_feature_scaling(dataset: List[List[float]]) -> None:
    for col_num in range(len(dataset[0])):
        column: List[float] = [row[col_num] for row in dataset]
        maximum = max(column)
        minimum = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num] - minimum) / (maximum - minimum)

