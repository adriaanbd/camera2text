- IDLE
    -  PyCharm

- Python version
    - Python 3.8.3rc1

- Libraries
	- pip install opencv-python
	- pip install pytesseract
	- pip install spacy
	- pip install scikit-image
	- pip install matplotlib
	- pip install pdf2image
	- pip install langdetect
	- pip install translate

- Download Poppler
    - link http://blog.alivate.com.au/poppler-windows/
    - Move file to C:\Program Files
    - Add Path to enviroment variable
        -> C:\Program Files\poppler-0.68.0\bin

- Download tesseract
    - Link : http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe
    - Add Path to enviroment variable
        -> C:\Program Files\Tesseract-OCR
    - Run .exe File

- Download Spanish Model tesseract
    - https://github.com/tesseract-ocr/tessdata_best/blob/master/spa.traineddata
    - Move File to C:\Program Files\Tesseract-OCR\tessdata
    -  Verify spanish model instalation
        -> tesseract --list-langs

- Download Spanish Spanish Model
    - python -m spacy download es_core_news_lg

- Load Spacy Spanish Model
    - spacy.load('es_core_news_lg')


