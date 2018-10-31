#pythran export square_array(float64 [])
#setup: import numpy as np ; np.random.seed(0); N = 10000 ; x = np.random.random(N)
#run: square_array(x)
import numpy as np
def square_array(x):
    return x ** 2
