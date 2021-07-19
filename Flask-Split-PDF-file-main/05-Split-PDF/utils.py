from flask import current_app
import os, secrets
from PyPDF2 import PdfFileWriter

def save_pdf(PDF):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(PDF.filename)
    pdf_fn = random_hex + f_ext
    pdf_path = os.path.join(current_app.root_path, 'static/OriginalFiles', pdf_fn)  
    PDF.save(pdf_path)   
    return random_hex
    
def create_folder(name):
    basedir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(basedir, 'static/SplitDocument/'+str(name))
    os.makedirs(path) 
     
def split_pdf(pdf,random_hex):
    File="static/SplitDocument/"+random_hex+"/Page"
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output = f'{File}{page+1}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)