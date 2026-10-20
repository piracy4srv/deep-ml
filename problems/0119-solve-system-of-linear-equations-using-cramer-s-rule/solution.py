import numpy as np

def cramers_rule(A, b):
    A=np.array(A)
    r,c=A.shape
    b=np.array(b)
    if np.linalg.det(A)==0.:
        return -1
    else:
        x=np.zeros(c)
        for i in range(c):
            A_x=A.copy()
            A_x[:,i]=b
            d_x=np.linalg.det(A_x)
            x[i]=d_x/(np.linalg.det(A))
        return x
