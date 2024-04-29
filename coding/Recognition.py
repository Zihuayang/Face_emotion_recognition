import cv2
import numpy as np

# Load the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# Load the Haar cascade for face detection
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

# Emotions related to ids: example ==> Anger: id=0, etc
names = ['Angry', 'Happy', 'Sad', 'None']

# Initialize and start real-time video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)


#ret, img =cam.read()   #camera picture

# Read an image
img = cv2.imread("sad.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(int(minW), int(minH)),
)

for (x, y, w, h) in faces:
    # Draw a rectangle around the detected face
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Predict the emotion of the detected face
    id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

    # Display the emotion label and confidence percentage
    text = ""
    for i, name in enumerate(names):
        if i == id:
            text += f"{name}: {round(100 - confidence)}%, "
        else:
            text += f"{name}: 0%, "  # Assume 0% confidence for other emotions
    cv2.putText(img, text[:-2], (x + 5, y - 5), font, 0.5, (255, 255, 255), 2)

# Save the image with emotion labels
cv2.imwrite("picture3.jpg", img)

print("\n [INFO] Done detecting and Image is saved")
cam.release()
cv2.destroyAllWindows()
