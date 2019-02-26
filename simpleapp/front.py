"""
Trivial frontend
"""

# stdlib
import os
import socket
import sys

# dependencies
from flask import Flask, jsonify, render_template
import requests

# local
from simpleapp.common import Backend


# Get conf from env
SERVICE_CONF = {
        'now': {
            'url': os.environ.get("SAPP_SERVICE_NOW_URL"),
        },
        'timefmt': {
            'url': os.environ.get("SAPP_SERVICE_TIMEFMT_URL"),
        }
    }

if not SERVICE_CONF['now']['url'] or not SERVICE_CONF['timefmt']['url']:
    raise RuntimeError(
        "You must define SAPP_SERVICE_NOW_URL and SAPP_SERVICE_FMT_URL"
    )


APP = Flask(__name__)

MY_NAME = socket.gethostname()
BACKEND = Backend()


def call_service(svc_name, query=""):
    res = None
    try:
        res = requests.get(SERVICE_CONF[svc_name]['url'] + query)
    except Exception as expt:
        raise RuntimeError("Cannot connect to service '%s' (%s): %s" % (svc_name, SERVICE_CONF[svc_name]['url'], str(expt)))

    if res.status_code != 200:
        raise RuntimeError("Bad status from service '%s' (%s): %s" % (svc_name, SERVICE_CONF[svc_name]['url'], str(res.status_code)))

    val = res.json()["value"]
    ver = res.json()["version"]
    return val, ver


@APP.route("/")
@APP.route("/index")
def index():
    """ Index page """

    try:
        now_val, now_ver = call_service("now")
    except RuntimeError as expt:
        return render_template('index.html', name=MY_NAME, error=str(expt))

    try:
        fmt = "%H:%M:%S"
        fmt_val, fmt_ver = call_service("timefmt", query="/%s/%s" % (now_val, fmt))
    except RuntimeError as expt:
        return render_template('index.html', name=MY_NAME, error=str(expt))

    return render_template('index.html', name=MY_NAME, now_val=now_val, now_ver=now_ver, fmt_val=fmt_val, fmt_ver=fmt_ver)


@APP.route("/stats")
def stats():
    """ Some stats """
    res = {"now": BACKEND.get("now"), "timefmt": BACKEND.get("timefmt")}
    return jsonify(res)


if __name__ == "__main__":
    port = 80
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    APP.run(host="0.0.0.0", port=port)
