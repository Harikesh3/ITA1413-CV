import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an image")
root.destroy()

if not image_path:
    raise SystemExit("No image selected.")

image = cv2.imread(image_path)
if image is None:
    raise SystemExit("The selected file could not be read as an image.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
if face_detector.empty() or eye_detector.empty():
    raise SystemExit("An OpenCV face or eye cascade could not be loaded.")

result = image.copy()
faces = face_detector.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
for x, y, width, height in faces:
    face_gray = gray[y:y + height, x:x + width]
    eyes = eye_detector.detectMultiScale(face_gray, 1.1, 5, minSize=(12, 12))
    for eye_x, eye_y, eye_width, eye_height in eyes:
        cv2.rectangle(result, (x + eye_x, y + eye_y), (x + eye_x + eye_width, y + eye_y + eye_height), (255, 0, 0), 2)
cv2.imshow("Eye Detection", result)
cv2.waitKey(0)
cv2.destroyAllWindows()