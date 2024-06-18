import cv2
import pandas as pd
import detect

caption_key = 0

def extract_label(image_path):
  image = cv2.imread(image_path)
  df = pd.DataFrame(detect.detect_label(image_path))
  labels = []
  for index, row in df.iterrows():
    x_min = int(row['xmin'])
    y_min = int(row['ymin'])
    x_max = int(row['xmax'])
    y_max = int(row['ymax'])
    class_name = 'caption' if row['class'] == caption_key else 'marker'

    cropped_img = image[y_min:y_max, x_min:x_max]
    crop_path = f'runs/crop/exp/{class_name}_{index}.png'
    labels.append(crop_path)
    cv2.imwrite(crop_path, cropped_img)
  
  return labels