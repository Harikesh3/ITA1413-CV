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

height, width = image.shape[:2]
larger = cv2.resize(image, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)
smaller = cv2.resize(image, (max(1, width // 2), max(1, height // 2)), interpolation=cv2.INTER_AREA)
cv2.imshow("Original", image)
cv2.imshow("Larger 2x", larger)
cv2.imshow("Smaller 0.5x", smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()