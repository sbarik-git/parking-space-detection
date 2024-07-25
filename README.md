# ***sPark*** : Automated Parking Space detection using open-cv & python :
<img src="https://github.com/user-attachments/assets/5e893129-feb6-4764-a4f4-763c399e9302" width="500" />

# Overview

The main goal of this project is to detect and monitor car parking spaces. It consists of two main parts:

1. **parkingspacepicker.py**: This Python script allows you to manually select parking space coordinates on a static image (`carParkImg.png`). You can left-click to mark parking spaces and right-click to remove them. The coordinates are saved in a file named `CarParkPos` using pickle.

2. **main.py**: This Python script reads the saved parking space coordinates and processes a video feed (`carPark.mp4`) to detect the occupancy of parking spaces. It displays the video with marked parking spaces and updates the count of free spaces in real-time.

## Installation

1. Install the required dependencies, including OpenCV and cvzone:

   ```bash
   pip install opencv-python-headless
   pip install numpy
   pip install cvzone
   ```

2. Ensure you have the following files in your project folder:

   - `carPark.mp4` (video file)
   - `carParkImg.png` (static image of the parking lot)
   - `parkingspacepicker.py`
   - `main.py`

## Usage

1. Run `parkingspacepicker.py` to mark the parking spaces on the static image. Left-click to add parking spaces and right-click to remove them. The coordinates will be saved in `CarParkPos`.

2. Run `main.py` to start processing the video feed and detecting parking space occupancy. The video will display with marked parking spaces and a count of free spaces.

## Files and Folders

- `carPark.mp4`: Input video file containing the parking lot footage.
- `carParkImg.png`: Static image of the parking lot for marking parking spaces.
- `parkingspacepicker.py`: Script to select and save parking space coordinates.
- `main.py`: Script for processing the video and detecting parking space occupancy.
- `CarParkPos`: Binary file containing saved parking space coordinates (created by `parkingspacepicker.py`).

## **Project Overview :** 

- 🚗 **Introduction and Project Overview:** The video introduces a project to create a parking space finder and counter using image processing techniques, without deep learning or machine learning. The system indicates the number of free and occupied parking spaces.
- **🔧 Setting Up the Environment:** Detailed instructions on setting up the project in PyCharm, installing necessary packages like OpenCV, NumPy, and  CVZone, and configuring the project interpreter.
- 📷 **Image Processing Techniques:** Explanation of image processing techniques used to detect and count parking spaces, including converting images to grayscale, applying Gaussian blur, and using adaptive thresholding to distinguish between occupied and free spaces.
- 💾 **Saving and Loading Data:** Demonstration of using Python's pickle module to save and load the positions of parking spaces, allowing the system to remember the marked spaces across sessions.
- 🔍 **Cropping and Counting Pixels:** Steps to crop images to the regions of interest (parking spaces) and counting the number of non-zero pixels to determine if a space is occupied.
- ✅ **Final Implementation:** Combining all steps to create a robust parking space counter, handling camera movement, and refining the detection parameters for accuracy.

# **Conclusion & Output :**
This project shows the strength of simple image processing methods for tackling real-world issues. Using OpenCV and Python, we built a reliable parking space counter that spots open parking spots as they happen.
<img src="https://github.com/user-attachments/assets/d68a7b66-b855-40d0-ab88-91f2dadcd30e" width="500" />
<img src="https://github.com/user-attachments/assets/8fb6616a-e945-4437-b03d-efdcfa64edb7" width="500" />


