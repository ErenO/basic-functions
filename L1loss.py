import numpy as np

def L1(yhat, y):
    
    loss = np.sum(np.absolute(y - yhat))
    
    return (loss)