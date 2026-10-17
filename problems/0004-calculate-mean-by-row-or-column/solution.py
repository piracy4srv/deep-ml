import numpy as np

def calculate_matrix_mean(matrix,mode):
	matrix_arr=np.array(matrix)
	result=[]
	result2=[]
	if mode=='column':
		for col in range(matrix_arr.shape[1]):
			result.append(np.mean(matrix_arr[:,col]))
		return result
	elif mode=='row':
		for row in range(matrix_arr.shape[0]):
			result2.append(np.mean(matrix_arr[row,:]))
		return result2
			