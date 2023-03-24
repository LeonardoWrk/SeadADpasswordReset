
from random import choice
import string
from flask import Flask, render_template, request, redirect, url_for
from func import gerar_senha, run, get_email, get_change_user

app = Flask(__name__)

# the login page route
@app.route('/')
def login():
    return render_template('login.html')

# the form submission route
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    emailD = request.form['email']

    # negocio muito doido q eu fiz, nem lembro mais como funciona
    email = get_email(username, emailD)
    if email:
        get_change_user(username, gerar_senha())

    return redirect(url_for('login'))

# the home page route
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
