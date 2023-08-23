#!/bin/bash

# cd to the correct directory
cd /home/pi/Documents/UoB-GoS-Election-Data/

# run the script
python election_list.py

# check for updates
if [[ `git status --porcelain` ]]; then
    # changes found
    git add .
    git commit -m "update election data"
    git push
else
    # no changes found, do nothing
    echo "No changes found..."
fi
