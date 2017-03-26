#!/usr/bin/python

from flask import Flask, render_template, request, send_from_directory
from subprocess import call
import tempfile
import RAKE
import re

app = Flask(__name__, static_folder='static', static_url_path='/static')

def clean_sentence(text):
    path = "words.txt"
    r = RAKE.Rake(path)
    k = []
    for word in text.split("."):
        k.append(r.run(word))

    clean_string = []
    for word in k:
        clean_string.append(re.sub('[^A-Za-z ]+', '', str(word)))

    result_string = ""
    for word in clean_string:
        result_string += word + " "
    return result_string

@app.route("/")
def run_it():
    return render_template("index.html", url=request.url_root)

# @app.route('/sunilemail.php')
# def handle_mail():
#     return send_from_directory(app.static_folder, request.path[1])

# @app.route('/triggercalendar.php')
# def handle_calender():
#     return send_from_directory(app.static_folder, request.path[1])

@app.route('/upload_it', methods=['GET'])
def upload_it():
    result = request.args.get("data")
    email_address = request.args.get("email")

    if (result == None or email_address == None):
        return ""

    call(['php', '-f', 'static/sunilemail.php', email_address, result])
    return ""

if __name__ == "__main__":
    app.run()
