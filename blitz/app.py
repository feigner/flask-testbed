import os

from flask import Flask
from flask import Flask, request, g, redirect, url_for, abort, render_template, flash

from blitz.database import db_session

#CONFIG
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#APP
app = Flask(__name__)
app.config.from_object(__name__)

#HOOKS
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

#VIEWS
@app.route("/")
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
