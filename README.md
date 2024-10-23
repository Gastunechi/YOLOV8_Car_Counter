# YOLOv8 Car Counter

## Introduction

This project implements an advanced **computer vision** solution for automatic vehicle counting from video streams. It uses the **YOLOv8** (You Only Look Once) object detection model to identify vehicles and the **SORT** (Simple Online and Realtime Tracking) algorithm to track detected objects across frames. The goal is to count vehicles crossing a predefined line in the image while maintaining high accuracy, even in dense and complex environments.

## Features

- **Real-time detection** of vehicles using **YOLOv8**.
- **Object tracking** with the **SORT** algorithm, enabling detection-to-detection association across frames.
- **Automatic counting** of vehicles crossing a virtual line in the video.
- **Enhanced accuracy** through advanced image processing techniques using **OpenCV** and **cvzone**.
- **Support for both live and pre-recorded videos**, offering flexibility for real-world applications like traffic monitoring.

## Prerequisites

- **Python 3.8+**
- **YOLOv8** and **SORT** for detection and tracking.
- **OpenCV** for image processing.
- **cvzone** to simplify working with OpenCV.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Car-Counter.git

2.Navigate to the project directory:
    ```bash
      cd Car-Counter
    ```

3.Install the required dependencies from requirements.txt:
  ```bash
  pip install -r requirements.txt
  ```

## Usage
1. Place the video you want to process in the project directory.

2. Run the main script to start the vehicle detection and counting process:
```bash
python Car_Counter.py --input <video_name.mp4>
```

3.The program will display real-time detections, vehicle tracking, and the total number of vehicles that have crossed the line.

## Project Structure
- Car_Counter.py: Main script handling vehicle detection, tracking, and counting.
- video_save_car_counter.py: Script for processing and saving annotated videos.
- sort.py: The SORT tracking algorithm for associating detections across frames.
- mask.png and graphics.png: Image files used for processing or display purposes.
- requirements.txt: List of required dependencies for the project.
  
## How It Works
- Detection: Each video frame is passed through the YOLOv8 model, which identifies vehicles and outputs bounding boxes.
- Tracking: Detected objects are tracked using SORT, assigning unique IDs to vehicles and linking detections across frames.
- Counting: When a vehicle crosses a predefined line in the image, it is counted. The position of this line can be adjusted based on the scene.

## Results and Performance
- Detection Accuracy: The project achieves high detection accuracy, optimized by using the YOLOv8 model.
- Robust Tracking: With SORT, the system tracks vehicles effectively even in dense scenes.
- Real-time Processing: The project can handle real-time video processing with minimal latency.

## Screenshot
## Screenshot

The following images demonstrate the vehicle detection and counting process at various stages:

1. **Before Crossing the Line**:
   ![Before Crossing the Line](8eme_voiture_avant.jpg)
   This image shows the vehicle detection before crossing the predefined line.

2. **During Crossing the Line**:
   ![During Crossing the Line](8eme_voiture_pendant.jpg)
   Here, the vehicle is in the process of crossing the line, illustrating real-time tracking and detection.

3. **After Crossing the Line**:
   ![After Crossing the Line](8eme_voiture_apres.jpg)
   This image captures the moment after the vehicle has crossed the line, highlighting the successful count increment.

These screenshots provide a clear view of how the system tracks and counts each vehicle accurately, demonstrating the effectiveness of the YOLOv8 and SORT integration in a real-world traffic scenario.


## Contributions
Contributions are welcome. For any suggestions or improvements, please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
