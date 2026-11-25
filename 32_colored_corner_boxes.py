import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()
width = simpledialog.askinteger("Image Width", "Enter image width:", minvalue=10, parent=root)
height = simpledialog.askinteger("Image Height", "Enter image height:", minvalue=10, parent=root)
root.destroy()

if width is None or height is None:
    raise SystemExit("Image width and height are required.")

image = np.full((height, width, 3), 255, dtype=np.uint8)
box_width = max(1, width // 10)
box_height = max(1, height // 10)
colors = ((0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255))
corners = ((0, 0), (width - box_width, 0), (0, height - box_height), (width - box_width, height - box_height))
for color, (x, y) in zip(colors, corners):
    image[y:y + box_height, x:x + box_width] = color

cv2.imshow("White Image with Colored Corner Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()