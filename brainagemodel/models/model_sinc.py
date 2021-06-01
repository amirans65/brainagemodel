"""
The Sinc Keras model presented in the paper.
To get the model call 'net' function.
"""


import numpy as np
import tensorflow as tf
from tensorflow.keras import initializers
from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.regularizers import *
from brainagemodel.core.config import Config

def __sinc_block(inpLayer, N, M, l2_reg, act, inc_ind):
    ld=[]
    incname = 'inc{}_'.format(inc_ind)
    ldt = Conv1D(N, 1,name=incname+'conv11_p', padding='same', activation=act, kernel_regularizer=l2(l2_reg))(inpLayer)
    for i in range(int(M)):
        ldt = Conv1D(N, 3,name=incname+'conv_'+str(i), padding='same', activation=act, kernel_regularizer=l2(l2_reg))(ldt)
        ld.append(ldt)

    lm = MaxPooling1D(3, 1,name=incname+'max', padding='same')(inpLayer)
    lm = Conv1D(N, 1,name=incname+'maxconv11', padding='same', activation=act, kernel_regularizer=l2(l2_reg))(lm)

    l1 = Conv1D(N, 1,name=incname+'conv11', padding='same', activation=act, kernel_regularizer=l2(l2_reg))(inpLayer)
    
    return concatenate([l1, lm] + ld,name=incname+'concat', axis = 2)

def net(config):
    '''
    This function returns the Sinc network presented in the paper.
    
    Parameters:
    ===========
    config: an object from any class (preferably from brainagemodel.core.config.Config) which includes the following attributes:
        - fs: sampling frequecy in Hz (according to the paper, it should be 64Hz)
        - frame_sec: defining the frame length of EEG in seconds. According to the paper it should be 30s.
        - CH: the number of EEG channels. According to the paper it should be 1, 2, 4, or 8.

        Example:
            model = net(Config(fs=64, CH=8, frame_sec=30))
        The input signal to the network will be [frame_sec*fs), ch] (paper: [1920(30s*64Hz), 8/4/2/1])

    Return:
    ===========
    a Keras API-based model (not compiled).
    '''

    #input is [1920(30s*64Hz), ch]
    assert(hasattr(config,'fs') and
           hasattr(config,'frame_sec') and 
           hasattr(config,'CH'))
    input_shape_orig = config.frame_sec * config.fs
    input_shape = (input_shape_orig, config.CH)
    can_have_bnorm = (not hasattr(config,'remove_all_batch_neomalization_layers') or not config.remove_all_batch_neomalization_layers)
    act = 'elu'
    config.l2_reg = 0.001

    np.random.seed(0)
    initializers.he_normal(seed=1)

    # Input layers and normalisation
    input_orig = Input((input_shape_orig, config.CH), name='input_orig')
    x = input_orig

    # Add a Gaussian Noise Layer
    x = GaussianNoise(0.001)(x)

    x = Conv1D(128, 3, padding='same', activation='elu')(x)
    x = Conv1D(128, 3, padding='same', activation=None)(x)

    x = LayerNormalization()(x)
    x = Activation('elu')(x)

    x = MaxPooling1D(pool_size=5, padding='same')(x)

    x = Conv1D(256, 3, padding='same', activation='elu')(x)
    x = Conv1D(256, 3, padding='same', activation=None)(x)

    x = LayerNormalization()(x)
    x = Activation('elu')(x)

    x = MaxPooling1D(pool_size=4, padding='same')(x)

    #sinc(inpLayer, N, M, l2_reg, act, inc_ind)
    x = __sinc_block(x, 64, 5, config.l2_reg, 'elu', 0)
    x = LayerNormalization()(x)
    x = __sinc_block(x,64,  5, config.l2_reg, 'elu', 1)
    x = LayerNormalization()(x)

    x = AveragePooling1D(pool_size=4, padding='valid')(x)
    x = Flatten()(x)

    x = Dropout(0.20)(x)
    regress = Dense(1, activation='linear')(x)

    # Initialise model
    model_init = Model(inputs=[input_orig], outputs=regress)

    return model_init


#%%
if (__name__ == '__main__'):
    # for example:
    model = net(Config(fs=64, CH=8, frame_sec=30))
    model.summary()
# %%
