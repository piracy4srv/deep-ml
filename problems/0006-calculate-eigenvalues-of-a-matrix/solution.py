import numpy as np

def calculate_eigenvalues(matrix):
	matrix_arr=np.array(matrix)
	w,v=np.linalg.eig(matrix_arr)
	return [float(x) for x in w]