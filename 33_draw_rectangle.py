import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()
width = simpledialog.askinteger("Image Width", "Enter image width:", minvalue=1, parent=root)
height = simpledialog.askinteger("Image Height", "Enter image height:", minvalue=1, parent=root)
root.destroy()

if width is None or height is None:
    raise SystemExit("Image width and height are required.")

image = np.full((height, width, 3), 255, dtype=np.uint8)
margin_x = max(1, width // 5)
margin_y = max(1, height // 5)
cv2.rectangle(image, (margin_x, margin_y), (width - margin_x, height - margin_y), (0, 0, 255), 3)
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()