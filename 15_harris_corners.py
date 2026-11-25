import cv2
import numpy as np
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
response = cv2.cornerHarris(np.float32(gray), 2, 3, 0.04)
response = cv2.dilate(response, None)
result = image.copy()
result[response > 0.01 * response.max()] = (0, 0, 255)
cv2.imshow("Harris Corners", result)
cv2.waitKey(0)
cv2.destroyAllWindows()