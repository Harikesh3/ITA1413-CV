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

lower = np.array([35, 40, 40], dtype=np.uint8)
upper = np.array([85, 255, 255], dtype=np.uint8)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
foreground_mask = cv2.inRange(hsv, lower, upper)
foreground = cv2.bitwise_and(image, image, mask=foreground_mask)
background = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(foreground_mask))
cv2.imshow("Selected Foreground Color", foreground)
cv2.imshow("Foreground Subtracted", background)
cv2.waitKey(0)
cv2.destroyAllWindows()