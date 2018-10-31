#pythran export sqrt_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * N
#run: sqrt_array(x)
import numpy as np
def sqrt_array(x):
    return np.sqrt(x)
