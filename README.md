# Webcam Motion Detection

This Python script captures video from your webcam and detects motion in real-time using OpenCV. When motion is detected, it saves a snapshot and produces a beep sound.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python
- OpenCV (`opencv-python` package)
- `winsound` (usually comes with Python)

You can install OpenCV via pip:
pip install opencv-python


## Usage

1. Clone this repository to your local machine:



2. Navigate to the project directory:

cd webcam-motion-detection

3. Run the script:

python motion_detection.py


4. Press the `Esc` key to exit the application.

## How it Works

- The script captures video from your default webcam (`VideoCapture(0)`).
- It continuously compares two consecutive frames to detect differences.
- If the difference surpasses a certain threshold, it is considered motion.
- The detected motion is outlined with a bounding box and saved as 'motion.png.'
- A beep sound is played when motion is detected.

## Customization

You can customize the motion detection parameters (such as the threshold and contour area) by modifying the script variables:

- `THRESHOLD`: Adjust the value to control the sensitivity of motion detection.
- `MIN_CONTOUR_AREA`: Set the minimum contour area to consider as motion.

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the OpenCV and Python communities for their contributions.

---

*This README template is for educational purposes and can be customized for your specific project.*



