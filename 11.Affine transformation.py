import cv2
import numpy as np
img = cv2.imread(r"C:\Users\ADMIN\Pictures\64.jpg")
rows, cols, _ = img.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
scaled_dst = cv2.resize(dst, (cols // 2, rows // 2)) 
cv2.imshow("Affine Transform & Resized", scaled_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
