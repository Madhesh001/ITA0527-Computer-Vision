import cv2
import numpy as np
image = cv2.imread(r"C:\Users\ADMIN\Pictures\dogg.jfif")
img2 = cv2.imread(r"C:\Users\ADMIN\Pictures\logo.png")
if image is None or img2 is None:
    print("Error: One or both of the images could not be loaded.")
    exit()
print(image.shape)
cv2.imshow("Original", image)
imageCopy = image.copy()
cv2.circle(imageCopy, (100, 100), 30, (255, 0, 0), -1)
cv2.imshow('Image', image)
cv2.imshow('Image Copy', imageCopy)
cropped_image = image[80:280, 150:330]
cv2.imshow("Cropped", cropped_image)
cv2.imwrite("Cropped Image.jpg", cropped_image)
img2_resized = cv2.resize(img2, (image.shape[1], image.shape[0]))
dst = cv2.addWeighted(image, 0.5, img2_resized, 0.7, 0)
img_arr = np.hstack((image, img2_resized))
cv2.imshow('Input Images', img_arr)
cv2.imshow('Blended Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
