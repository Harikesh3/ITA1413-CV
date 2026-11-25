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

kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(image, kernel, iterations=1)
cv2.imshow("Original", image)
cv2.imshow("Eroded", eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()