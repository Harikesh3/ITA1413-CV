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

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
top_hat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Grayscale Input", gray)
cv2.imshow("Top Hat", top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()