from flask import Flask, render_template
import secrets

app=Flask(__name__)


pdf_books=[
    {"si_no":"1","id":secrets.token_hex(8),"book_name":"Thirukural","Author":"Thiruvalluvar","price":300},
    {"si_no":"2","id":secrets.token_hex(8),"book_name":"Aathichudi","Author":"Avviyar","price":200},
    {"si_no":"3","id":secrets.token_hex(8),"book_name":"Bharathiyar Kavithaigal","Author":"Subramania Bharati","price":900},
    {"si_no":"4","id":secrets.token_hex(8),"book_name":"Pandiyan Parisu","Author":"Bharathidasan","price":800}]


@app.route('/')
def pdf():
    return render_template('home_pdf.html',books=pdf_books)

if __name__=='__main__':
    app.run(debug='True')
