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

points = []


def select_point(event, x, y, flags, parameter):
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append((x, y))


window_name = "Select corners: top-left, top-right, bottom-right, bottom-left"
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, select_point)
while len(points) < 4:
    preview = image.copy()
    for point in points:
        cv2.circle(preview, point, 6, (0, 0, 255), -1)
    cv2.imshow(window_name, preview)
    if cv2.waitKey(20) & 0xFF == 27:
        cv2.destroyAllWindows()
        raise SystemExit("Corner selection cancelled.")

height, width = image.shape[:2]
source_points = np.float32(points)
destination_points = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
matrix = cv2.getPerspectiveTransform(source_points, destination_points)
transformed = cv2.warpPerspective(image, matrix, (width, height))
cv2.destroyAllWindows()
cv2.imshow("Perspective Transformation", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()