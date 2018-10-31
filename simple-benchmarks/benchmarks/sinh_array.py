#pythran export sinh_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * N
#run: sinh_array(x)
import numpy as np
def sinh_array(x):
    return np.sinh(x)
