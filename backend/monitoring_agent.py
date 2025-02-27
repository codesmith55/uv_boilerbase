import cv2
import pyautogui
import numpy as np
import os
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)
CORS(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    typeDetails = db.Column(db.String(50), nullable=False)

scheduler = BackgroundScheduler()
scheduler.start()

def monitor_screen():
    with app.app_context():
        print("Monitoring screen...")  # Debugging statement
        # Capture screen

        # Define the region of interest (ROI) where the button is located
        # Adjust these coordinates based on the button's position on the screen
        x, y, w, h = 0, 0, 1, 1  # Example coordinates (x, y, width, height)

        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        # Draw a black outline around the ROI
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)

        # Extract the ROI
        roi = frame[y:y+h, x:x+w]

        # Convert the ROI to HSV color space
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Define the color ranges for red and green
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        lower_green = np.array([35, 100, 100])
        upper_green = np.array([85, 255, 255])

        # Create masks for red and green
        mask_red = cv2.inRange(hsv_roi, lower_red, upper_red)
        mask_green = cv2.inRange(hsv_roi, lower_green, upper_green)

        # Check if the button is red or green
        if np.any(mask_red):
            print("Button is red")
        elif np.any(mask_green):
            print("Button is green")
        else:
            print("Button color not detected")

        # Save the screenshot to the output folder
        output_folder = 'output'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        screenshot_path = os.path.join(output_folder, 'screenshot.png')
        cv2.imwrite(screenshot_path, frame)
        print(f"Screenshot saved to {screenshot_path}")

        # Display the frame with the outline (for debugging purposes)
        # cv2.imshow('Screen Monitor', frame)
        # cv2.waitKey(1)  # Wait for 1 ms to update the display

def add_scheduled_job(interval):
    print(f"Adding scheduled job with interval {interval} seconds")  # Debugging statement
    scheduler.add_job(monitor_screen, 'interval', seconds=interval)

@app.route('/start-monitoring', methods=['POST'])
def start_monitoring():
    data = request.json
    interval = data.get('interval', 5)  # Default interval is 5 seconds
    add_scheduled_job(interval)
    return jsonify({'message': 'Monitoring started'}), 200

if __name__ == '__main__':
    app.run(debug=True)