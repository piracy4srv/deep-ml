import numpy as np

def scalar_multiply(matrix,scalar):
	matrix_arr=np.array(matrix)
	return np.dot(matrix_arr,scalar).tolist()
