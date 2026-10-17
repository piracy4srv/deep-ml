import numpy as np

def calculate_covariance_matrix(vectors):
	vectors_arr=np.array(vectors)
	return np.cov(vectors_arr,ddof=1)
	