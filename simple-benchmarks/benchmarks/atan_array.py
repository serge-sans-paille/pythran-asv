#pythran export atan_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * 2 - 1
#run: atan_array(x)
import numpy as np
def atan_array(x):
    return np.arctan(x)
