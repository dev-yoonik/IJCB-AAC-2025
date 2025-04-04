#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import uvicorn
from fastapi import FastAPI
import numpy as np
import cv2
import json
import time

from template_extractor import TemplateExtractor
from classifier import Classifier

extractor = TemplateExtractor()
classifier_obj = Classifier()

app = FastAPI()


@app.get("/resilience/extract_template")
async def template_extraction(image_path: str = ""):
    """ Extract Biometric Template Endpoint. """

    template_data = extractor.extract(image_path = image_path)

    extracted_template = template_data.tolist()
    report = {
            'data': extracted_template,
            }
    return report


@app.get("/resilience/compare_templates")
async def compare_two_templates_endpoint(template_1: str = "",template_2: str = ""):
    """ Compare 2 feature templates """

    try:
        bin_data_1 = json.loads(template_1)
        bin_data_2 = json.loads(template_2)
        
        #checking the templates size match
        if len(bin_data_1) != len(bin_data_2):
            similarity_report = {
                'similarity': "ERROR",
                'comment': "Templates size mismatch"}
            return similarity_report

        bin_array_1 = np.array([float(x) for x in bin_data_1])
        bin_array_2 = np.array([float(x) for x in bin_data_2])

        similarity = extractor.compare(bin_array_1, bin_array_2)

        #output result
        similarity_report = {
                'similarity': similarity,
                'comment':'OK'}

    except Exception as e:
        print("Error while processing templates ")
        similarity_report = {
                'similarity': "ERROR",
                'comment': f"Error: {e}"}
    
    return similarity_report


@app.get("/resilience/compare_images")
async def compare_two_images_endpoint(image_path_1: str = "", image_path_2: str = ""):
    """ Compare 2 Images by their filenames."""

    try:
        #extract templates
        template_1 = extractor.extract(image_path = image_path_1)
        template_2 = extractor.extract(image_path = image_path_2)

        #compute similarity
        similarity = extractor.compare(template_1, template_2)

        #output result
        similarity_report = {
                'image_path_1': image_path_1,
                'image_path_2': image_path_2,
                'similarity': similarity,
                'comment':'OK'}

    except Exception as e:
        print("Error while comparing ", image_path_1 ," and ", image_path_2)
        similarity_report = {
                'image_path_1': image_path_1,
                'image_path_2': image_path_2,
                'similarity': "ERROR",
                'comment': f"Error: {e}"}

    return similarity_report

@app.get("/detection/detect")
async def classify_image(image_path: str = ""):
    """ Extract Adversarial Decision Endpoint. """

    try:
        score, decision = classifier_obj.extract(image_path=image_path)
        report = {
            'image_path': image_path,
            'score': score,
            'decision': decision,
            'comment': 'OK'
        }

    except Exception as e:
        print("Error during classification:", e)
        report = {
            'image_path': image_path,
            'score': "ERROR",
            'decision': "ERROR",
            'comment': f"Error: {e}"
        }
    return report


if __name__ == '__main__':

    #to execute app in console
    uvicorn.run("main:app",
                host='0.0.0.0',
                port=7007)
