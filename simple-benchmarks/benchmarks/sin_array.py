#pythran export sin_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * 2 * np.pi
#run: sin_array(x)
import numpy as np
def sin_array(x):
    return np.sin(x)
