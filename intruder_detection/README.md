# Intruder Detection

Intruder detection is a computer vision-based solution to detect the presence of unauthorized individuals in a specified area. This repository contains a Python implementation of an intruder detection algorithm that can be applied to videos.

## Requirements
OpenCV
Numpy

## Usage
To use the intruder detection algorithm, you need to provide the path to the input video file, the path to the output video file, and optional parameters such as the erosion kernel, the number of frames to skip before starting the detection, and the number of top contours to display in the output video.

## How it works
The algorithm first captures the input video using OpenCV's cv2.VideoCapture function. It then applies a background subtraction method to identify moving objects in the video. The resulting binary mask is eroded using the specified erosion kernel to reduce noise. The contours of the objects in the mask are then extracted and sorted by area. The bounding box around the top n contours is drawn on the original video frame, where n is specified by the top_contours parameter. The processed frame is then written to the output video file.

## Limitations
The intruder detection algorithm is not perfect and may produce false positives or negatives. The accuracy can be improved by fine-tuning the parameters, such as the background subtraction method, the erosion kernel, and the number of top contours to display.

## Conclusion
Intruder detection is a powerful tool for enhancing security and protecting property. The algorithm implemented in this repository is a simple but effective solution for detecting intruders in videos. However, it is not a complete security system and should be used in conjunction with other security measures.