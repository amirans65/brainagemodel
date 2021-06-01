"""
It is the same as 107 with LayerNormalization.
"""


import numpy as np
import tensorflow as tf
from tensorflow.keras import initializers
from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.regularizers import *
from .config import Config

def set_gpu():
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    mygpu = physical_devices[0]
    print(mygpu)
    tf.config.experimental.set_memory_growth(mygpu, True)
 
def sinc(inpLayer, N, M, l2_reg, act, inc_ind):
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
    x = sinc(x, 64, 5, config.l2_reg, 'elu', 0)
    x = LayerNormalization()(x)
    x = sinc(x,64,  5, config.l2_reg, 'elu', 1)
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
    model = net(Config(fs=64, CH=8, frame_sec=30))
    model.summary()
# %%
