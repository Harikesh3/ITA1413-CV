import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog

root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an image")
watermark = simpledialog.askstring("Watermark", "Enter watermark text:", parent=root)
root.destroy()

if not image_path or not watermark:
    raise SystemExit("An image and watermark text are required.")

image = cv2.imread(image_path)
if image is None:
    raise SystemExit("The selected file could not be read as an image.")

result = image.copy()
height, width = result.shape[:2]
font_scale = max(0.5, min(width, height) / 900)
thickness = max(1, round(font_scale * 2))
text_size, baseline = cv2.getTextSize(watermark, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
origin = (max(0, width - text_size[0] - 20), max(text_size[1] + 20, height - baseline - 20))
layer = result.copy()
cv2.putText(layer, watermark, origin, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)
result = cv2.addWeighted(layer, 0.35, result, 0.65, 0)
cv2.imshow("Watermarked Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()