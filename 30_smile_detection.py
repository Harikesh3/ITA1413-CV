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
smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
if face_detector.empty() or smile_detector.empty():
    raise SystemExit("An OpenCV face or smile cascade could not be loaded.")

result = image.copy()
faces = face_detector.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
smile_count = 0
for x, y, width, height in faces:
    face_gray = gray[y:y + height, x:x + width]
    smiles = smile_detector.detectMultiScale(face_gray, 1.7, 20, minSize=(20, 10))
    for smile_x, smile_y, smile_width, smile_height in smiles:
        smile_count += 1
        cv2.rectangle(result, (x + smile_x, y + smile_y), (x + smile_x + smile_width, y + smile_y + smile_height), (0, 255, 0), 2)
cv2.putText(result, f"Smiles: {smile_count}", (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("Smile Detection", result)
cv2.waitKey(0)
cv2.destroyAllWindows()