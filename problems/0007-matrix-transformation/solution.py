import numpy as np

def transform_matrix(A,T,S):
	T_arr=np.array(T)
	S_arr=np.array(S)
	A_arr=np.array(A)

	if np.linalg.det(T_arr)==0:
		return -1
	elif np.linalg.det(S_arr)==0:
		return -1
	else:
		try:
			result=(np.linalg.inv(T_arr))@(A_arr)@(S_arr)
			return result
		except:
			return -1