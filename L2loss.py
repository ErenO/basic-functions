import numpy as np

def L2(yhat, y):
    
    loss = np.sum((y - yhat) ** 2)
    
    return (loss)