import pyautogui
import cv2
import numpy as np
import keyboard
import time

# List to store highlighted regions
highlighted_regions = []

# Function to draw a yellow rectangle on the screen
def draw_highlight(x, y, w, h):
    print(f"draw_highlight region: ({x}, {y}, {w}, {h})")
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.imshow('Highlight', frame)
    cv2.waitKey(1)

# Function to capture the highlighted region
def capture_highlighted_region(x, y, w, h):
    highlighted_regions.append((x, y, w, h))
    print(f"Highlighted region: ({x}, {y}, {w}, {h})")
    draw_highlight(x,y,w,h)

# Function to print all highlighted regions
def print_highlighted_regions():
    print("Highlighted regions:")
    for region in highlighted_regions:
        print(region)

# Main function to run the helper program
def main():
    global highlighted_regions
    highlighted_regions = []
    first_z_pressed = False
    start_x, start_y = None, None

    print("Press 'Z' to start highlighting and 'Z' again to stop.")
    print("Double press 'B' to print all highlighted regions and exit.")

    while True:
        if keyboard.is_pressed('z'):
            time.sleep(0.1)  # Debounce delay
            if not first_z_pressed:
                # First 'Z' key press
                first_z_pressed = True
                start_x, start_y = pyautogui.position()
                print(f"Highlight started at ({start_x}, {start_y})")
            else:
                # Second 'Z' key press
                first_z_pressed = False
                end_x, end_y = pyautogui.position()
                width = abs(end_x - start_x)
                height = abs(end_y - start_y)
                capture_highlighted_region(min(start_x, end_x), min(start_y, end_y), width, height)
                print(f"Highlight ended at ({end_x}, {end_y})")
                #draw_highlight(min(start_x, end_x), min(start_y, end_y), width, height)

        if keyboard.is_pressed('b'):
            time.sleep(0.1)  # Debounce delay
            if keyboard.is_pressed('b'):
                print_highlighted_regions()
                break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()