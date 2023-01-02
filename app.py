from flask import (Flask, request, redirect, url_for, flash, 
                   render_template, abort, session,
                   make_response, send_file, send_from_directory)
from werkzeug.utils import secure_filename
from werkzeug.urls import url_encode, url_decode

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/home')
def home():
    return 'Hello world'


@app.route('/secure_filename')
def secure_filename_api():
    f_name = 'Example Name@!-1'
    secured_filename = secure_filename(f_name)
    
    return secured_filename


@app.route('/redirect')
def redirect_api():
    redirect_url = 'https://erp.softsuave.in/app/timesheet'
    return redirect(redirect_url)


@app.route('/url_for')
def url_for_api():
    return redirect(url_for('home'))


@app.route('/flash')
def flash_api():
    if True:
        flash('Success')
        return render_template('index.html', flash=True)
    

@app.route('/session')
def session_api():
    session['key'] = 'value'
    return 'Session data stored'


@app.route('/get_session')
def get_session_api():
    value = session['key']
    return value


@app.route('/delete_session')
def delete_session_api():
    session.clear()
    try:
        value = session['key']
    except:
        value = 'Not found'
    
    return value


@app.route('/abort')
def abort_api():
    true = True
    if not true:
        return 'Hey'
    return abort(401)


@app.route('/make_response')
def make_response_api():
    response_data = dict(
        status = 'Success',
        statusCode = 200,
        message = "It's working"
    )
    response = make_response(response_data, 200)
    response.headers['Content-Type'] = 'application/json'
    response.set_cookie('cookie_name', 'cookie_value')

    return response


@app.route('/get_cookie')
def get_cookie_api():
    if 'cookie_name' in request.cookies:
        return request.cookies['cookie_name']
    else:
        return 'Cookie does not exist'
    

@app.route('/send_file')
def send_file_api():
    file_path = "static/mr.jpg"
    return send_file(file_path, mimetype='image/jpg', as_attachment=False)


@app.route('/url_encode')
def url_encode_api():
    query_params = {'q': 'flask', 'sort': 'relevance'}
    query_string = url_encode(query_params)
    
    return query_string


@app.route('/url_decode')
def url_decode_api():
    query_string = 'q=flask&sort=relevance'
    query_params = url_decode(query_string)
    
    return query_params


@app.route('/send_from_directory')
def send_from_directory_api():
    file = '/static/mr.jpg'
    return send_from_directory(file, )