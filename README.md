# Neural Networks for Gravitational Lens Modeling

This code uses convolutional neural networks (with TensorFlow) to estimate the parameters of strong gravitational lenses, namely the coordinates of the center of the lens in two dimensions, the einstein radius, and the complex ellipticities. These parameters enable us to quantify the distortions of images due to gravitational lensing.

## Gravitational Lensing Intro

According to Einstein's general theory of relativity, gravity is most accurately described as the bending of space-time around massive objects rather than a force acting at a distance (Einstein, 1915). 

Althought light moves in straight lines, if space-time is bent or distorted, then light, which has no mass, must follow these distortions. 
This phenomenon of light following these distortions in space-time is known as **gravitational lensing**. 

Gravitational lensing is observed when a light source and an observer have some object between them—such as galaxy, cluster of galaxies, or a black hole—that is massive enough to act as a lens . 

Very distant galaxies can be magnified through the phenomenon of gravitational lensing. 


![Einstein Ring](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Einstein ring captured by Hubble of LRG 3-757 (2007)")

![Einstein Cross](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Here are four images of the same quasar sitting behind Huchra’s Lens. The feature in the center is the core of the foreground galaxy. This arrangement is known as an Einstein cross.
")


## Update, August 2020
- The original version of this code was written in TensorFlow 1.1x and uses many functions that are now deprecated. 
- Additionally, the links to both the pretrained network weights and samples of lensing images in the orginal repo no longer work. 

As a result, I'll be making changes to update the code to (1) run in TensorFlow 2 , (2) run with the high level keras API, or (3) run with PyTorch 1.6+. 

## Demo:
The Jupyter notebook has a quick demonstration of lens modeling with neural networks.

TODO: 
- Simulate data for the demo to use.
- Train models from single_model_predictions.py and save them in a directory for in this repo. 
- Make them demo run in collab so that people without GPU access can still train from scratch. 

## Usage (undergoing large updates):
-  **Data**: You can produce simulated data using the following script: "[src/Lensing_TrainingImage_Generator.m](https://github.com/Unique-Divine/Neural-Networks-for-Gravitational-Lens-Modeling/tree/master/src)". This is a matlab script that contains all the required functions to generate simulated lenses. The only thing needed for this is a sample of unlensed images (e.g., from the GalaxyZoo, or GREAT3 datasets). 

- **Training**: 
  1.  Run "init.py" to setup the models. 
  2.  Run "single_model_predictions.py" to receive predictions from a single network. OR, run "combo_prediction.py" to combine the 4 models (see the paper referenced below). If you'd like to train your own model, use "train.py". You can train the existing models (there're about 11 models defined in "ensai_model.py").


------
## Acknowledgements \& References:
- This material is based upon work supported by the National Science Foundation under Grant PHY-1659598. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

- The legacy version of the code was forked from [Yashar Hezaveh](https://github.com/yasharhezaveh/Ensai) in May 2019. I've since gone a different direction with the project, changing certain aspects of the code for additional functionality, extenstibility, and readability, for maintenance purposes, and out of personal taste.  
  - Hezaveh, Y. D., Levasseur, L. P., & Marshall, P. J. (2017). Fast automated analysis of strong gravitational lenses with convolutional neural networks. *Nature*, 548(7669), 555-557.
  - Levasseur, L. P., Hezaveh, Y. D., & Wechsler, R. H. (2017). Uncertainties in parameters estimated with neural networks: Application to strong gravitational lensing. *The Astrophysical Journal Letters*, 850(1), L7.
