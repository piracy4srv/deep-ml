import numpy as np

def inverse_2x2(m):
    M=np.array(m)
    if np.linalg.det(M)==0:
        return None
    else:
        return np.linalg.inv(M)