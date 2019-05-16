from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

from tt_api.routes.ticket import ticket_api

app = Flask(__name__)
api = Api(app)

CORS(app)

app.register_blueprint(ticket_api)

@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})



if __name__ == '__main__':
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(port=5002)