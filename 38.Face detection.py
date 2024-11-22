import cv2

# Ensure the correct path to the cascade file
face_cascade = cv2.CascadeClassifier(r"file:///C:/Users/ADMIN/Downloads/Face-Detection-OpenCV-master/Face-Detection-OpenCV-master/data/lbpcascade_frontalface.xml")

# Check if the cascade file is loaded properly
if face_cascade.empty():
    print("Error: Cascade file not loaded. Check the path to the xml file.")
    exit()

# Load image
image = cv2.imread(r"‪C:\Users\ADMIN\Pictures\man.jfif")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
