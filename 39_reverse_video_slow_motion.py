import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
video_path = filedialog.askopenfilename(title="Select a video")
root.destroy()

if not video_path:
    raise SystemExit("No video selected.")

capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    raise SystemExit("The selected video could not be opened.")

fps = capture.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 25
delay = max(1, round(3000 / fps))
frames = []
while True:
    success, frame = capture.read()
    if not success:
        break
    frames.append(frame)
capture.release()

if not frames:
    raise SystemExit("The video contains no readable frames.")

for frame in reversed(frames):
    cv2.imshow("Reverse Video Slow Motion", frame)
    if cv2.waitKey(delay) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()