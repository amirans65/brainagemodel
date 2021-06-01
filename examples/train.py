'''
This script is for training the proposed Sinc model. Before using it the marked lines corresponding the training and validation datagenerators should be altered.
'''

import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import ModelCheckpoint
from brainagemodel.models.model_sinc import net
from examplegenerators import TrainingGenerator,ValidationGenerator
#from traininggenerator import TrainingGenerator
#from validationgenerator import ValidationGenerator
from brainagemodel.core.config import Config


#%% set configuration
config = Config()
config.random_seed=0
config.fs=64
config.CH=8
config.frame_sec=30
config.epochs = 2
config.batch = 64


#%% generators
# !========== IMPORTANT ==========
'''
Before running this script TrainingGenerator and ValidationGenerator must be implimented
'''

trgen = TrainingGenerator(config.batch, config.CH)
vlgen = ValidationGenerator(config.batch, config.CH)
#%% save

model = net(config)
model.compile(optimizer='adam',
            loss='mean_squared_error', 
            metrics=['mae'])

early_stopping = EarlyStopping(monitor='val_loss', mode='auto', patience=10, restore_best_weights=True)
h = model.fit(trgen,
                    epochs=config.epochs,
                    validation_data = vlgen,
                    callbacks=[early_stopping,])
print(h.history)

#%% save the model
tf.keras.models.save_model(model, f'trained_models_ch{config.CH}/model{config.random_seed}.mdl')
print('saved.')
#%%