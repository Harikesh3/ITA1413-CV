import argparse
import cv2
import tkinter as tk
from tkinter import filedialog

parser = argparse.ArgumentParser(description="Convert an image to grayscale.")
parser.add_argument("--input", help="Path to the input image.")
parser.add_argument("--output", help="Path for the grayscale output image.")
args = parser.parse_args()

image_path = args.input
if not image_path:
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(title="Select an image")
    root.destroy()

if not image_path:
    raise SystemExit("No image selected.")

image = cv2.imread(image_path)
if image is None:
    raise SystemExit("The selected file could not be read as an image.")

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if args.output:
    if not cv2.imwrite(args.output, grayscale):
        raise SystemExit("The grayscale image could not be written.")
else:
    cv2.imshow("Original", image)
    cv2.imshow("Grayscale", grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()