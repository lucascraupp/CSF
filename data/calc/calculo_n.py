import numpy as np

def modelo(distancias, N, d0, pl_d0):
    return pl_d0 - (10 * N * np.log10(np.divide(distancias, d0)))

