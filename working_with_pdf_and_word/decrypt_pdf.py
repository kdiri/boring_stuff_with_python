"""
.. module:: working_with_pdf_and_word.decrypt_pdf
   :synopsis: Read encrypted pdf file and decrypt + read it.
"""

import os

from PyPDF2 import PdfFileReader
from dotenv import load_dotenv
from loguru import logger


def _is_encrypted(pdf_reader: PdfFileReader):
    return pdf_reader.isEncrypted


def _get_passwd():
    load_dotenv("envs/pass.env")
    return os.getenv("pdf_pass")


def _decrypt(pdf_reader: PdfFileReader, passwd: str):
    return pdf_reader.decrypt(passwd)


def read_pdf():
    with open("pdf_word_files/encrypted.pdf", "rb") as enc_file:
        pdf_reader = PdfFileReader(enc_file)
        if _is_encrypted(pdf_reader):
            passwd = _get_passwd()
            if _decrypt(pdf_reader, passwd):
                page = pdf_reader.getPage(0)
                logger.success(page.extractText())


if __name__ == "__main__":
    read_pdf()
