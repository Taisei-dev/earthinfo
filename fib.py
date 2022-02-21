# 2-3
import numpy as np
def fib(n):
  return np.linalg.matrix_power(np.array([[1,1],[1,0]],dtype=object), n)[1][0]
print(fib(1000))
