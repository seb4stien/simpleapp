"""
Trivial frontend
"""
# stdlib
from datetime import datetime
import os
import sys

# dependencies
from flask import Flask, jsonify

# local
from simpleapp.common import Backend

VERSION = os.environ.get("SAPP_VERSION", "unknown")

app = Flask(__name__)
backend = Backend()


@app.route("/strftime/<int:time>/<string:fmt>")
def strftime(time, fmt):
    backend.increment("timefmt")
    out = datetime.fromtimestamp(time).strftime(fmt)
    return jsonify({"input": time, "format": fmt, "value": out, "version": VERSION})


if __name__ == "__main__":
    port = 80
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port)
