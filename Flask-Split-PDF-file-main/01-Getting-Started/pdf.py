from flask import Flask

app=Flask(__name__)

@app.route('/')
def pdf():
    return "<center><h1>hello world</h1></center>"

if __name__=='__main__':
    app.run(debug='True')
