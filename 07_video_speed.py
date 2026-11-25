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
base_delay = max(1, round(1000 / fps))

for mode_name, delay in (("Normal Speed", base_delay), ("Slow Motion", base_delay * 3), ("Fast Motion", max(1, base_delay // 3))):
    capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
    while True:
        success, frame = capture.read()
        if not success:
            break
        cv2.imshow(mode_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord("q"):
            break
    cv2.destroyWindow(mode_name)

capture.release()
cv2.destroyAllWindows()