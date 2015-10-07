import sys
import glob
import os
import numpy as np


def info_gain(S, Sl, Sr):
    """S is a the set of structure examples. Sl is the subset that
       goes to the left, Sr is the subset that goest to the right
       based on the split criteria at this node

       S - numpy array, columns are variables, rows are samples
    """
    #S is useless, S = Sl + Sr

    infgain = entropy(S) - ( np.shape(Sl)[0] / np.shape(S)[0] * entropy(Sl) + np.shape(Sr)[0] / np.shape(S)[0] * entropy(Sr))
    return infgain

def entropy(S):
    """ computes the entropy for S
    """
    H = 0.5 * np.log(np.linalg.det(covariant(S))) + 0.5 * np.shape(S)[1] * (1 + 1.83787706641) # ln(2pi) = 1.8378..
    return H

def covariant(S):
    return np.cov(S, rowvar=0)