from flask import Flask
from datetime import datetime
import re
import os
import platform


app = Flask(__name__)

@app.route("/")
def home():
    content = "<br>[OS] " + platform.platform() + "<br> [Time] " + datetime.now().strftime("%A, %d %B, %Y at %X")
    content = "[TEXT] " + "Version 1" + content
    content += "<br>This is main.py, runnin on GCP"
    return content

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)