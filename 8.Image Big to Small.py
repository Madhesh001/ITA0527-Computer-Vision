import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)
img = cv2.imread("C:\\Users\\ADMIN\\Pictures\\spyy.jpg", cv2.IMREAD_COLOR)
if img is None:
    print("Error: Could not read the image.")
else:
    img = cv2.resize(img, (300, 300))
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
