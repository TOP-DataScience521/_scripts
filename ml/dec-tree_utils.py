from math import log2


def entropy_shannon(*probs: float) -> float:
    return -sum(prob*log2(prob) for prob in probs)


