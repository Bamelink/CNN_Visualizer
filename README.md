# CNN_Visualizer
## Setup
Created with Python 3.11.3
```bash
pip install -r requirements.txt
```

## Drawer
The original code is from https://github.com/techwithtim/PythonPaintProgram with some small modifications made to fit the MNIST dataset.

## Visualizer
The Visualtier takes in the specified file as an image and colvolves with the selected kernel. The output is normalized to a range between 0-255 to fit a graysclaed image and also converted to red and green to show the detection with a better contrast.

Press "ESC" or the X in the top right corner to close the window.

See settings.py for the available kernels or create your own.