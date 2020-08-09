# Neural Networks for Gravitational Lens Modeling
------- 
This code uses convolutional neural networks (with TensorFlow) to estimate the parameters of strong gravitational lenses.

## **How to use the code:**
The best place to start is the ipython notebook. It has a quick demonstration of lens modeling with neural networks. This is what you need.

## 1. Software needed:
* Python 3
* TensorFlow 1.1x. (coming soon to TensorFlow 2)
   * I used pip to install this, following the instructions at [tensforflow.org](https://www.tensorflow.org/install/).

## 2.  The data: 
The files (especially the trained network weights) are too large to be hosted here. They can be found at the following links.
* [trained network weights](https://stanford.box.com/s/7wtkx1fr77156uec8h8apqm9my0aevpi),
* [a sample of lensing images to demonstrate the tool](https://stanford.box.com/s/tb2lpk824kee22ah3gz5b50trbp30vyx),
* and few [cosmic ray and artifact maps](https://stanford.box.com/s/hn6l82pkmhm65xsls6g7tcjq63blj8v7)
   * Please download these, untar them (e.g., tar xvfz CosmicRays.tar.gz), and place them inside the "data/" folder. Inside your "data" folder you should have a folder called "CosmicRays", another called "SAURON_TEST", and a third called "trained_weights" (in addition to the two files that are already there). 

You can now run through the ipython notebook and model gravitational lenses with neural networks!

#### If you'd like to get your hands a bit more dirty:
1) The data provided here is just for fun. You can produce simulated data using the following script: "[src/Lensing_TrainingImage_Generator.m](https://github.com/Unique-Divine/Neural-Networks-for-Gravitational-Lens-Modeling/tree/master/src)". This is a MATLAB script that contains all the required functions to generate simulated lenses. The only thing needed for this script is a sample of unlensed images (e.g., from the GalaxyZoo, or GREAT3 datasets). 

2) You can use "init.py" to setup the models. Then with "single_model_predictions.py" you can get the predictions of a single network. Alternatively, after running "init.py". you can run "combo_prediction.py", to combine the 4 models (see the paper referenced above). If you'd like to train your own model, use "train.py". You can train the existing models (there're about 11 models defined in "ensai_model.py").

## 3.  TODO: 
- Change demo file to run on TensorFlow 2 so that you can run it in a kaggle kernel. (https://github.com/tensorflow/models/issues/7767) Recent TensorFlow updates have broken the demo.
- Recreate the entire implementation in PyTorch, even if for no other reason than just to practice.

------
### Source note:
This repo was originally forked from [Yashar Hezaveh](https://github.com/yasharhezaveh/Ensai) in May 2019. I began working on the code that Summer (2019) at UIUC in the lenstronomy group with Joaquin Vieira. I've since gone a different direction with the project.  
> The results of this work have been published in a Nature letter "Fast Automated Analysis of Strong Gravitational Lenses with Convolutional Neural Networks" (Hezaveh, Perreault Levasseur, Marshall, 2017) and another paper, "Uncertainties in Parameters Estimated with Neural Networks: Application to Strong Gravitational Lensing", submitted to the Astrophysical Journal Letters (Perreault Levasseur, Hezaveh, and Wechsler, 2017).
