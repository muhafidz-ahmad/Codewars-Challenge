import numpy as np

def greatest_product(st):
    result = []
    for i in range(len(st) - 4):
        result.append(np.prod([int(x) for x in st[i:i+5]]))
    return max(result)