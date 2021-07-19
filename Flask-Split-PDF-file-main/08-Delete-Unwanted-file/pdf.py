from flask import Flask, render_template, current_app, flash
from forms import PDFForm
from utils import save_pdf, create_folder, split_pdf, create_zip
from PyPDF2 import PdfFileReader
import os, shutil

app=Flask(__name__)
app.config['SECRET_KEY'] = '123456789'


@app.route('/', methods=['POST', 'GET'])
def pdf():
    form = PDFForm()
    if form.validate_on_submit():
        file_name = form.PDF.data.filename
        random_hex = save_pdf(form.PDF.data)
        create_folder(random_hex)
        PDF_path = os.path.join(current_app.root_path, 'static/OriginalFiles', random_hex+'.pdf')
        pdf = PdfFileReader(PDF_path)
        split_pdf(pdf,random_hex)
        create_zip(random_hex)
        
        PDF_Delete_path = os.path.join(current_app.root_path, 'static/SplitDocument', random_hex)
        shutil.rmtree(PDF_Delete_path)
        
        flash('File Created successfully', 'success')
        return render_template('download.html', zip_path=random_hex)   
    return render_template('home_pdf.html', form=form)

@app.route('/download/<id>')
def download_again(id):
    return render_template('download.html', zip_path=id)


if __name__=='__main__':
    app.run(debug='True')
