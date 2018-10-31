#pythran export asin_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * 2 - 1
#run: asin_array(x)
import numpy as np
def asin_array(x):
    return np.arcsin(x)
