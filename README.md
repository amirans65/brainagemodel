![python](https://img.shields.io/static/v1?label=python&message=3.6%20%7C%203.7%20%7C%203.8&color=blue) ![PyPi](https://img.shields.io/static/v1?label=pypi%20package&message=2.5.0&color=blue)

## Requirements
![Tensorflow](https://img.shields.io/static/v1?label=tensorflow&message=2.1&color=green) ![numpy](https://img.shields.io/static/v1?label=numpy&message=1.18&color=green) ![scipy](https://img.shields.io/static/v1?label=scipy&message=1.4&color=green) ![tqdm](https://img.shields.io/static/v1?label=tqdm&message=4.43&color=green)

## Brain-age Estimation
This repository contains python scripts for automated neonatal brain-age estimation algorithm published in:
*"Ansari A.H., Pillay K., et al., "Brain-age as an estimator of neurodevelopmental outcome: A deep learning approach for neonatal cot-side monitoring", 2021."*

## How to use?
The important files in the repo are as follows:

├──  brainagemodel

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  core:   *(main classes and functions*)

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──   config: *(the Config class to set the configurations)*

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──   ensemblemodels: *(the EnsembleModels class to handle the ensemble networks, predictions, and aggregations)*

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  models

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──   sincnetwork: *(the proposed Sinc-based network for the age prediction problem)*

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──  pretrained: *( all requred saved files for loading the pretrained sinc models)*

│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──   pretrainedsincmodel *(the pretrained  ensemble Sinc-based network for the age prediction problem)*

└──  examples

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  traininggenerator  *(the training generator, some functions should be completed by the user)*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  validationgenerator  *(the validation generator, some functions should be completed by the user)*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  testgenerator  *(the test generator, some functions should be completed by the user)*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  examplegenerators  *(an example of random generators for testing the train and test scripts)*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  train  *(the training procedure given the training and validation generators are implemented)*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──   test  *(the test procedure given the test generator is implemented)*


To use this package, the following steps should be done:
1. make the training, validation, and test generators. To do so, you can implement the functions in the corresponding files or make some sub-classes and override the unimplemented functions. In these generators, the outputs should be normalized EEG segments (for more details see the documentation in the generators). To normalize the EEG, according to the paper, we standardized with a mean and a standard deviation (equally for all channels). To use the same values, which were calculated on our training dataset, you can use 'pre_normalize' function located in brainagemodel/pretrained/prenorm.
  * Note 1: if you use prenorm, be sure that the input is in Volts (not uV)
  * Note 2: in the paper we suggested some mechanisms for compensating the imbalacedness of data including bootstraping, sample_weight, and PMA noise. If you want to reproduce the results the same mechanisms should be implemented in this training generator.
  * Note 3: in case of using the pretrained models, the order of the EEG channels must be the same as what listed in the paper: ['Fp1','Fp2','C3','C4','T3','T4','O1','O2'], ['C3','C4','T3','T4'], ['C3','C4'], or ['C3' - 'C4']. (for more details, see the paper).
3.  [*if you want to use the pretrained models, skip this step*] run the 'train' script multiple times with different random_seeds and your favorable number of channels. As running TensorFlow on GPU is not reproducable regardless of the random_seed, this random_seed is not set anywhere, but it is an index showing different initializations. At the end of each run, the best trained model is saved in a folder named with the chennel suffix. Thus, after multiple runs for one channel configuration, you have a folder with multiple saved models. In the paper, we performed it 10 times.
4.  run the test script. Here you can select using the pretrained models or your trained models using the PretrainedSincModel class or EnsembleModels. These models are not Keras-based models, as they both support ensemble models. But they have a predict function which produces the age of each input EEG segment from each of the enseble model. They also have 'aggregation' function to aggregate the recordings and ensemble models. To use it you need to provide a vetror indicating the index or name of each EEG segment that fed to the network (see the test script for more details). The results are in a dictionary with recording index/name as key and age (PMA) in weeks as value.

## Citation
Please cite the following papers: 
1. Ansari A.H., Pillay K., et al., et al., "Brain-age as an estimator of neurodevelopmental outcome: A deep learning approach for neonatal cot-side monitoring", 2021. 
2. Ansari A.H., Pillay K., et al., et al., "A Deep Shared Multi-Scale Inception Network Enables Accurate Neonatal Quiet Sleep Detection with Limited EEG Channels" 2021.

## License
![License](https://img.shields.io/static/v1?label=License&message=MIT&color=green)

