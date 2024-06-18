import torch
import helper

detected_img_path = 'runs/detect/exp/'
max_object_detection = 2
confidence_threshold = 0.25
image_size = 640

def detect_label(image):
  helper.clear_dir(detected_img_path)
  try:
    model = torch.hub.load('', 'custom', path='runs/train/exp3/weights/best.pt', source='local', force_reload=True)
    model.conf = confidence_threshold
    model.max_det = max_object_detection
    result = model(image, size=image_size)
    result.save()
    return result.pandas().xyxy[0]
  except:
    return 'Data label could not be done, please try again'