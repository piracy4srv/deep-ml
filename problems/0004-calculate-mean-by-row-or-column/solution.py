import numpy as np

def calculate_matrix_mean(matrix,mode):
	matrix_arr=np.array(matrix)

	if mode=='column':
		return [float(x) for x in np.mean(matrix_arr,axis=0)]
	elif mode=='row':
		return [float(x) for x in np.mean(matrix_arr, axis=1)]
	else:
		print("Error")
	