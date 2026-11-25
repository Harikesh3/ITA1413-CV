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

source_roi = cv2.selectROI("Select source region", image, showCrosshair=True)
if source_roi[2] == 0 or source_roi[3] == 0:
    cv2.destroyAllWindows()
    raise SystemExit("No source region selected.")

source_x, source_y, source_width, source_height = map(int, source_roi)
cropped = image[source_y:source_y + source_height, source_x:source_x + source_width].copy()
destination_roi = cv2.selectROI("Select paste destination", image, showCrosshair=True)
if destination_roi[2] == 0 or destination_roi[3] == 0:
    cv2.destroyAllWindows()
    raise SystemExit("No destination region selected.")

destination_x, destination_y, destination_width, destination_height = map(int, destination_roi)
copied = cv2.resize(cropped, (destination_width, destination_height))
result = image.copy()
result[destination_y:destination_y + destination_height, destination_x:destination_x + destination_width] = copied
cv2.destroyAllWindows()
cv2.imshow("Cropped ROI", cropped)
cv2.imshow("ROI Pasted", result)
cv2.waitKey(0)
cv2.destroyAllWindows()