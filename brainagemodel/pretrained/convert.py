#%%
import os
import tensorflow as tf
from shutil import copyfile

for ch in (1,2,4,8):
    root0 = f'C:/MyFiles/MyCodes/research/DLAG_Clear/brainagemodel/pretrained'
    root = f'{root0}/channel{ch}'
    models = []
    for sn in range(100):
        fname = f'{root}/model117_sn{sn}_fs64_fr30_ch{ch}/model.h5'
        print(fname)
        if(not os.path.exists(fname)):
            break
        dst = f'{root0}/models/sincmodel_ch{ch}_sn{sn}'
        copyfile(fname, dst)


    


#%%
