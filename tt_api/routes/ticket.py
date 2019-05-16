from flask import Blueprint
from flask_jsonpify import jsonify
# from errors.errors import PageNotFound
from tt_api.modules.ticket import ticket as ticket_module


ticket_api = Blueprint('ticket_api', __name__)


@ticket_api.route("/ticket/<id>")
def get(id=0):
    # raise PageNotFound('Page Not Found', status_code=404)
    ticket = ticket_module.getTicket(id)
    return jsonify({'ticket': ticket}) 