import cv2
import pyautogui
import numpy as np
import time

# Constants
WIDTH, HEIGHT = pyautogui.size()  # Get screen size
FLIP_MODE = -1  # -1 for both axes, 0 for vertical, 1 for horizontal
DELAY = 0.05  # Delay between frames

def capture_screen():
    """Captures the screen as an image."""
    screenshot = pyautogui.screenshot()  # Take a screenshot
    frame = np.array(screenshot)  # Convert to NumPy array
    return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV

def flip_screen(frame):
    """Flips the given frame based on FLIP_MODE."""
    return cv2.flip(frame, FLIP_MODE)

def main():
    """Main function to continuously capture, flip, and display the screen."""
    cv2.namedWindow("Flipped Screen", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Flipped Screen", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        frame = capture_screen()  # Capture screen
        flipped_frame = flip_screen(frame)  # Flip the screen
        cv2.imshow("Flipped Screen", flipped_frame)  # Display flipped screen

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(DELAY)  # Small delay to control update speed

    cv2.destroyAllWindows()  # Cleanup

if __name__ == "__main__":
    main()
