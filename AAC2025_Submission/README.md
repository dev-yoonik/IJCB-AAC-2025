# How it works:

This document details how the submission template works and how it should be used. 

The template is setup with three main folders: 
- `docker_template`: The code itself.
- `results`: Location of extracted results.
- `test_images`: Location of testing set in the same format as the final testing set.

## Docker template

The evaluation process will be conducted using Docker. Participants are invited to submit their implementations as Docker containers. The provided container should encapsulate their approach, ensuring reproducibility and consistency across all submissions.


### Quick start guide

How to quickly test your solution:

#### Step 1 - Docker install
First install Docker: Follow the installation guide [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)
For Windows users, please use WSL in the following steps and enable docker inside WSL.

#### Step 2 - Verify installation and Submission Template
 Run `full_test_resilience.sh` and `full_test_detection.sh`  which for now just run placeholder logic. You can alternativelly run `launch_container.sh` to launch and test the container.

```console
cd AAC2025_Submission/docker_template
sudo ./full_test_resilience.sh
sudo ./full_test_detection.sh
```


#### Step 3 - Implement your submission

##### 3.1 - Rename the folder *docker_template* according to your submission name.
The folder shall be named as {participant}_{sequence} , where participant is a single word, non-infringing name of the particiant; sequence: a single digit decimal identifier to start at 0 and incremented by 1 for each new submission. 


##### 3.2 - Implement your solution's logic for your submission

 *Image alignment is already handled in our testing data, so no additional alignment operations are required.*
 
**For the detection track**

Here, developers primarily need to implement functionality for:
 
- Model inference (extract) – extracting classification score (float) and decision (boolean).

These implementations should be added in `classifier.py`, along with a corresponding dependencies added to the requirements.txt file.

**For the resilience track**

Here, developers primarily need to implement functionality for:
 
- Model inference (extract) – extracting biometric templates.
- Template comparison (compare) – computing similarity between extracted templates.

These implementations should be added in `template_extractor.py`, along with a corresponding dependencies added to the requirements.txt file.

#### Step 4 - Test your solution

Using the provided scripts the test images in the `AAC2025_Submission/test_images` folder are evaluated. Each track has its corresponding protocol text file. The format of the final testing set will be similar to the one provided (with more images of course). After running the provided scripts, the results should be saved in the `AAC2025_Submission/results` folder.

**For the detection track**

To verify that the container functions correctly, run the attached `full_test_detection.sh` script. This script will:
- Build the Docker image.
- Run the container.
- Execute adversarial classification for the provided images using `run_detection_track.py`
- Remove the container and delete the image.

```console
sudo ./full_test_detection.sh
```

**For the resilience track**

To verify that the container functions correctly, run the attached `full_test_resilience.sh` script. This script will:
- Build the Docker image.
- Run the container.
- Execute a comparison test for the pairs of provided images using `run_resilience_track.py`
- Remove the container and delete the image.

```console
sudo ./full_test_resilience.sh
```

#### Step 5 - Submission Files
The content of  `AAC2025_Submission/{submission_name}` is your submission to be sent to the organizers. Please archive the folder {submission_name} and send it according to the submission instructions on the challenge website.

That's it! 

For any further clarifications, please refer to the provided documentation or reach out to the organizers.


