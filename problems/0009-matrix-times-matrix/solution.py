import numpy as np

def matrixmul(a,b):
    A=np.array(a)
    B=np.array(b)

    try:
        result= A @ B 
        return result
    except:
        return -1 