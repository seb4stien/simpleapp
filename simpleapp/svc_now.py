"""
Trivial frontend
"""
# stdlib
import os
import sys
import time

# dependencies
from flask import Flask, jsonify

# local
from simpleapp.common import Backend

VERSION = os.environ.get("SAPP_VERSION", "unknown")


app = Flask(__name__)
backend = Backend()


@app.route("/now")
def now():
    backend.increment("now")
    return jsonify({"value": int(time.time()), "version": VERSION})


if __name__ == "__main__":
    port = 80
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host="0.0.0.0", port=port)
