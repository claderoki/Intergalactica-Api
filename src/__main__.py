import json

from flask import Flask, request

import src.config as config
from src.models import Location, database

app = Flask(__name__)

@app.route("/location/save", methods = ["POST"])
def location_save():
    post = json.loads(request.data)
    with database.connection_context():
        location = Location.create(**post)

    return {"success" : True, "id" : location.id}

app.run()