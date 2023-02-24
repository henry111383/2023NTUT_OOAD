import matplotlib.pyplot as plt
import numpy as np

def plotxy() :
    xx = np.arange(start=0, stop=10, step=0.1, dtype=float)
    yy =  np.power(xx, 4)

    plt.plot(xx, yy)
    plt.show()