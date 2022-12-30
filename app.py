from flask import Flask, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

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
