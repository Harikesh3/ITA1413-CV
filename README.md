# ITA1413-CV: Computer Vision Experiments

Each numbered Python file is a separate experiment. Run it from this folder with the workspace virtual environment:

```powershell
.\.venv\Scripts\python.exe .\01_grayscale.py
```

Replace `01_grayscale.py` with the experiment file you want to run. Image and video experiments open a file picker when started. Press a key in an OpenCV window to close it; video playback experiments use `q` to stop playback.

Install dependencies with:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Experiment 25 asks for a source image and a smaller image of the watch to use as a template. Experiment 28 also asks for a COCO-trained vehicle-detection ONNX model. Experiment 40 requires the Tesseract OCR application installed on Windows and asks you to select its `tesseract.exe` file.

The HSV color limits in experiments 36 and 37 are set near the top of each file and can be adjusted for the colors in the chosen image. OpenCV displays image results in separate windows.
