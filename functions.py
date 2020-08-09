import numpy as np
import cv2
import pytesseract
import language_tool_python
from pytesseract import Output
import spacy
import matplotlib.pyplot as plt
from skimage import measure, morphology
from skimage.color import label2rgb
from skimage.measure import regionprops
from langdetect import detect_langs
from translate import Translator

## Load Models
#Spanish
spacy.load('es_core_news_lg')
nlp = spacy.load('es_core_news_lg')

#Englis Model
nlp = spacy.load('en_core_web_lg')

pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Program Files\Tesseract-OCR\tesseract.exe'
)

########################################### Process Img with OpenCv ###########################################

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)

# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


def prepareImg(img_path):
    image = cv2.imread(img_path)

    gray = get_grayscale(image)
    #thresh = thresholding(gray)

    return gray


#########################################  Main Project Functions  ####################################


def getTranslate(str,from_lang, to_lang):
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    split_chunks = []

    clean_str = str.split('\n')

    for i in range(len(clean_str)):
        split_chunks.append( translator.translate(clean_str[i]) )

    translation = " ".join(split_chunks)

    return translation


def spacyAnalizys(str):

    doc = nlp(str)
    for token in doc:
       print(token, token.lemma_)


def getText(img_path,lang):

    custom_config = r'--oem 3 --psm 6'

    image = prepareImg(img_path)

    text = pytesseract.image_to_string(image, config=custom_config, lang=lang)

    return text

def getLanguages(img_path):

    custom_config = r'-l eng --psm 6'

    image = prepareImg(img_path)

    txt = pytesseract.image_to_string(image['thresh'], config=custom_config)

    possible_lang = detect_langs(txt)

    return possible_lang

############################# Load Test Data ##################################

string = """Simple Sample
My Name
Jamuary 6, 2017

1 Hello World!
Hello World! Today Iam leaming IATEX. ISTEX is a great program for writing
math. I can write in line math such as a? | 6? =e? . I can also give equations
their own space:

PtP =u? a
I I do not leave any blank lines BTEX will continue this text without making
it into a new paragraph. Notice how there was no indentation in the text after
equation (1). Also notice how oven though I hit enter after that sentence and
here | BTEX formats the sentence withont any break. Also look how it doesn’t
matter how many spaces I put betwoen my words."""

