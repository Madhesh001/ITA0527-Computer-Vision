import cv2
import numpy as np
image = cv2.imread(r"C:\Users\ADMIN\Pictures\girl.png", cv2.IMREAD_COLOR)
if image is None:
    print("Error: Could not load the image. Check the file path.")
    exit()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3) 
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3) 
gradient_magnitude = cv2.magnitude(sobel_x, sobel_y)
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)  

alpha = 1   
beta = 0.5                                                                                                        
sharpened_image = cv2.addWeighted(gray_image, alpha, gradient_magnitude, beta, 0)
cv2.imshow("Original Image", gray_image)
cv2.imshow("Gradient Magnitude (Mask)", gradient_magnitude)
cv2.imshow("Sharpened Image", sharpened_image)

# Wait and cleanup
cv2.waitKey(0)
cv2.destroyAllWindows()
