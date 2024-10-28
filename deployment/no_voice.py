import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import streamlit as st

# Streamlit configuration
st.set_page_config(layout="wide")
st.image('thelastofai.png')

col1, col2 = st.columns([3, 2])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Answer")
    output_text_area = st.empty()  # Area to display recognized hand sign in one line

# Initialize the webcam to capture video
cap = cv2.VideoCapture(0)  # Use the built-in camera (index 0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

# Define hand signs and corresponding text outputs
hand_signs = {
    (0, 1, 0, 0, 0): "Hello There",
    (1, 1, 1, 0, 0): "Yes",
    (0, 1, 1, 0, 0): "Peace",
    (1, 0, 0, 0, 0): "is",
    (1, 1, 1, 1, 1): "Stop!",
    (0, 0, 0, 0, 1): "My",
    (1, 0, 0, 0, 1): "Name",
    (1, 0, 1, 0, 0): "Hello",
    (0, 1, 0, 1, 0): "Thank you",
    (1, 1, 0, 1, 0): "Welcome",
    (0, 0, 1, 1, 0): "Goodbye",
    (0, 1, 0, 1, 1): "Help",
    (1, 0, 1, 0, 1): "Please",
    (0, 1, 1, 1, 0): "Sorry",
    (1, 1, 0, 0, 1): "Good Morning",
    (1, 0, 1, 1, 1): "Good Night",
    (0, 0, 1, 0, 1): "How are you?",
    (1, 1, 0, 1, 1): "I love you",
    (0, 0, 1, 1, 1): "Congratulations",
    (1, 0, 1, 1, 0): "Good luck",
    (0, 1, 1, 0, 1): "Take care",
    (1, 1, 1, 0, 1): "See you",
    (1, 0, 0, 1, 0): "Nice to meet you"
}

# Function to get hand information from the image
def getHandInfo(img):
    try:
        hands, img = detector.findHands(img, draw=False, flipType=True)
        if hands:
            hand = hands[0]
            lmList = hand["lmList"]
            fingers = detector.fingersUp(hand)
            return fingers, lmList
        else:
            return None
    except Exception as e:
        st.error(f"An error occurred while detecting hands: {e}")
        return None

# Function to interpret hand sign based on detected fingers
def interpret_hand_sign(fingers):
    return hand_signs.get(tuple(fingers), None)

# Initialize canvas and output variables
canvas = None
output_text = ""

while True:  # Infinite loop for continuous video capture
    if run:
        success, img = cap.read()
        if not success or img is None:
            st.error("Failed to capture image from camera.")
            continue

        img = cv2.flip(img, 1)

        if canvas is None:
            canvas = np.zeros_like(img)

        info = getHandInfo(img)
        if info:
            fingers, lmList = info
            # Interpret hand sign based on the detected fingers
            recognized_text = interpret_hand_sign(fingers)
            
            # If recognized and not already displayed in the line, append it
            if recognized_text and (output_text == "" or not output_text.endswith(recognized_text)):
                output_text += " " + recognized_text  # Append new sign to existing text
                output_text_area.markdown(f"**{output_text.strip()}**")  # Display all recognized signs in one line

        # Display video feed
        image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
        FRAME_WINDOW.image(image_combined, channels="BGR")

        cv2.waitKey(1)  # Keep the video feed running

# Release resources
cap.release()
cv2.destroyAllWindows()
