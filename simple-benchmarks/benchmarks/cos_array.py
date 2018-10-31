#pythran export cos_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N) * 2 * np.pi
#run: cos_array(x)
import numpy as np
def cos_array(x):
    return np.cos(x)
