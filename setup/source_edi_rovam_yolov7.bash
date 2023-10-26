#!/bin/bash

# Sets up the edi_rovam_yolov7 environment for development.
#
# One recommendation is to make a bash function for this script in
# your ~/.bashrc file as follows:
#
# For non-ROS workflows:
#
#  edi_rovam_yolov7() {
#    source ~/workspace/learn_ws/src/edi_rovam_yolov7/setup/setup/source_edi_rovam_yolov7.bash
#  }
#
#  So you can then run this from your Terminal:
#    edi_rovam_yolov7
#

# User variables -- change this to meet your needs
export VIRTUALENV_FOLDER=~/python-virtualenvs/edi_rovam_yolov7
export YOLOV7_WS=~/workspace/learn_ws/src/edi_rovam_yolov7

if [ -n "$VIRTUAL_ENV" ]
then
    deactivate
fi

# Activate the Python virtual environment
source $VIRTUALENV_FOLDER/bin/activate
