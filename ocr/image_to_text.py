import pytesseract
from PIL import Image
import os


def write_file(str_title, str_content):
    os.makedirs('result', exist_ok=True)
    with open('result/'+str_title+'.txt', 'a') as f:
        f.write(str_content+'\n')


# get file list
def getallFiles(file_dir):
    b = []
    for root, dirs, files in os.walk(file_dir):
        a = files
    for file in a:
        print(file_dir + file)
        b.append(file_dir + file)
    return b


def imageToText(imageName, lang):
    return pytesseract.image_to_string(Image.open(imageName), lang=lang)


if __name__ == "__main__":
    base_dir = 'E:/www/magicpython/ocr/images/'
    fileList = getallFiles(base_dir)
    for f in fileList:
        image_text = imageToText(f, 'chi_sim')
        write_file('result', image_text)
