import cv2
import numpy as np

# Open the video file
cap = cv2.VideoCapture("C:\\Users\\ADMIN\\Pictures\\test.mp4")

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video file")
else:
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)

            # Wait for 250 ms or until 'q' is pressed
            if cv2.waitKey(250) & 0xFF == ord('q'):
                break
        else:
            break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
