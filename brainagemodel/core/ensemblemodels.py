import os
import numpy as np
from re import VERBOSE
import tensorflow as tf
from tqdm import tqdm
from tensorflow.keras.utils import Sequence
class EnsembleModels():
    '''
    To load all ensembled Sinc models. 
    Note that it is not a keras model, but it has a predict funtion with similar inputs/outputs.
    
    Parameters:
    ===========
    CH: the number of eeg channels {1, 2, 4, or 8}
    trained_model_directory: the directory in which the ensemble models are located. The name of the models must be 'model[x].h5' (e.g. model1.h5, model2.h5, ...). It maximally supports 1000 models.
    verbose: if True, it shows the loading progress; otherwise, it is silent.
    '''
    def __init__(self, CH, trained_model_directory, verbose=True):
        assert(CH in (1,2,4,8))
        self.CH = CH
        self.verbose = verbose
        self.__find_models(trained_model_directory)
        if(self.verbose):
            print(' ')

    def __len__(self):
        '''Return the length of the loaded ensmbled models.'''
        return len(self.models_paths)

    def __find_models(self, trained_model_directory):
        self.models_paths = {}
        if(trained_model_directory is None):
            return
        rn = range(1000) 
        if self.verbose: 
            rn = tqdm(rn)
        for sn in rn:
            fname = f'{trained_model_directory}/model{sn}.h5'
            if(not os.path.exists(fname)):
                continue
            self.models_paths[sn] = fname

    def __get_models(self, index):
        fname = self.models_paths[index]
        if(not os.path.exists(fname)):
            raise ValueError('This index is not correct!')
        model = tf.keras.models.load_model(fname)
        return model

    def predict(self, eeg):
        '''
        To predict the outputs of all loaded ensembled models. 
        
        parameters:
        ===========
        eeg:    a numpy tensor as [batch, 1920, CH]
                OR
                a datagenerator returning [batch, 1920, CH]

        Return:
        =======
        PMA numpy matrix as [batch, number of models]
        '''
        res = []
        for i in range(len(self)):
            print(f'model {i} out of {len(self)}...')
            model = self.__get_models(i)
            r = model.predict(eeg, verbose = self.verbose)
            res.append(r)
        res = np.stack(np.squeeze(res), -1)
        print('prediction values are ready.')
        return res

    def aggregate(self, pmas, recordings_indices):
        '''
        This function takes pmas tensor of all recordings and all models as well as the recording indices/names and returns the aggregated PMA per recording in a dictionary.
        This can be called after the 'predict' function. 
        The 'predict_recording' function internally calls this function and returns its output.
        '''
        res = {}
        recs = np.unique(recordings_indices)
        for rec in recs:
            ii = (recordings_indices == rec)
            x = pmas[ii,:]
            m = np.median(x,0) # median across epochs
            mm = np.median(m, 0) #median across models
            res[rec] = mm
        return res


