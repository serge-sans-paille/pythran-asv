#pythran export tan_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * 2 * np.pi
#run: tan_array(x)
import numpy as np
def tan_array(x):
    return np.tan(x)
