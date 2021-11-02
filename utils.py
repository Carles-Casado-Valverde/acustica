import numpy as np

def singen(A, t, step, f0, phi0):
    t = np.arange(0,t, step)
    return A*np.sin(2*np.pi*f0*t + phi0)