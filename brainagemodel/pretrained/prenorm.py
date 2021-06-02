import pickle
import os
import numpy as np
def pre_normalize(eeg_in_volts):
    root = os.path.dirname(__file__)
    fname = f'{root}/norm.pkl'
    with open(fname, 'rb') as f:
        r = pickle.load(f)
    return (eeg_in_volts - r['sub']) / r['den']
