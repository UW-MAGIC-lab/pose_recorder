#!/usr/bin/env python

# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.01.26

import time
import PIL.Image
import threading
import cv2
from mediapipe import solutions
import numpy as np
mp_drawing = solutions.drawing_utils
mp_holistic = solutions.holistic

"""TODO: add docstring"""

class VideoCapture():

  def __init__(self, width=None, height=None, fps=None):
    """TODO: add docstring"""

    self.width = width
    self.height = height
    self.fps = fps

    self.running = False

    # Open the video source
    self.vid = cv2.VideoCapture(0)
    self.holistic = mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5)
    if not self.vid.isOpened():
        raise ValueError("[MyVideoCapture] Unable to open video source", video_source)

    # Get video source width and height
    if not self.width:
        # convert float to int
        self.width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    if not self.height:
        # convert float to int
        self.height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if not self.fps:
        # convert float to int
        self.fps = int(self.vid.get(cv2.CAP_PROP_FPS))

    # default value at start
    self.ret = False
    self.frame = None
    self.results = None

    self.convert_color = cv2.COLOR_BGR2RGB
    #self.convert_color = cv2.COLOR_BGR2GRAY
    self.convert_pillow = True

    # start thread
    self.running = True
    self.thread = threading.Thread(target=self.process)
    self.thread.daemon = True
    self.thread.start()


  def process(self):
    """TODO: add docstring"""

    while self.running:
      ret, frame = self.vid.read()
      self.start = time.time()
      if ret:
        # process image
        frame = cv2.resize(frame, (self.width, self.height))

        if self.convert_pillow:
          frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
          frame.flags.writeable = False
          results = self.holistic.process(frame)

          # Draw landmark annotation on the frame.
          frame.flags.writeable = True
          # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
          mp_drawing.draw_landmarks(
              frame, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
          mp_drawing.draw_landmarks(
              frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
          mp_drawing.draw_landmarks(
              frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
          mp_drawing.draw_landmarks(
              frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
          frame = PIL.Image.fromarray(frame)
      else:
        print('[MyVideoCapture] stream end:', self.video_source)
        break

      # assign new frame
      self.ret = ret
      self.frame = frame
      self.results = results

      # sleep for next frame
      time.sleep(1/self.fps)

  def get_frame(self):
    """TODO: add docstring"""
    return self.ret, self.frame
