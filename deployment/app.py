import cvzone
import numpy as np
import cv2
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
from PIL import Image




# Configure Google generative AI
genai.configure(api_key="AIzaSyB276-hKMAXayPaHj0caoOXApV-1sr503M")  # Replace with your actual API key
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the HandDetector
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)


def getHandInfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    else:
        return None


def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, tuple(current_pos), tuple(prev_pos), (255, 0, 255), 10)
    elif fingers == [1, 1, 1, 1, 1]:
        canvas = np.zeros_like(img)
    return current_pos, canvas


def sendToAI(model, canvas, fingers):
    if fingers == [1, 1, 1, 0, 0]:
        Pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve this Math Problem", Pil_image])
        print( response.text)


prev_pos = None
canvas = None

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)

    info = getHandInfo(img)
    if info:
        fingers, lmList = info
        print(fingers)
        prev_pos, canvas = draw(info, prev_pos, canvas)
        sendToAI(model, canvas, fingers)

    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    # Display the image in a window
    cv2.imshow("Image", img)
    cv2.imshow("Canvas", canvas)
    cv2.imshow("image_combined", image_combined)

    cv2.waitKey(1)

# Release the webcam
cap.release()
cv2.destroyAllWindows()