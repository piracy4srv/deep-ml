import math
import numpy as np
def softmax(score):
    score=np.asarray(score,dtype=float)

    shifted_score=score-np.max(score,axis=-1,keepdims=True)

    return np.exp(shifted_score) / np.sum(np.exp(shifted_score),axis=-1,keepdims=True)





