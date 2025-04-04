#!/bin/bash

#submission name is the name of current folder 
export submission_name=$(basename $PWD)
export submission_name_container=$submission_name"_container"
export PORT_N_D=7007
export PORT_N_M=7007

#mounting the pwd container directory 
export dk_mnt=/mnt/images

echo "Building Docker Image"
sudo docker build --build-arg PORT_NUMBER=$PORT_N_D -t $submission_name .

echo "Running Docker Container"
sudo docker run -d -v $PWD:$dk_mnt --name $submission_name_container -p $PORT_N_D:$PORT_N_M $submission_name

echo "Wait few seconds"
sleep 1s 

echo "Check Container is running"
sudo docker ps

echo "Deleting Container"
sudo docker remove --force $submission_name_container

echo "Deleting image"
sudo docker rmi $submission_name