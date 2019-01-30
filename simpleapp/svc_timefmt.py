"""
Trivial frontend
"""
# stdlib
from datetime import datetime
import sys

# dependencies
from flask import Flask, jsonify

# local
from simpleapp.common import Backend

app = Flask(__name__)
backend = Backend()

@app.route('/strftime/<int:time>/<string:fmt>')
def strftime(time, fmt):
    backend.increment('timefmt')
    out = datetime.fromtimestamp(time).strftime(fmt)
    return jsonify({
        'input': time,
        'format': fmt,
        'output': out,
        })

if __name__ == "__main__":
    port = 80
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port)
