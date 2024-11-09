import numpy as np
def normalization(trial):
    d = np.array(trial)
    min = d.min
    max = d.max
    d = (d-min)/(max-min)
    return d

