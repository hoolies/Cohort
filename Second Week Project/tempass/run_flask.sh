#!/usr/bin/env python3


ls

echo "Enter the file that you want flask to run: "

read

export FLASK_APP=$REPLY
flask run
