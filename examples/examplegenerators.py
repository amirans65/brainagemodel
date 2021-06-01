'''
producing random numbers as an example to test the codes
'''
import numpy as np
from tensorflow.keras.utils import Sequence

class BaseGenerator(Sequence):
    def __init__(self, batch_size, CH):
        self.batch_size = batch_size
        self.CH = CH
        self.__fullepoch_recordings_indices=[]
        print('THIS GENERATOR PRODUCES MEANINGLESS RANDOM NUMBERS!')

    def __len__(self):
        return 100

    def get_fullepoch_recordings_indices(self):
        return np.array(self.__fullepoch_recordings_indices).flatten()

    def __getitem__(self, idx):
        x = np.random.randn(self.batch_size, 30*64, self.CH) # generate random EEG segments
        y = np.random.randint(25,45, (self.batch_size, )) # generate random PMAs
        if(idx ==0):
            self.__fullepoch_recordings_indices = []
        self.__fullepoch_recordings_indices.append(np.random.randint(0,13, self.batch_size )) # generate random recordings
        return (x, y)

class TrainingGenerator(BaseGenerator):
    pass

class ValidationGenerator(BaseGenerator):
    pass

class TestGenerator(BaseGenerator):
    pass
