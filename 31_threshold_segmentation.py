import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog

root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an image")
threshold_value = simpledialog.askinteger("Threshold", "Enter threshold from 0 to 255:", minvalue=0, maxvalue=255, parent=root)
root.destroy()

if not image_path or threshold_value is None:
    raise SystemExit("Select an image and enter a threshold.")

image = cv2.imread(image_path)
if image is None:
    raise SystemExit("The selected file could not be read as an image.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, segmented = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
cv2.imshow("Original", image)
cv2.imshow(f"Threshold Segmentation: {threshold_value}", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()