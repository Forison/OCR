# Algorithm
# Detect label
## use DL learning to detect the labels 

# Extract label
## Here we extract the marker and the caption from image by cropping them
# Store cropped image inside runs/crop/exp

# OCR labels cropped above
## Read the content of the extracted labels

import extract
import ocr

def main(image):
  try:
    labels = extract.extract_label(image)
    for label in labels:
      ocr.ocr_label(label)
    return 'You have successfull completed'
  except:
    return 'OCR was unsuccessful'
