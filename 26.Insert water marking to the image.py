import cv2
import numpy as np

main_image = cv2.imread(r"C:\Users\ADMIN\Pictures\girl.png")
if main_image is None:
    exit()

watermark = cv2.imread(r"C:\Users\ADMIN\Pictures\water mark.png", cv2.IMREAD_UNCHANGED)
if watermark is None or watermark.shape[2] != 4:
    exit()

h_img, w_img, _ = main_image.shape
h_wm, w_wm, _ = watermark.shape

if h_wm > h_img or w_wm > w_img:
    scale_factor = 0.2
    watermark = cv2.resize(watermark, (int(w_img * scale_factor), int(h_img * scale_factor)))

h_wm, w_wm, _ = watermark.shape
watermark_bgr = watermark[:, :, :3]
alpha_channel = watermark[:, :, 3]
x_offset = w_img - w_wm - 10
y_offset = h_img - h_wm - 10
roi = main_image[y_offset:y_offset + h_wm, x_offset:x_offset + w_wm]
alpha_mask = alpha_channel / 255.0

for c in range(3):
    roi[:, :, c] = (1.0 - alpha_mask) * roi[:, :, c] + alpha_mask * watermark_bgr[:, :, c]

main_image[y_offset:y_offset + h_wm, x_offset:x_offset + w_wm] = roi
output_path = r"C:\Users\ADMIN\Pictures\watermarked_girl.png"
cv2.imwrite(output_path, main_image)
scale_factor_display = 0.5
resized_output = cv2.resize(main_image, (int(w_img * scale_factor_display), int(h_img * scale_factor_display)))
cv2.imshow("Watermarked Image (Resized for Display)", resized_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
