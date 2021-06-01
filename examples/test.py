#%%
'''
This script is for testing a model on new data.
You can chose to use the pretrained model or use the model that trained by yourself.
'''

%reload_ext autoreload
%autoreload 2

import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
from brainagemodel.models.model_sinc import net
from brainagemodel.core.config import Config

from examplegenerators import TestGenerator
#from testgenerator import TestGenerator


#%% set configuration
use_pre_trained = False

config = Config()
config.fs=64
config.CH=8
config.frame_sec=30
config.epochs = 200
config.batch = 64


#%% generators
# !========== IMPORTANT ==========
'''
Before running this script TrainingGenerator and ValidationGenerator must be implimented
'''

tsgen = TestGenerator(config.batch, config.CH)

#%% load the trained model
if(use_pre_trained):
    from brainagemodel.pretrained.pretrainedsincmodel import PretrainedSincModel
    pre_model = PretrainedSincModel(config.CH)
    print(f'number of ensembles: {len(pre_model)}')
else:
    from brainagemodel.core.ensemblemodels import EnsembleModels
    saved_models = f'trained_models_ch{config.CH}'
    pre_model = EnsembleModels(config.CH, saved_models)
    print(f'number of ensembles: {len(pre_model)}')

# %% predict
predicted_pma = pre_model.predict(tsgen)
print(predicted_pma.shape)

# %%aggregate

# get recording indices or names
recording_indices = tsgen.get_fullepoch_recordings_indices()

# aggregate
final_pma = pre_model.aggregate(predicted_pma, recording_indices)
print(final_pma)

# %%
