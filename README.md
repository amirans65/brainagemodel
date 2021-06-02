![python](https://img.shields.io/static/v1?label=python&message=3.6%20%7C%203.7%20%7C%203.8&color=blue) ![PyPi](https://img.shields.io/static/v1?label=pypi%20package&message=2.5.0&color=blue)

## Requirements
![Tensorflow](https://img.shields.io/static/v1?label=tensorflow&message=2.1&color=green) ![numpy](https://img.shields.io/static/v1?label=numpy&message=1.18&color=green) ![scipy](https://img.shields.io/static/v1?label=scipy&message=1.4&color=green) ![tqdm](https://img.shields.io/static/v1?label=tqdm&message=4.43&color=green)

## Brain-age Estimation
This repository contains python scripts for automated neonatal brain-age estimation algorithm published in:
*"Ansari A.H., Pillay K., et al., "Brain-age as an estimator of neurodevelopmental outcome: A deep learning approach for neonatal cot-side monitoring", 2021."*

## How to use?
The important files in the repo are as follows:
- repo
├──  brainagemodel
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  core:   *(main classes and functions*)
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──   config: *(the Config class to set the configurations)*
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──   ensemblemodels: *(the EnsembleModels class to handle the ensemble networks, predictions, and aggregations)*
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  models
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──   sincnetwork: *(the proposed Sinc-based network for the age prediction problem)*
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──  pretrained: *( all requred saved files for loading the pretrained sinc models)*
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──   pretrainedsincmodel *(the pretrained  ensemble Sinc-based network for the age prediction problem)*
└──  examples
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  traingenerator  *(the training generator where some functions should be implemented or be overridden in a derived class)*
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  validationgenerator  *(the  generator where some functions should be implemented or be overridden in a derived class)*
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  testgenerator  *(the test generator where some functions should be implemented or be overridden in a derived class)*
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  examplegenerators  *(an example of random generators for testing the train and test scripts)*
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──  train  *(the training procedure given the training and validation generators are implemented)*
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──   test  *(the test procedure given the test generator is implemented)*


## Citation
Please cite the following papers: 
1. Ansari A.H., Pillay K., et al., "Brain-age as an estimator of neurodevelopmental outcome: A deep learning approach for neonatal cot-side monitoring", 2021. 
2. Ansari A.H., et al. "A Deep Shared Multi-Scale Inception Network Enables Accurate Neonatal Quiet Sleep Detection with Limited EEG Channels" 2021.

## License
![License](https://img.shields.io/static/v1?label=License&message=MIT&color=green)

