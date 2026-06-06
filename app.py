from flask import Flask, render_template, request, redirect, session
from database import contacts
from datetime import datetime

from config import (
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
    SECRET_KEY
)

app = Flask(__name__)

app.secret_key = SECRET_KEY


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Contact Form
@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    contacts.insert_one({
        "name": name,
        "email": email,
        "message": message,
        "created_at": datetime.now()
    })

    return render_template('success.html')


# Admin Login
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            session['admin'] = True

            return redirect('/admin')

        return render_template(
            'admin_login.html',
            error="Invalid Username or Password"
        )

    return render_template('admin_login.html')


# Admin Dashboard
@app.route('/admin')
def admin():

    if not session.get('admin'):
        return redirect('/admin-login')

    messages = list(
        contacts.find().sort("created_at", -1)
    )

    return render_template(
        'admin.html',
        messages=messages,
        total_messages=len(messages)
    )


# Logout
@app.route('/logout')
def logout():

    session.pop('admin', None)

    return redirect('/admin-login')


if __name__ == '__main__':
    app.run()