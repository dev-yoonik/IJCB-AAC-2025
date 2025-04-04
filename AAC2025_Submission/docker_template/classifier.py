""""Module to extract classification probability from the deep model"""
import numpy as np
import cv2


class Classifier:
    """"Class to extract template data from face images"""

    def __init__(self):
        """
        Implement custom initialization here
        """
        self.model_path = ""
        self.image_width = 224
        self.image_height = 224
        self.image_channels = 3


    def extract(self, image_path):
        """
            Method to extract feature template from image path. Implement custom logic here.
            Input - str path to the image.
            Returns score float, decision bool: True(1) - Presentation Attack ; False(0) - Bona Fide Presentation.
        """

        # read image and extract template
        img = cv2.imread(image_path)

        # random placeholder array generation
        score = np.random.rand(1).item()
        decision = score > 0.5
        return score, decision