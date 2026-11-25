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

height, width = image.shape[:2]
source_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1]])
destination_points = np.float32([[width * 0.08, height * 0.12], [width * 0.92, height * 0.04], [width * 0.18, height * 0.9]])
matrix = cv2.getAffineTransform(source_points, destination_points)
transformed = cv2.warpAffine(image, matrix, (width, height))
cv2.imshow("Original", image)
cv2.imshow("Affine Transformation", transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()