import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
video_path = filedialog.askopenfilename(title="Select a video")
model_path = filedialog.askopenfilename(title="Select a vehicle-detection ONNX model", filetypes=[("ONNX model", "*.onnx"), ("All files", "*.*")])
root.destroy()

if not video_path or not model_path:
    raise SystemExit("Select both a video and a COCO-trained vehicle-detection ONNX model.")

try:
    network = cv2.dnn.readNetFromONNX(model_path)
except cv2.error as error:
    raise SystemExit(f"The selected ONNX model could not be loaded: {error}")

capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    raise SystemExit("The selected video could not be opened.")

vehicle_classes = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck"}
while True:
    success, frame = capture.read()
    if not success:
        break

    height, width = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (640, 640), swapRB=True, crop=False)
    network.setInput(blob)
    predictions = np.squeeze(network.forward())
    if predictions.ndim == 1:
        predictions = predictions.reshape(1, -1)
    if predictions.shape[0] <= 128 and predictions.shape[1] > predictions.shape[0]:
        predictions = predictions.T

    boxes = []
    scores = []
    labels = []
    for prediction in predictions:
        if prediction.size < 6:
            continue
        if prediction.size == 85:
            class_scores = prediction[5:]
            objectness = prediction[4]
        else:
            class_scores = prediction[4:]
            objectness = 1.0
        class_id = int(np.argmax(class_scores))
        confidence = float(class_scores[class_id] * objectness)
        if class_id not in vehicle_classes or confidence < 0.35:
            continue
        center_x, center_y, box_width, box_height = prediction[:4]
        left = int((center_x - box_width / 2) * width / 640)
        top = int((center_y - box_height / 2) * height / 640)
        box_width = int(box_width * width / 640)
        box_height = int(box_height * height / 640)
        boxes.append([left, top, box_width, box_height])
        scores.append(confidence)
        labels.append(vehicle_classes[class_id])

    for index in cv2.dnn.NMSBoxes(boxes, scores, 0.35, 0.45):
        index = int(index)
        left, top, box_width, box_height = boxes[index]
        cv2.rectangle(frame, (left, top), (left + box_width, top + box_height), (0, 255, 0), 2)
        cv2.putText(frame, f"{labels[index]} {scores[index]:.2f}", (left, max(20, top - 8)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Vehicle Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()