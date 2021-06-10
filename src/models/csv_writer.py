from csv import DictWriter
from mediapipe import solutions
import os.path
from datetime import (datetime, timezone)
mp_holistic = solutions.holistic

class CSVWriter(object):
  def __init__(self, filename, image_height, image_width,fps):
    self.filename = filename
    self.file = None
    self.image_height = image_height
    self.image_width = image_width
    self.fps = fps
    self.writer = None

  def add(self, results):
    csv_dict = self.results_to_csv_dict(results)
    if self.writer:
      print("added to csv")
      self.writer.writerow(csv_dict)
    else:
      print("started csv")
      self.start_csv_document(csv_dict)
      self.writer.writerow(csv_dict)

  def start_csv_document(self, csv_dict):
    # write headers
    self.file = open(f'{self.filename}', 'w')
    keys = list(csv_dict.keys())
    writer = DictWriter(self.file, keys)
    writer.writeheader()
    self.file.close()
    # prepare document for writing data
    # change to append only mode to improve performance
    self.file = open(f'{self.filename}', 'a+')
    self.writer = DictWriter(self.file, keys)

  def results_to_csv_dict(self, results):
    csv_data = {
      'image_height': self.image_height,
      'image_width': self.image_width,
      'fps': self.fps
    }
    for landmark in mp_holistic.PoseLandmark._member_names_:
      x = results.pose_landmarks.landmark[mp_holistic.PoseLandmark[landmark]].x
      y = results.pose_landmarks.landmark[mp_holistic.PoseLandmark[landmark]].y
      csv_data[f'{landmark}_x'] = x
      csv_data[f'{landmark}_y'] = y

    for landmark in mp_holistic.HandLandmark._member_names_:
      if results.left_hand_landmarks:
        l_x = results.left_hand_landmarks.landmark[mp_holistic.HandLandmark[landmark]].x
        l_y = results.left_hand_landmarks.landmark[mp_holistic.HandLandmark[landmark]].y
      else:
        l_x = None
        l_y = None
      if results.right_hand_landmarks:
        r_x = results.right_hand_landmarks.landmark[mp_holistic.HandLandmark[landmark]].x
        r_y = results.right_hand_landmarks.landmark[mp_holistic.HandLandmark[landmark]].y
      else:
        r_x = None
        r_y = None
      csv_data[f'L_{landmark}_x'] = l_x
      csv_data[f'L_{landmark}_y'] = l_y
      csv_data[f'R_{landmark}_x'] = r_x
      csv_data[f'R_{landmark}_y'] = r_y

    csv_data['timestamp'] = f'{datetime.now(timezone.utc)}'
    return csv_data

  def __del__(self):
    """TODO: add docstring"""
    self.file.close()
