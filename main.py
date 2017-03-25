#!/usr/bin/python

from flask import Flask, render_template, request, send_from_directory, url_for
import tempfile

app = Flask(__name__)

@app.route("/")
def run_it():
    return render_template("index.html", button=url_for('static', filename='button.jpg'), url=request.url_root)

@app.route('/upload_it', methods=['GET'])
def upload_file():
    result = request.args.get("data");

    print "got result: " + result;

    return ""

if __name__ == "__main__":
    app.run()
