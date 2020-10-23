from datetime import datetime
import flask
import re
import os
import platform


application = flask.Flask(__name__)

@application.route("/")
def home():
    content = "<br>This is application.py, running on AWS"
    content = "<br>[OS] " + platform.platform() + "<br> [Time] " + datetime.now().strftime("%A, %d %B, %Y at %X") + content
    content = "[TEXT] " + "Version 1" + content
    return content

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)