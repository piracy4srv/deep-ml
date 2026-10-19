import numpy as np

def linear_regression_gradient_descent(x,y,alpha,iteration):
    m,n=x.shape
    theta=np.zeros(n)

    for _ in range(iteration):
        predictions=x@theta
        errors=predictions-y
        gradient=(x.T @ errors)/m 
        theta-=alpha*gradient 
    return theta