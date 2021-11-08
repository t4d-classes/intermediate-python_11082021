""" rates api """

from typing import Any
import pathlib
import csv
import math
import time
from flask import Flask, Response, request, jsonify, abort


app = Flask(__name__)


@app.route("/check")
def check() -> Response:
    """ health check endpoint """
    return "READY"


@app.route("/")
def home() -> Response:
    """ home """
    return "<h1>Hello, World!</h1>"


def start_rates_api() -> None:
    """ start rates api """

    app.run()


if __name__ == "__main__":
    start_rates_api()
