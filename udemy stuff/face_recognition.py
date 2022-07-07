#importing library
import cv2

# loading the cascades
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


# defining function

# def detect(gray, frame):
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
