""" rates api """

from typing import Any
import pathlib
import csv
import math
import time
from flask import Flask, Response, request, jsonify, abort

