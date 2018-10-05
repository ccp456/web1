from app import app
from flask import render_template,url_for,make_response,request

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Clonwpiece'}
    return render_template('index.html',title='mine',user=user)


@app.route('/set_cookie')
def set_cookie():
    resp=make_response('Hello World')
    resp.set_cookie('Name','Hyman')
    return resp