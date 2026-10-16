import numpy as np

def matrix_dot_vector(matrix,vector):
	matrix_arr=np.array(matrix)
	vector_arr=np.array(vector)

	try:
		result= matrix_arr @ vector_arr
		return result.tolist()
	except ValueError as e:
		return -1
	
	
