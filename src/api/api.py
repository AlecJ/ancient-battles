from flask import Blueprint

api_blueprint = Blueprint('who_won', __name__)

@api_blueprint.route('/')
def index():
    # update usage stats

    # create a new match

    # send question to user

@api_blueprint.route('/answer')
def answer():
    # expect a match id and a guess

    # if correct, respond with correct

    # else, respond incorrect

    # update usage stats

    # remove old match