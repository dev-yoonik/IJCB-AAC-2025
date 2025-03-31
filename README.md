![logo](https://www.youverse.id/storage/images/challenge/challenge.jpg)

## **1. Introduction**

Welcome to the 2025 Adversarial Attack Challenge for Secure Face Recognition. This challenge is designed to advance research in adversarial robustness and real-world security applications by testing models in two distinct tracks:

- **Detection Track:** Identify whether a face image is adversarial or clean.
- **Resilience Track:** Train a robust face recognition model that maintains high accuracy even under adversarial attacks.

For full details, please visit our [challenge website](https://www.youverse.id/adversarial). This document outlines participation instructions, dataset access, submission guidelines, evaluation metrics, and other essential information. Additionally, a GitHub repository with an adversarial attack package for face recognition is available to support your development efforts.

---

## **2. Challenge Tracks and Objectives**

### **2.1 Detection Track**

- **Objective:** Develop a model that accurately classifies face images as either “clean” or “adversarial.”
- **Dataset Composition:** Contains a mix of clean images and adversarially modified images, generated with varying perturbation levels and attack types.
- **Evaluation Metrics:**
    - **APCER (Attack Presentation Classification Error Rate):** Measures how often adversarial images are incorrectly accepted as clean.
    - **BPCER (Bona Fide Presentation Classification Error Rate):** Measures how often clean images are mistakenly classified as adversarial.
    - **F1-score:** Balances precision and recall to assess overall detection accuracy.
    - **AUC-ROC:** Evaluates the model’s ability to distinguish between adversarial and clean images across varying thresholds.

### **2.2 Resilience Track**

- **Objective:** Train a face recognition model that remains robust under adversarial attacks.
- **Dataset Composition:** Contains both clean images and adversarially altered face images, including various types of attack modifications.
- **Evaluation Metrics:**
    - **FMR (False Match Rate):** The probability that an imposter is incorrectly accepted.
    - **FNMR (False Non-Match Rate):** The probability that a genuine user is wrongly rejected.
    - **Attack Success Rate (ASR):** The proportion of adversarial inputs that successfully cause misclassification.
    - **Robustness Score:** A custom metric that measures the model’s overall ability to resist adversarial modifications (detailed computation available on the challenge website).

---

## **3. Datasets and Resources**

### **3.1 Dataset Composition**

- **Training Dataset:** Based on CelebA, composed of 50% clean images, 25% evasion attacks, and 25% impersonation attacks.
- **Validation Dataset:** A combination of CelebA and LFW, following the same 50/25/25 split.
- **Test Dataset:** A private dataset featuring unseen samples and potentially novel attacks.

The provided datasets—_adversarial versions of CelebA and LFW_—include 10 distinct attack types per dataset. Each dataset is accompanied by information files detailing the applied modifications.

- **Only the provided datasets should be used for model development. We want participants to use only the provided data (can be augmented as desired). Since we also provide the attack package this would benefit participants with more resources to just increase the data size as desired which would go against the challenge goals.**
- **If usage of external data is suspected the participants may be removed from the challenge.**

### **3.2 Data Access and Restrictions**

- The data will be made available via a link provided to all registered participants.
- **Due to licensing constraints, datasets cannot be redistributed.**

### **3.3 Pretrained Models** ###

- The usage of pretrained models is allowed for both tracks.
- These models can be general purpose classification models of face recognition models, e.g. found in `timm`, `torchvison`or `insightface` packages for example.


### **3.4 Data Augmentation**

- Any kind of data augmentation is allowed as long as it is explained in the submission and reproducible. 

---

## **4. Adversarial Attack Package**

To further support your development, we have published and continue to maintain an adversarial attack package for face recognition. This package is available on our GitHub repository: [GitHub Attack Package](https://github.com/dev-yoonik/youverse-adversarial-attacks). Please refer to the repository for code examples, usage instructions, and additional resources.

---

## **5. Submission Guidelines**

### **5.1 Submission Format**

- Participants must submit their implementations as **Docker containers**.
- A **template Docker container** will be provided to guide you through the submission process.
- Ensure that your Docker container includes all necessary dependencies (e.g., specific versions of deep learning frameworks) and follows the provided template structure.

### **5.2 Submission Process**

- Submit your Docker container via the official challenge portal (details available on the challenge website).
- All submissions will be executed on our private hardware using the private testing data.

### **5.3 Runtime Constraints**

- **Inference time must not exceed 1 second per image** when running on a **single-core CPU**.
- The CPU that will be used for inference is a  Intel Core i9-13900 2 GHz/5.6 GHz. For reference, the inference process using a Resnet50 onnx classification model takes around 0.05 seconds per image.

### **5.4 Submission eligibility**

- All submissions must include a report detailing the methodology.
- The solutions presented need to be open-sourced to be eligible for the monetary prizes and paper co-authoring.

---

## **6. Evaluation Protocol**

- **Final Track Rankings:** Rankings will be determined by an aggregated score that combines all evaluation metrics. Specific weighting details for each metric are available on the challenge website.
- **Recognition:** The top 3 teams in each track will be invited to co-author a competition summary paper at IJCB 2025.

---

## **7. Monetary Prizes**

- Monetary prizes up to **$3,500** are available. Further details on prize distribution (e.g., breakdown by track and award level) will be provided on the challenge website.

---

## **8. Ethical and Legal Considerations**

- The CelebA and LFW datasets are provided for research purposes only. Redistribution is strictly prohibited.
- Participants are encouraged to consider fairness, potential dataset biases, and ethical implications in their research and submissions.

---

## **9. Timeline and Important Dates**

- March 17, 2025 - Github instructions release.
- March 17, 2025 - Dataset release.
- May 31, 2025 - Deadline for Algorithm evaluation on platform.
- June 10, 2025 - Announcement of the results to participants.
- June 23, 2025 - Submission of summary papers.
- July 23, 2025 - Camera-ready papers.
- September 8-11, 2025 - IJCB conference.

For any updates or additional details, please regularly check the challenge website.

---

## **10. Contact and Support**

- For questions or further assistance, please contact us at [adversarial@youverse.id](mailto:adversarial@youverse.id).

![logo](https://yk-website-images.s3.eu-west-1.amazonaws.com/LogoV4_TRANSPARENT.png?)

![logo](https://www.youverse.id/storage/images/challenge/isr.jpeg)
---

We look forward to your participation and your contributions to advancing the field of adversarial attack detection and robust face recognition!

---
## **FAQ**
