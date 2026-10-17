import numpy as np

def reshape_matrix(matrix,n_shape):
	matrix_arr=np.array(matrix)
	try:

		return matrix_arr.reshape(n_shape).tolist()
	except: 
		empty=[]
		return empty
	