#!/bin/bash

# Get the name of the current directory (where the script is run)
export submission_name=$(basename $PWD)
export submission_name_container=$submission_name"_container"
export PORT_N_D=7007
export PORT_N_M=7007

# Define mount paths
export code_dir=$PWD
export images_dir=$(dirname $PWD)/test_images
export results_dir=$(dirname $PWD)/results

export dk_code_mnt=/mnt/code
export dk_images_mnt=/mnt/test_images
export dk_results_mnt=/mnt/results
export dk_save_mnt="$dk_results_mnt/$submission_name"

echo "Building Docker Image"
sudo docker build --build-arg PORT_NUMBER=$PORT_N_D -t $submission_name .

echo "Running Docker Container"
sudo docker run -d \
  --cpus="4" \
  -v "$code_dir:$dk_code_mnt" \
  -v "$images_dir:$dk_images_mnt" \
  -v "$results_dir:$dk_results_mnt" \
  --name "$submission_name_container" \
  -p "$PORT_N_D:$PORT_N_M" \
  "$submission_name"

echo "Wait few seconds"
sleep 5s

echo "Check Container is running"
sudo docker ps

echo "Creating submission save folder"
sudo docker exec -it "$submission_name_container" mkdir -p "$dk_save_mnt"

echo "Adding images and save path to docker environment and running script"
sudo docker exec -it -e images_dir="$dk_images_mnt" -e save_dir="$dk_save_mnt" "$submission_name_container" python3 ./run_resilence_track.py


echo "Deleting Container"
sudo docker remove --force $submission_name_container

echo "Deleting image"
sudo docker rmi $submission_name