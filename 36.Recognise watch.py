import cv2
import numpy as np

# Load the input image and template image (watch image)
image = cv2.imread(r"C:/path/to/your_image.jpg")
template = cv2.imread(r"C:/Users/ADMIN/Pictures/watch (2).jfif")  # Ensure there are no non-printable characters in this path

# Check if the images were loaded correctly
if image is None or template is None:
    print("Error: Could not load the images.")
    exit()

# Resize the template if it is larger than the input image
h_img, w_img, _ = image.shape
h_template, w_template, _ = template.shape

if h_template > h_img or w_template > w_img:
    print("Template is larger than the image, resizing template.")
    # Resize the template to fit inside the image
    template = cv2.resize(template, (w_img, h_img))

# Convert the input image to grayscale for matching
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert the template image to grayscale
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)

# Get the location of the best match
threshold = 0.8  # Adjust the threshold for accuracy
locations = np.where(result >= threshold)

# Draw rectangles around the detected regions
for loc in zip(*locations[::-1]):  # Flipping to get coordinates in (x, y) format
    x, y = loc
    cv2.rectangle(image, (x, y), (x + template.shape[1], y + template.shape[0]), (0, 255, 0), 2)

# Display the result
cv2.imshow("Detected Watch", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the output image
cv2.imwrite(r"C:/path/to/output_image.jpg", image)

