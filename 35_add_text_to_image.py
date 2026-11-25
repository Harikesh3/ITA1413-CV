import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog

root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an image")
text = simpledialog.askstring("Image Text", "Enter the text to place on the image:", parent=root)
root.destroy()

if not image_path or not text:
    raise SystemExit("Select an image and enter text.")

image = cv2.imread(image_path)
if image is None:
    raise SystemExit("The selected file could not be read as an image.")

height, width = image.shape[:2]
font_scale = max(0.5, min(width, height) / 900)
baseline_y = min(height - 5, max(30, int(height * 0.1)))
cv2.putText(image, text, (10, baseline_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow("Text on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()