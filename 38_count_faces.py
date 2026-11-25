import cv2
import tkinter as tk
from tkinter import filedialog


def count_faces(image):
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(cascade_path)
    if detector.empty():
        raise RuntimeError("The OpenCV face cascade could not be loaded.")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return len(faces), faces


root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an image")
root.destroy()

if not image_path:
    raise SystemExit("No image selected.")

image = cv2.imread(image_path)
if image is None:
    raise SystemExit("The selected file could not be read as an image.")

face_count, faces = count_faces(image)
result = image.copy()
for x, y, width, height in faces:
    cv2.rectangle(result, (x, y), (x + width, y + height), (0, 255, 0), 2)
cv2.putText(result, f"Faces: {face_count}", (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
print(f"Number of faces: {face_count}")
cv2.imshow("Face Count", result)
cv2.waitKey(0)
cv2.destroyAllWindows()