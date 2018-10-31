#pythran export acos_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * 2 - 1
#run: acos_array(x)
import numpy as np
def acos_array(x):
    return np.arccos(x)
