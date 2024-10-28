### Sign Language Tutor
Project by **Ahmed Pasha**, enables real-time hand sign language recognition, converting recognized signs into corresponding text. It uses a trained neural network model to detect and classify hand signs from video input.

## Features
- Recognizes hand signs (A-Z) using a webcam.
- Dynamically generates and displays a sentence based on recognized signs.
- Adds a space when no hand is detected.
- Allows erasing the entire sentence by pressing the E key.
- Interactive tutorials with visual aids for each letter of the ASL alphabet.
- Hand gesture recognition using OpenCV, TensorFlow, and MediaPipe.
- Progress tracking for users to monitor their learning journey.
- Additional community resources for ASL learners.
## How to Use
1. Run the Python script to start the webcam and hand sign recognition.
2. Show hand signs in front of the camera for real-time recognition.
3. The recognized signs will appear as text on the screen.
4. Press E to erase the current sentence.
## Requirements
- Python 3.x
- TensorFlow
- OpenCV
- MediaPipe

## Setup
1. Clone this repository:

```git clone https://github.com/ahmed-pasha/Sign-Language-Alphabet-Tutor.git ```
2. Install the required dependencies:

```pip install -r requirements.txt```
## Run the program:

```python sign_language_recognition.py```

## Dataset
The hand sign data is collected from custom images using MediaPipe and trained using a neural network in Keras.
## Model
The trained model (hand_sign_model.keras) is included for prediction purposes. The model can recognize hand signs from A-Z.
## License
This project is licensed under the MIT License. Ownership of the code and documentation belongs to Ahmed Pasha. Redistribution or use in source and binary forms, with or without modification, are permitted provided the terms of the MIT License are followed.

For more details, visit my GitHub: Ahmed Pasha's GitHub.
