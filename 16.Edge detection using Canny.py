import cv2

img = cv2.imread(r"C:\Users\ADMIN\Pictures\64.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

small_edges = cv2.resize(edges, (edges.shape[1] // 4, edges.shape[0] // 4))

cv2.imshow('Canny Edge Detection', small_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
