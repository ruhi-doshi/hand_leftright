REAL TIME HAND-TRACKING AND MOVEMENT DETECTION

This Python project uses MediaPipe and OpenCV to perform real-time hand tracking using a webcam. It can detect:
The left, right, or both hands
Vertical hand movements (up and down) based on wrist position


FEATURES
Detects and tracks up to 2 hands in real-time
Displays the hand label (Left, Right, or Both)
Monitors wrist movement direction (up/down)
Visualizes hand landmarks with connections using MediaPipe


HOW IT WORKS
Uses MediaPipe’s Hands solution to detect and track hands.
Tracks the wrist position to determine vertical movement.
Compares current wrist Y-coordinate to previous frame’s Y-coordinate:
If wrist moves up, displays "Up" in green.
If wrist moves down, displays "Down" in red.
Also identifies whether the hand is left, right, or if both hands are visible.
