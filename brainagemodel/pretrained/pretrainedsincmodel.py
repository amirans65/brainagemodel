import os
import numpy as np
from re import VERBOSE
import tensorflow as tf
from tqdm import tqdm
from tensorflow.keras.utils import Sequence
from brainagemodel.core.ensemblemodels import EnsembleModels
class PretrainedSincModel(EnsembleModels):
    '''
    To load all ensembled trained Sinc models. 
    Note that it is not a keras model, but it has a predict funtion with similar inputs/outputs.
    It also has a predict_recording which also applies the recording-level aggregation and then model ensembling aggregation according to the paper.
    
    Parameters:
    ===========
    CH: the number of eeg channels {1, 2, 4, or 8}
    verbose: if True, it shows the loading progress; otherwise, it is silent.
    '''
    def __init__(self, CH, verbose=True):
        super().__init__(CH, None)
        self.__find_models()

    def __find_models(self):
        root = os.path.dirname(__file__)
        self.models_paths = {}
        rn = range(100) 
        if self.verbose: 
            rn = tqdm(rn)
        for sn in rn:
            fname = f'{root}/models/sincmodel_ch{self.CH}_sn{sn}'
            if(not os.path.exists(fname)):
                continue
            self.models_paths[sn] = fname


