from flask import Flask
from datetime import datetime
import re
import os
import platform


app = Flask(__name__)

@app.route("/")
def home():
    content = "<br>[OS] " + platform.platform() + "<br> [Time] " + datetime.now().strftime("%A, %d %B, %Y at %X")
    content = "[TEXT] " + "Version 6" + content
    return content
