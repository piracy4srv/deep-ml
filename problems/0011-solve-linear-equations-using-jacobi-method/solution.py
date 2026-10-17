import numpy as np

def solve_jacobi(A,b,n):

    A=np.array(A, dtype=float)
    b=np.array(b,dtype=float)
    m=len(b)
    x=np.zeros(m)
    for _ in range(n):
        x_new=np.zeros(m)

        for i in range(m):

            sigma=sum(A[i][j]* x[j] for j in range(m) if j!=i)

            x_new[i]=(b[i]-sigma)*(1/A[i][i])
        x=x_new

    return [round(float(k),4) for k in x ]