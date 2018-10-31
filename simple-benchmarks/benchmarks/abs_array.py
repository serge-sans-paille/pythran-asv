#pythran export abs_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * 2 * N - N
#run: abs_array(x)
import numpy as np
def abs_array(x):
    return np.abs(x)
