#!/usr/bin/python

from flask import Flask, render_template, request, send_from_directory, url_for
import tempfile

app = Flask(__name__)

@app.route("/")
def run_it():
    return render_template("index.html", url=request.url_root)

@app.route('/upload_it', methods=['GET'])
def upload_it():
    result = request.args.get("data")
    email_address = request.args.get("email")

    print "got result: " + result
    print "with email: " + email_address

    return ""

if __name__ == "__main__":
    app.run()
