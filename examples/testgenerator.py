'''
This datageneratormust be defined before testing the network. Custom Keras datagenerators are elaborately described and illustrated here, https://towardsdatascience.com/implementing-custom-data-generators-in-keras-de56f013581c
The generators must return (EEG, PMA)  or (EEG, PMA, sample_weights) where:
    - EEG is a numpy tensor as [batchsize, (fs * frame_sec), CH]. (batchsize is an arbitrary number). Accrding to the paper it should be [64, 1920, 8].
        * the EEG should be normalized in the genrator (or before) so that the mean and std is respectively 0 and 1.
    - PMA is a numpy vector as [batchsize,] defining the PMAs corresponding the EEG samples
    - sample_weights is an optional weights (with the same size as PMA) to define training weights of the EEG samples. (According to the paper it should compensate the PMA distribution imbalancedness of the training data.)
'''

from tensorflow.keras.utils import Sequence

class TestGenerator(Sequence):

    def __init__(self, batch_size, CH):
        self.batch_size = batch_size
        self.CH = CH

    def on_epoch_end(self):
        #TODO: must be implimented, if shuffling is needed
        raise TypeError('TestGenerator is not yet fully implimented!') 

    def __len__(self):
        #TODO: must be implimented, length of one epoch
        raise TypeError('TestGenerator is not yet fully implimented!') 

    def __getitem__(self, idx):
        #TODO: must be implimented, return one batch of data
        '''
        It must return (EEG, PMA)  or (EEG, PMA, sample_weights) where:
            - EEG is a numpy tensor as [batchsize, (fs * frame_sec), CH]. (batchsize is an arbitrary number). Accrding to the paper it should be [64, 1920, 8].
                * the EEG should be normalized here (or before) so that the mean and std is respectively 0 and 1.
            - PMA is a numpy vector as [batchsize,] defining the PMAs corresponding the EEG samples
            - sample_weights are optional weights (with the same size as PMA) to define training weights of the EEG samples. (According to the paper it should compensate the PMA distribution imbalancedness of the training data.)
        '''
        raise TypeError('TestGenerator is not yet fully implimented!') 

