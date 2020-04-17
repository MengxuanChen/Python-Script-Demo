Description: This script is design for running on raspberry pi and it also controls a camera peripheral that connects
to the raspberry pi. It uses OpenCV for the facial recognition.The script allows the user create a facial profile on real time. 
Then the script encodes the data and then it trains the recognizer. At the final stage it takes a live video input
and then recognize the user's face in the video. The script has 3 files. FacialDataCollector.py is responsible for collecting data and
FaceEncode.py is for training the recognizer. FaceRecognition.py is the main method for the whole script, 
it starts the video input and displays the recognization result.

run FaceRecognition.py to start the facial recogniction process.

Depedencies: Please install the following dependencies

1. OpenCV
2. Raspberry Pi camera module
