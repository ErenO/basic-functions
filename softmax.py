import numpy as np

def softmax(x):
    
    x_exp = np.exp(x)
    
    x_sum = np.sum(x_exp, axis = 1, keepdims = True)
    
    s = x_exp / x_sum
    
    return (s)