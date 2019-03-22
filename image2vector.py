import numpy as np

def image2vector(img):
    
    vec = img.reshape(img.shape[0] * img.shape[1] * img.shape[2], 1)
    
    return (vec)