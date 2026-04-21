"""

import cv2
import matplotlib.pyplot as plt

# Read images
img1 = cv2.imread("data/1-b.png")
img2 = cv2.imread("data/2-b.png")

# Convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and descriptors
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)


"""


class SIFTExtractor:
    def __init__(self):
        pass

    def extract(self, image):
        pass
