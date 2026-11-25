import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select the image to search")
template_path = filedialog.askopenfilename(title="Select a watch template image")
root.destroy()

if not image_path or not template_path:
    raise SystemExit("Select both a source image and a watch template.")

image = cv2.imread(image_path)
template = cv2.imread(template_path)
if image is None or template is None:
    raise SystemExit("One of the selected files could not be read as an image.")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
image_height, image_width = gray_image.shape
template_height, template_width = gray_template.shape
if template_height > image_height or template_width > image_width:
    raise SystemExit("The watch template must be smaller than the source image.")

matches = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)
_, confidence, _, location = cv2.minMaxLoc(matches)
result = image.copy()
if confidence >= 0.5:
    opposite = (location[0] + template_width, location[1] + template_height)
    cv2.rectangle(result, location, opposite, (0, 255, 0), 3)
    label = f"Watch match: {confidence:.2f}"
else:
    label = f"No confident match: {confidence:.2f}"
cv2.putText(result, label, (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
cv2.imshow("Watch Recognition by Template Matching", result)
cv2.waitKey(0)
cv2.destroyAllWindows()