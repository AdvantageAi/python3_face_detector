# Face Detector

Nothing new here, just a simple Haar Cascade face detector using opencv 3 and python 3.

To make things simple I've included a conda `environment.yml`. 
To use navigate to the repos root, then the below commands:
```
conda env create -p=environment.yml
source activate python3_face_detector
rm -r imgs/*_boxed*
python Face_Detector.py harrcascades/haarcascade_frontalface_default.xml imgs/*
```

Example:

![alt text][example]

## Helpful resources 
The Harr Cascades are stored at `opencv/data/haarcascades/`
For example, if you're using anaconda3:
```
ls ~/anaconda3/pkgs/opencv-3.2.0-np112py36_blas_openblas_201/share/OpenCV/haarcascades/
```
For easy and to play with I have copy the files found in the above to `harrcascades/`.

### Other Stuff
* You can read more http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
* Another resource I just happened to find:
(alereimondo Harr Cascades)[http://alereimondo.no-ip.org/OpenCV/34]

[example]: example.jpg "Bounded Faces"
