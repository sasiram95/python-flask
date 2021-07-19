from flask import Flask, render_template
from forms import PDFForm


app=Flask(__name__)
app.config['SECRET_KEY'] = '123456789'


@app.route('/', methods=['POST', 'GET'])
def pdf():
    form = PDFForm()
    if form.validate_on_submit():
        file_name = form.PDF.data.filename
        return render_template('download.html',file = file_name)   
    return render_template('home_pdf.html', form=form)

if __name__=='__main__':
    app.run(debug='True')
