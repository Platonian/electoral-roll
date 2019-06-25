# -*- coding: utf-8 -*-
import argparse
import io
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

file1 = 'file-1.jpg'
file2 = 'file2.jpg'
output_ext = '.txt'


# [START vision_fulltext_detection]
def extract_text_from_doc(path):
    base_name = os.path.basename(path)
    file_name = os.path.splitext(base_name)[0]
    print(file_name+': ...')
    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_document_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:

            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    temp = open('temp1'+file_name+output_ext, 'a+')
                    if (word_text == "Photo"):
                        temp.write("")
                    elif (word_text == "is"):
                        temp.write("")
                    elif (word_text == "Available"):
                        temp.write("")
                    elif (word_text == "DELETED"):
                        temp.write("")
                    elif (word_text == "LETED"):
                        temp.write("")
                    elif (word_text == "|"):
                        temp.write("")
                    elif (word_text.find("UP") != -1):
                        temp.write("\n")
                        temp.write(word_text)
                    elif (word_text.find('ABG') != -1):
                        temp.write("\n")
                        temp.write(word_text)
                        temp.write("\n")
                    elif (word_text.find('HND') != -1):
                        temp.write("\n")
                        temp.write(word_text)
                        temp.write("\n")
                    elif(word_text == 'पुरुष'):
                        temp.write("पुरुष\n")
                    elif(word_text == 'महिला'):
                        temp.write("महिला\n")
                    else:
                        temp.write(" ")
                        temp.write(word_text)
                    temp.close()
    with open('temp1'+file_name+output_ext, 'r+') as infile, \
            open('temp2'+file_name+output_ext, 'w+') as outfile:
        data = infile.read()
        data = data.replace("]", "")
        data = data.replace(' / ', '/')
        data = data.replace('\\', '')
        data = data.replace('ः', ':')
        data = data.replace(':', ' : ')
        data = data.replace('  ', ' ')
        data = data.replace('संख्या व नाम', 'संख्यावनाम')
        data = data.replace('का नाम', 'कानाम')
        data = data.replace(' नाम', '\nनाम')
        data = data.replace('कानाम', 'का नाम')
        data = data.replace('संख्यावनाम', 'संख्या व नाम')
        data = data.replace('लिग', 'लिंग')
        data = data.replace(' पति', ' : पति')
        data = data.replace(' पिता', ' : पिता')
        data = data.replace(' माता', ' : माता')
        data = data.replace(' मकान', ' : मकान')
        data = data.replace(' आयु', ' : आयु')
        data = data.replace(' लिंग', ' : लिंग')
        data = data.replace('  ', ' ')
        data = data.replace(' ।', '')
        outfile.write(data)

    with open('temp2'+file_name+output_ext, 'r') as infile, \
            open('output_'+file_name+output_ext, 'w+') as outfile:
        for line in infile:
            if line.startswith("नाम : "):
                outfile.write(line)
    os.remove('temp1'+file_name+output_ext)
    os.remove('temp2'+file_name+output_ext)
    # [END vision_python_migration_document_text_detection]
# [END vision_fulltext_detection]

extract_text_from_doc('file-1.jpg')
