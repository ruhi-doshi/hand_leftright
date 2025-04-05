REAL TIME HAND-TRACKING AND MOVEMENT DETECTION

1. This Python project uses MediaPipe and OpenCV to perform real-time hand tracking using a webcam. It can detect:
2. The left, right, or both hands
3. Vertical hand movements (up and down) based on wrist position


FEATURES

1. Detects and tracks up to 2 hands in real-time
2. Displays the hand label (Left, Right, or Both)
3. Monitors wrist movement direction (up/down)
4. Visualizes hand landmarks with connections using MediaPipe


HOW IT WORKS

1. Uses MediaPipe’s Hands solution to detect and track hands.
2. Tracks the wrist position to determine vertical movement.
3. Compares current wrist Y-coordinate to previous frame’s Y-coordinate:
4. If wrist moves up, displays "Up" in green.
5. If wrist moves down, displays "Down" in red.
Also identifies whether the hand is left, right, or if both hands are visible.
