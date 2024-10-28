# train.py

# developer-Ahmed Pasha. More work @ , visit: https://github.com/ahmed-pasha

# Overview:
# This project does not involve a traditional training process since it uses a predefined rule-based system
# for recognizing hand signs. Instead of training a machine learning model, we use hand landmarks and finger positions
# to identify specific gestures. 

# The process works as follows:
# 1. We capture video frames using OpenCV and use CvZone's HandDetector to detect hand landmarks in real time.
# 2. The HandDetector identifies the state (up or down) of each finger based on the position of the landmarks.
# 3. Each gesture is defined by a specific combination of finger states (up/down), represented as a tuple of binary values.
#    For example, (0, 1, 0, 0, 0) may represent "Hello There," where each value indicates whether a finger is up (1) or down (0).
# 4. We use a dictionary to map these tuples to corresponding text phrases. When a gesture matches a key in this dictionary,
#    the associated phrase is displayed as text.
# 5. This approach allows for real-time conversion of recognized hand gestures into text without requiring model training.

# Author: Ahmed Pasha
# GitHub: https://github.com/ahmed-pasha
