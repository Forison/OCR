import pytesseract as pt
import preprocessor

def ocr_label(image):
  try:
    label = "caption" if "caption" in image else "marker"
    caption_or_image = pt.image_to_string(preprocessor.process(image)) if "caption" in image else image
    print(caption_or_image)
    result = { f"{label}": caption_or_image }
    return result
  except:
    return 'image could not be converted to text'
