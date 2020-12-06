"""
tests for CV parsing: PDF, Word and Images.
run:
./manage.py test apps.cv.tests.TestUtils
"""
import os
from django.conf import settings
from unittest import TestCase
from .utils import extract_text_from_file

absolute_path = os.path.join(settings.BASE_DIR, 'media', 'CVs')


class TestUtils(TestCase):

    def test_pdf_parser(self):
        text = extract_text_from_file(os.path.join(absolute_path, 'cv6.pdf'))
        self.assertTrue(text)
        self.assertIsInstance(text, str)

    def test_word_parser(self):
        text = extract_text_from_file(os.path.join(absolute_path, 'cv11.docx'))
        self.assertTrue(text)
        self.assertIsInstance(text, str)

    def test_png_parser(self):
        text = extract_text_from_file(os.path.join(absolute_path, 'cv5.png'))
        self.assertTrue(text)
        self.assertIsInstance(text, str)

    def test_jpg_parser(self):
        text = extract_text_from_file(os.path.join(absolute_path, 'cv4.jpg'))
        self.assertTrue(text)
        self.assertIsInstance(text, str)
