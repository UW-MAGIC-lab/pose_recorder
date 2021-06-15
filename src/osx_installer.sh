#!/bin/bash

pipenv run pyinstaller --debug=all main.py --noconfirm
echo "copying dependencies"
cp -r modules dist/main/mediapipe
