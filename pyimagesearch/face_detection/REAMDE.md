https://pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/

https://github.com/opencv/opencv/tree/master/samples/dnn/face_detector


When using OpenCV’s deep neural network module with Caffe models, you’ll need two sets of files:

    The .prototxt file(s) which define the model architecture (i.e., the layers themselves)
    The .caffemodel file which contains the weights for the actual layers


python detect_faces.py --image rooster.jpg --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel

python detect_faces.py --image rooster.jpg --prototxt deploy_lowres.prototxt.txt --model res10_300x300_ssd_iter_140000_fp16.caffemodel

python detect_faces_video.py --prototxt deploy.prototxt --model res10_300x300_ssd_iter_140000.caffemodel
