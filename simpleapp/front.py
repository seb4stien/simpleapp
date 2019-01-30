"""
Trivial frontend
"""

# stdlib
import os
import socket
import sys
import time

# dependencies
from flask import Flask, jsonify
import requests

# local
from simpleapp.common import Backend


SERVICE_NOW = "http://" + os.environ.get('SERVICE_NOW', '127.0.0.1') + "/now"
SERVICE_TIMEFMT = "http://" + os.environ.get('SERVICE_TIMEFMT', '127.0.0.1') + "/strftime"

app = Flask(__name__)

me = socket.gethostname()
backend = Backend()

@app.route('/')
def index():
    res = {
            'me': me,
    }

    now = requests.get(SERVICE_NOW).json()['now']
    time = requests.get(SERVICE_TIMEFMT + '/' + str(now) + '/%H:%M').json()['output']
    res['time'] = time

    return jsonify(res)

@app.route('/stats')
def stats():
    res = {
            'now': backend.get('now'),
            'timefmt': backend.get('timefmt')
    }
    return jsonify(res)


if __name__ == "__main__":
    port = 80
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port)
