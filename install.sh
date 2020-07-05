#!/bin/bash

# Verify as root
if [[ $EUID -ne 0 ]]; then
	echo "This script most be run as root" 1>&2
	exit 1
fi 

apt-get install scrot -y
apt-get install python3-tk -y
apt-get install python3-dev -y
pip3 install requirements.txt
python3 -m pip install pyautogui