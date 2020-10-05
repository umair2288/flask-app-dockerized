from flask import jsonify
from app import app
import json


@app.route("/predict" , methods=["POST"])
def hello():
    resonse  = {
        "success":True,
        "message": "prediction sucessfull",
        "data" : {
            "healthy" : 0.502
        }
    }
    return jsonify(resonse)