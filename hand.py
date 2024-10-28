import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize the HandDetector
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip the image horizontally

    hands, img = detector.findHands(img, draw=True, flipType=True)
    
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        hand_type = hand["type"]
        
        # Display the number of fingers and hand type on the image
        cv2.putText(img, f'Fingers: {str(fingers)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(img, f'Hand: {hand_type}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the image in a window
    cv2.imshow("Image", img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
