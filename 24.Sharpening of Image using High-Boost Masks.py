import cv2
resized_img = cv2.imread(r"C:\Users\ADMIN\Pictures\girl.png")
if resized_img is None:
    print("Error: Could not load the main image. Check the file path.")
    exit()
resized_wm = cv2.imread(r"C:\Users\ADMIN\Pictures\watermark.png")
if resized_wm is None:
    print("Error: Could not load the watermark image. Check the file path.")
    exit()
resized_wm = cv2.resize(resized_wm, (100, 100))  
h_img, w_img, _ = resized_img.shape
h_wm, w_wm, _ = resized_wm.shape

center_y = int(h_img / 2)
center_x = int(w_img / 2)

top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

if top_y < 0 or left_x < 0 or bottom_y > h_img or right_x > w_img:
    print("Error: Watermark size exceeds the boundaries of the main image.")
    exit()

roi = resized_img[top_y:bottom_y, left_x:right_x]

result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)

resized_img[top_y:bottom_y, left_x:right_x] = result

filename = r"C:\Users\ADMIN\Pictures\watermarked_girl.png"
cv2.imwrite(filename, resized_img)

cv2.imshow("Resized Input Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
