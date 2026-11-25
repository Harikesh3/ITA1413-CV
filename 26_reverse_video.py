import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
video_path = filedialog.askopenfilename(title="Select a video")
output_path = filedialog.asksaveasfilename(title="Save reversed video", defaultextension=".mp4", filetypes=[("MP4 video", "*.mp4")])
root.destroy()

if not video_path or not output_path:
    raise SystemExit("Select a source video and output file.")

capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    raise SystemExit("The selected video could not be opened.")

fps = capture.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 25
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames = []
while True:
    success, frame = capture.read()
    if not success:
        break
    frames.append(frame)
capture.release()

if not frames:
    raise SystemExit("The video contains no readable frames.")

writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))
for frame in reversed(frames):
    writer.write(frame)
writer.release()
print(f"Saved reversed video to {output_path}")