#pythran export cosh_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * N
#run: cosh_array(x)
import numpy as np
def cosh_array(x):
    return np.cosh(x)
