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
    for landmark_id in mp_holistic.PoseLandmark._member_names_:
      landmark = results.pose_landmarks.landmark[mp_holistic.PoseLandmark[landmark_id]]
      landmark_x, landmark_y, landmark_z = [None, None, None]
      if landmark.visibility > 0.6:
        landmark_x = landmark.x
        landmark_y = landmark.y
        landmark_z = landmark.z
      csv_data[f'{landmark_id}_x'.lower()] = landmark_x
      csv_data[f'{landmark_id}_y'.lower()] = landmark_y
      csv_data[f'{landmark_id}_z'.lower()] = landmark_z

    for landmark_id in mp_holistic.HandLandmark._member_names_:
      l_x, l_y, l_z, r_x, r_y, r_z = [None, None, None, None, None, None]
      if results.left_hand_landmarks:
        lh_landmark = results.left_hand_landmarks.landmark[mp_holistic.HandLandmark[landmark_id]]
        if lh_landmark.visibility > 0.6:
          l_x = lh_landmark.x
          l_y = lh_landmark.y
          l_z = lh_landmark.z
      if results.right_hand_landmarks:
        rh_landmark = results.right_hand_landmarks.landmark[mp_holistic.HandLandmark[landmark_id]]
        if rh_landmark.visibility > 0.6:
          r_x = rh_landmark.x
          r_y = rh_landmark.y
          r_z = rh_landmark.z
      csv_data[f'L_{landmark_id}_x'.lower()] = l_x
      csv_data[f'L_{landmark_id}_y'.lower()] = l_y
      csv_data[f'L_{landmark_id}_z'.lower()] = l_z
      csv_data[f'R_{landmark_id}_x'.lower()] = r_x
      csv_data[f'R_{landmark_id}_y'.lower()] = r_y
      csv_data[f'R_{landmark_id}_z'.lower()] = r_z

    csv_data['timestamp'.lower()] = f'{datetime.now(timezone.utc)}'
    return csv_data

  def __del__(self):
    """TODO: add docstring"""
    if self.file:
      self.file.close()
