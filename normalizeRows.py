import numpy as np

def normalizeRows(x):
    
    x_norm = np.linalg.norm(x, ord=2, axis=1, keepdims=True)
    
    x = x / norm
    
    return (x)