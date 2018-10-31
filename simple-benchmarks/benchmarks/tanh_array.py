#pythran export tanh_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * N
#run: tanh_array(x)
import numpy as np
def tanh_array(x):
    return np.tanh(x)
