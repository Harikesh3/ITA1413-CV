import cv2
import pytesseract
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
video_path = filedialog.askopenfilename(title="Select a video")
tesseract_path = filedialog.askopenfilename(title="Select tesseract.exe", filetypes=[("Tesseract executable", "tesseract.exe"), ("Executable", "*.exe")])
output_path = filedialog.asksaveasfilename(title="Save extracted text", defaultextension=".txt", filetypes=[("Text file", "*.txt")])
root.destroy()

if not video_path or not tesseract_path or not output_path:
    raise SystemExit("Select a video, Tesseract executable, and output text file.")

pytesseract.pytesseract.tesseract_cmd = tesseract_path
capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    raise SystemExit("The selected video could not be opened.")

fps = capture.get(cv2.CAP_PROP_FPS)
frame_interval = max(1, round(fps)) if fps > 0 else 25
frame_index = 0
last_text = ""
extracted = []
while True:
    success, frame = capture.read()
    if not success:
        break
    if frame_index % frame_interval == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray).strip()
        if text and text != last_text:
            extracted.append(f"Frame {frame_index}:\n{text}")
            last_text = text
    frame_index += 1
capture.release()

with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write("\n\n".join(extracted))
print(f"Extracted text from {len(extracted)} sampled frames to {output_path}")