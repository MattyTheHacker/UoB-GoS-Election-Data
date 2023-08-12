#!/bin/bash

# cd to the correct directory
cd /home/pi/Documents/UoB-GoS-Election-Data/

# run the script
python election_list.py

# add all files to git
git add --all

# commit any changes
git commit -m "update"

# push to github
git push
