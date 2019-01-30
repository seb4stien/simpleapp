"""
Trivial frontend
"""

# stdlib
import socket

# dependencies
from flask import Flask

# local
from simpleapp.common import Backend


myname = socket.gethostname()

app = Flask(__name__)
app.config["MYNAME"] = myname

backend = Backend()
backend.register(myname)

@app.route('/')
def index():
    return "Hello, I am {} in a group of {}".format(
            app.config['MYNAME'],
            backend.members())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1235)
