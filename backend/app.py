import time

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS is a required security feature to allow the front end
# to send requests to the back end.
CORS(app)


@app.route('/')
def hello_world():
    # Add a one second delay to the request to make it look like
    # we're calculating something.
    time.sleep(1)

    return jsonify(f"Hello World! I'm a Python 3 server")
