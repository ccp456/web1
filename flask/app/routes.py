from app import app
from flask import render_template,url_for,make_response,Request,Response

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return("hello world")




@app.route('/test')
def test():
    return render_template('test.html')