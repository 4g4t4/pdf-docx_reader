from PyPDF2 import PdfReader
from docx import Document
from gtts import gTTS
import interface

# Funkcja do czytania pliku PDF
def read_pdf(file_path):
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        # Pobierz tekst z wszystkich stron
        pdf_text = ""
        for page in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page].extract_text()
        tts = gTTS(pdf_text, lang='en')
        tts.save("pdf_audio.mp3")
        return pdf_text

# Funkcja do czytania pliku docx
def read_docx(file_path):
    docx_document = Document(file_path)

    # Pobierz tekst z wszystkich paragrafów
    docx_text = ""
    for para in docx_document.paragraphs:
        docx_text += para.text
    tts = gTTS(docx_text, lang='en')
    tts.save("docx_audio.mp3")
    return docx_text
