import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


def analyze_color_histogram(image):
    channel_names = ("Blue", "Green", "Red")
    histograms = {}
    for channel_index, channel_name in enumerate(channel_names):
        histogram = cv2.calcHist([image], [channel_index], None, [256], [0, 256])
        histograms[channel_name] = histogram.flatten()
    return histograms


root = tk.Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select a color image")
root.destroy()

if not image_path:
    raise SystemExit("No image selected.")

image = cv2.imread(image_path)
if image is None:
    raise SystemExit("The selected file could not be read as an image.")

histograms = analyze_color_histogram(image)
for color_name, color_values in histograms.items():
    plt.plot(color_values, label=color_name)
plt.title("Color-Level Histogram")
plt.xlabel("Intensity Level")
plt.ylabel("Pixel Count")
plt.xlim(0, 255)
plt.legend()
plt.tight_layout()
plt.show()