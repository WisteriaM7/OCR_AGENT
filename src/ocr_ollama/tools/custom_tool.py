import easyocr

def extract_text_from_image(image_path: str) -> str:
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)
