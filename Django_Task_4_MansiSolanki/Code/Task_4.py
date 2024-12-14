
import os
from docx import Document
from reportlab.pdfgen import canvas

def convert_docx_to_pdf(docx_path, pdf_path):
    if not os.path.exists(docx_path):
        print(f"Error: File not found at {docx_path}")
        return

    doc = Document(docx_path)
    c = canvas.Canvas(pdf_path)

    y_position = 800  
    for paragraph in doc.paragraphs:
        if y_position < 50:  
            c.showPage()
            y_position = 800
        c.drawString(100, y_position, paragraph.text)
        y_position -= 20

    c.save()
    print(f"PDF created at {pdf_path}")


convert_docx_to_pdf(r"C:/Users/mohin/Desktop/Brainybeam Tasks/Task 4/Code/Day2 bda.docx", r"C:/Users/mohin/Desktop/Brainybeam Tasks/Task 4/Day2 bda.pdf")
