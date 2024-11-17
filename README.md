# Lock On: OpenCV-Based Face Tracking for Real-Time Target Positioning

This project utilizes OpenCV to perform real-time face tracking. By detecting and tracking faces in live video input, the program continuously identifies and displays the center position of the detected face, which can be used for applications such as target positioning and real-time tracking systems.

## Features

- **Real-Time Face Detection and Tracking**: Uses Haar Cascade Classifiers to detect faces in real time.
- **CSRT Tracker**: Once a face is detected, the program initializes the CSRT (Channel and Spatial Reliability Tracker) for robust, high-accuracy face tracking.
- **Target Positioning Display**: The program calculates and displays the center of the face, updating it continuously on-screen as the face moves.
- **Automatic Re-Detection**: If the tracker loses the face, it will automatically attempt to detect and reinitialize tracking.

## Requirements

Ensure the following libraries are installed:

```bash
pip install opencv-python opencv-contrib-python
```

- **OpenCV**: Used for image processing and tracking algorithms.

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pratz222/OpenCV-based-Face-Tracking-for-Real-Time-Target-Positioning
   cd lockon
   ```

2. **Run the Code**:
   Execute the following command in the project directory:
   ```bash
   python lockon.py
   ```

3. **Quit the Program**:
   - Press `q` to exit the program at any time.

## Usage

1. **Face Detection**: The program first detects faces in the video feed.
2. **Initialize Tracking**: Upon detection, it initializes the tracker, displaying a bounding box around the face.
3. **Display Target Position**: The program calculates and displays the center coordinates of the face as the target position.
4. **Reinitialize on Loss**: If tracking is lost, the program automatically searches for a new face.

## Code Overview

- **Face Detection**: Uses Haar cascades to detect faces in real time from the video input.
- **Face Tracking**: Once a face is detected, the CSRT tracker is initialized to track its position across frames.
- **Position Display**: Displays the x and y coordinates of the face’s center on the screen.

## Alternative Trackers

If you encounter compatibility issues with the CSRT tracker, consider using one of these alternative OpenCV trackers:
- **MIL** tracker: `cv2.TrackerMIL_create()`
- **KCF** tracker: `cv2.TrackerKCF_create()`

To use an alternative tracker, replace:
```python
tracker = cv2.TrackerCSRT_create()
```
with the relevant tracker creation line, such as `tracker = cv2.TrackerMIL_create()`.

## Example Output

The program displays a real-time video feed with:
- A bounding box around the tracked face
- The face’s center coordinates labeled as the target position
