""""Module to extract template from the deep model"""
import numpy as np
import cv2


class TemplateExtractor:
    """"Class to extract template data from face images"""

    def __init__(self):
        """
        Implement custom initialization here
        """
        self.template_shape = 512
        self.model_path = ""
        self.image_width = 224
        self.image_height = 224
        self.image_channels = 3


    @staticmethod
    def compare(reference, probe):
        """
            Method to compare 2 feature templates. Dot product by default.
            Input - 2 numpy arrays.
            Returns normalised similarity value float: 0 - nonmatch, 1 - match
        """

        dot_product = np.dot(probe.flatten(), reference.flatten())
        dot_product_normalized = dot_product / np.linalg.norm(probe.flatten()) / np.linalg.norm(reference.flatten())
        return dot_product_normalized


    def extract(self, image_path):
        """
            Method to extract feature template from image path. Implement custom logic here.
            Input - str path to the image.
            Returns numpy array.
        """
       
        #read image and extract template
        img = cv2.imread(image_path)

        # Placeholder random array generation
        template = np.random.rand(self.template_shape)
        template = template / np.linalg.norm(template)
        return template