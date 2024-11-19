import cv2
path = "C:\\Users\\ADMIN\\Pictures\\spyy.jpg"
src = cv2.imread(path)
if src is None:
    print("Error: Could not read the image.")
else:
    image = cv2.rotate(src, cv2.ROTATE_180)
    window_name = 'Image'
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
