import json

from flask import Flask, request
from waitress import serve

import src.config as config
from src.models import Location, database

app = Flask(__name__)
config.app = app

@app.route("/location/save", methods = ["POST"])
def location_save():
    post = json.loads(request.data)
    with database.connection_context():
        location = Location.create(**post)

    return {"success" : True, "id" : location.id}

serve(app, host = '0.0.0.0')