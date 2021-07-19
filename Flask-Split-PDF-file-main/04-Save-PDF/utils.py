from flask import current_app
import os, secrets

def save_pdf(PDF):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(PDF.filename)
    pdf_fn = random_hex + f_ext
    pdf_path = os.path.join(current_app.root_path, 'static/', pdf_fn)  
    PDF.save(pdf_path)   
    return random_hex