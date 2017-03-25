#!/usr/bin/python

from flask import Flask
from flask import render_template
import tempfile

app = Flask(__name__)

@app.route("/")
def run_it():
    return render_template("index.html")

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     f = request.files['text_file']
#     temp_file = tempfile.mkstemp()
#     f.save(temp_file[1])
#     # Colin ... do something!!!

if __name__ == "__main__":
    app.run()
