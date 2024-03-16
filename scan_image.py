import pytesseract
import cv2

class TextExtractor:
    def __init__(self, left=450, top=390, right=540, bottom=430):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def extract_text_from_image(self, image_path, config, language):
        img = cv2.imread(image_path)
        cropped_img = img[self.top:self.bottom, self.left:self.right]
        gray_image = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
        extracted_text = pytesseract.image_to_string(image=cropped_img, config=config, lang=language)
        return extracted_text
