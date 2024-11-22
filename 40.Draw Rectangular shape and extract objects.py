import cv2

# Make sure the path is correct without invisible characters
img = cv2.imread(r"C:\Users\ADMIN\Pictures\spyy.jpg")

# Check if the image is loaded properly
if img is None:
    print("Error: Could not load the image. Check the file path.")
    exit()

# Define the ROI coordinates and size
x, y = 100, 100
width, height = 200, 150

# Extract the region of interest (ROI)
roi = img[y:y+height, x:x+width]

# Display the ROI
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
