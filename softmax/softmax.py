import numpy as np
import math

# This function takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    L_prob = []
    L_sum = 0
    for i in range(len(L)):
        L_sum += math.exp(L[i])
    for i in range(len(L)):
        L_prob.append(math.exp(L[i])/L_sum)
    return L_prob
