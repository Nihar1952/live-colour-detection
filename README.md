# live-colour-detection
Uses OpenCV to capture real time webcam feed.
Detects colours by double-clicking on any pixel. 
Displays a box with the nearest color name and RGB values based on the colors.csv dataset using a KD-Tree for fast color matching.

Required libraries:
numpy, pandas, scipy, and opencv

Package installation command:
pip install opencv-python pandas numpy scipy

Usage:
python color.py
Double-click anywhere in the window to detect color.
Press Esc to exit.

This project uses a licensed dataset for color names and RGB values, available on Kaggle:
[Color Detection Dataset on Kaggle](https://www.kaggle.com/datasets/pypiahmad/color-detection-dataset)  
Created by: [@pypiahmad](https://www.kaggle.com/pypiahmad)  
License: Refer to the dataset's [licence.txt](https://www.kaggle.com/datasets/pypiahmad/color-detection-dataset?select=license.txt)
