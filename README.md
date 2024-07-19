# parking-space-detection
# Parking Space Detection and Counter using Open-CV and Python
### ParkingSpacePicker.py - used for adding all the parking spaces 
### main.py - used for the detection of parking space and count the number of available parking spaces
# ***sPark*** : Automated Parking Space detection using open-cv & python :

This project shows how to create a parking space finder with OpenCV Python. It tells apart empty and full spaces by looking at car size. It doesn't use deep learning or machine learning. The project talks about the hard parts of picking out areas to watch and dealing with odd shapes. It stresses that you need to mark areas by hand to get it right. The project goes over making files to pick parking spaces, keeping rectangles with pickle, and running video feeds over and over to test the code. It also shows how to crop and check each parking space for cars. It figures out if cars are there by using thresholding and adaptive thresholding. It shows the number of non-zero pixels in each space and lets you change the text size. The project also tweaks threshold values to tell parking spaces apart better. It shows open and taken spaces in different colors.

### **Project Overview :** 

- 🚗 **Introduction and Project Overview:** The video introduces a project to create a parking space finder and counter using image processing techniques, without deep learning or machine learning. The system indicates the number of free and occupied parking spaces.
- **🔧 Setting Up the Environment:** Detailed instructions on setting up the project in PyCharm, installing necessary packages like OpenCV, NumPy, and  CVZone, and configuring the project interpreter.
- 📷 **Image Processing Techniques:** Explanation of image processing techniques used to detect and count parking spaces, including converting images to grayscale, applying Gaussian blur, and using adaptive thresholding to distinguish between occupied and free spaces.
- 💾 **Saving and Loading Data:** Demonstration of using Python's pickle module to save and load the positions of parking spaces, allowing the system to remember the marked spaces across sessions.
- 🔍 **Cropping and Counting Pixels:** Steps to crop images to the regions of interest (parking spaces) and counting the number of non-zero pixels to determine if a space is occupied.
- ✅ **Final Implementation:** Combining all steps to create a robust parking space counter, handling camera movement, and refining the detection parameters for accuracy.

### **Conclusion :** This project shows the strength of simple image processing methods for tackling real-world issues. Using OpenCV and Python, we built a reliable parking space counter that spots open parking spots as they happen.
