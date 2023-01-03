from flask import (Flask, request, redirect, url_for, flash, 
                   render_template, abort, session, current_app,
                   make_response, send_file, send_from_directory, 
                   after_this_request, g, escape, has_request_context,
                   get_template_attribute)
from flask.logging import create_logger
from werkzeug.utils import secure_filename, append_slash_redirect
from werkzeug.urls import url_encode, url_decode
from datetime import datetime
from logging import getLogger

app = Flask(__name__)
app.secret_key = 'secret'
app.config['SITE_NAME'] = 'orange'
app.static_folder = 'static'
app.config['SESSION_PERMANENT'] = True
# app.session_interface = 'memory'


@app.route('/home')
def home():
    return '<h1> HELLO GUYS </h1>'


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
    session['name'] = "{'name':'MM'}"
    return 'Session data stored'


@app.route('/get_session')
def get_session_api():
    value = session['key']
    return value


@app.route('/delete_session')
def delete_session_api():
    session.clear()
    try:
        value = session['Name']
    except:
        value = 'Not found'
    
    return value


@app.route('/abort')
def abort_api():
    true = True
    if not true:
        return 'Hey'
    return abort(402)


@app.route('/make_response')
def make_response_api():
    response_data = dict(
        status = 'Success',
        statusCode = 200,
        message = "It's working"
    )
    response = make_response(response_data, 200)
    response.headers['Content-Type'] = 'application/json'
    response.set_cookie('name', 'ibrahim')

    return response


@app.route('/get_cookie')
def get_cookie_api():
    if 'cookie_name' in request.cookies:
        return request.cookies.get('name', 'Not found')
    else:
        return 'Cookie does not exist'
   

@app.route('/send_file')
def send_file_api():
    file_path = "static/mr.jpg"
    return send_file(file_path, mimetype='image/jpg', as_attachment=True)


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
    file = 'mr.jpg'
    return send_from_directory('static', file)


@app.route('/escape')
def escape_api():
    # str_ = "He%$y)(!@$# <>-"
    # str_ = "&lth1&gt Hey &lt/h1&gt"
    
    without_escape = "<h1> str_nd\nkfsl </h1>" 
    with_escape = escape("<h1> str_nd\nkfsl </h1>")
    
    return with_escape


@app.route('/has_request_context')
def has_request_context_api():
    a = has_request_context()
    
    return str(a) 


@app.route('/get_template_attribute')
def get_template_attribute_api():

    attr = get_template_attribute('index.html', 'title')
    return attr


@app.route("/send_static_file")
def send_static_file_api():
    return app.send_static_file('mr1.jpg')


# @app.route("/url_value_preprocessor")
# def url_value_preprocessor_api():
#     a = 10
#     a+=1
    
#     return a