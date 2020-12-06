import os
from typing import Any
# from typing import Dict
import pytesseract
from PIL import Image
import PyPDF2
import fitz
import docx
# from resume_parser import resumeparse
# from .install_deps import nlp
import textract


def get_file_extension(file: Any) -> str:
    """return file extension"""
    if isinstance(file, str):
        st = file
    else:
        st = file.name
    file_extension = os.path.splitext(st)[1]
    return str(file_extension[1:]).lower()


def convert_doc_to_text(doc_file: str) -> str:
    """
    convert Word file to text
    """
    doc = docx.Document(doc_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


def convert_pdf_to_text(pdf_file: str) -> str:
    """
    convert PDF file to text
    """
    with fitz.open(pdf_file) as f:
        full_text = []
        for page in f:
            full_text.append(page.getText())
        return '\n'.join(full_text)


def convert_pdf_to_text_v2(pdf_file: str) -> str:
    """
    convert PDF file to text
    """
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        full_text = []
        for pageNum in range(pdf_reader.numPages):
            full_text.append(pdf_reader.getPage(pageNum).extractText())
        return '\n'.join(full_text)


def convert_image_to_text(image_file: str) -> str:
    """
    convert DOC file to text
    """
    res = pytesseract.image_to_string(Image.open(image_file))
    return res


def convert_txt_to_text(txt_file: str) -> str:
    """
    convert TXT file to text
    """
    with open(txt_file, 'r') as f:
        return f.read()


def extract_text_from_file(filepath: str) -> str:
    """convert a PDF, Word or text file to String"""
    try:
        text = textract.process(filepath)
        return text.decode("utf8")
    except:
        return ""


def extract_text_from_file_v2(filepath: str) -> str:
    """convert a PDF, Word or text file to String"""
    try:
        extension = get_file_extension(filepath)
        if extension == 'txt':
            res = convert_txt_to_text(filepath)
        elif extension in ['docx', 'doc']:
            res = convert_doc_to_text(filepath)
        elif extension == 'pdf':
            res = convert_pdf_to_text(filepath)
        elif extension in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff']:
            res = convert_image_to_text(filepath)
        else:
            res = convert_txt_to_text(filepath)  # default to TXT
        return res
    except Exception as e:
        raise Exception(f"{filepath}: Can't extract text from file: {str(e)}")

# def parse_resume(filepath: str) -> Dict:
#     """Parse a PDF, Word or text file resume to semi-structured format"""
#     res = resumeparse.read_file(filepath)
#     return res
