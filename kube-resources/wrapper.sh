#!/bin/bash

function check_status(){
    if [ $? -ne 0 ]; then
        echo "ERROR: Last command failed."
    else
        echo "INFO: Last command completed."
    fi
}

echo "INFO: Updating repository"
apt-get update
check_status
echo "INFO: Installing Vim package"
apt-get install -y vim
check_status
echo "INFO: Installing pyhon3-pip package"
apt-get install -y python3-pip
check_status
echo "INFO: Installing dnsutils package"
apt-get install -y dnsutils
check_status
echo "INFO: Installing curl package"
apt-get install -y curl
check_status
echo "INFO: Installing Kubernetes package of Python"
pip3 install kubernetes
check_status 
echo "INFO: Sleeping to keep container alive"
echo "PS1=\"[\u@\h \w]\$ \"" >> ~/.bashrc
touch /ready.txt
while true
do 
    sleep 10;
done
