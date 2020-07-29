"""
.. module:: working_with_pdf_and_word.create_word_file
   :synopsis: Create word file with different font style, attributes, etc.
"""
from working_with_pdf_and_word.read_word_file import create_doc


def restyle_doc():
    doc = create_doc()
    doc.paragraphs[0].style = "Normal"
    doc.paragraphs[1].runs[0].style = "QuoteChar"
    doc.paragraphs[1].runs[1].underline = True
    doc.paragraphs[1].runs[3].underline = True
    doc.save("pdf_word_files/restyled.docx")



if __name__ == "__main__":
    restyle_doc()
