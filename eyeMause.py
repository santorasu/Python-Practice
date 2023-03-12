# Eye mouse project in Python

import cv2
import numpy as np
import pyautogui

# Define the video capture device
cap = cv2.VideoCapture(0)

# Define the color range for the eye detection
lower_eye_color = np.array([0, 0, 0])
upper_eye_color = np.array([255, 255, 255])

# Define the size of the window and the delay time
window_size = (640, 480)
delay_time = 1

# Define the size of the screen for the mouse control
screen_width, screen_height = pyautogui.size()

# Define the minimum and maximum movement thresholds for the mouse control
min_movement_threshold = 10
max_movement_threshold = 100

# Define the scaling factors for the mouse control
x_scale_factor = screen_width / window_size[0]
y_scale_factor = screen_height / window_size[1]

# Initialize the previous position of the eye
previous_eye_position = None

# Loop until the user presses the 'q' key
while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to the grayscale image
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # Detect the edges in the blurred image
    edges = cv2.Canny(blurred, 50, 150)

    # Find the contours in the edges image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area
    largest_contour = None
    largest_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > largest_area:
            largest_area = area
            largest_contour = contour

    # Find the centroid of the largest contour
    if largest_contour is not None:
        moments = cv2.moments(largest_contour)
        if moments["m00"] != 0:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])
            eye_position = (cx, cy)

            # Move the mouse cursor based on the change in eye position
            if previous_eye_position is not None:
                dx = (eye_position[0] - previous_eye_position[0]) * x_scale_factor
                dy = (eye_position[1] - previous_eye_position[1]) * y_scale_factor
                movement_threshold = min(max(abs(dx), abs(dy)), max_movement_threshold)
                if movement_threshold > min_movement_threshold:
                    pyautogui.moveRel(dx, dy)

            # Draw a circle at the centroid of the largest contour
            cv2.circle(frame, eye_position, 5, (0, 255, 0), -1)

            # Store the current eye position as the previous position for the next iteration
            previous_eye_position = eye_position

    # Show the frame in a window
    cv2.imshow("Eye Mouse", cv2.resize(frame, window_size))

    # Check if the user has pressed the 'q' key
    if cv2.waitKey(delay_time) & 0xFF == ord('q'):
        break

# Release
