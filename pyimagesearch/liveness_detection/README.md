https://pyimagesearch.com/2019/03/11/liveness-detection-with-opencv/

There are four main directories inside our project:

dataset/ : Our dataset directory consists of two classes of images:
        Fake images of me from a camera aimed at my screen while playing a video of my face.
Real images of me captured from a selfie video with my phone.
face_detector/ : Consists of our pretrained Caffe face detector to locate face ROIs.
pyimagesearch/ : This module contains our LivenessNet class.
videos/ : I’ve provided two input videos for training our LivenessNet classifier.

Today we’ll be reviewing three Python scripts in detail. By the end of the post you’ll be able to run them on your own data and input video feeds as well. In order of appearance in this tutorial, the three scripts are:

gather_examples.py : This script grabs face ROIs from input video files and helps us to create a deep learning face liveness dataset.

train.py : As the filename indicates, this script will train our LivenessNet classifier. We’ll use Keras and TensorFlow to train the model. The training process results in a few files:

le.pickle : Our class label encoder.

liveness.model : Our serialized Keras model which detects face liveness.

plot.png : The training history plot shows accuracy and loss curves so we can assess our model (i.e. over/underfitting).

liveness_demo.py : Our demonstration script will fire up your webcam to grab frames to conduct face liveness detection in real-time.
