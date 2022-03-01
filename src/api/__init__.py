from flask import Blueprint

api_blueprint = Blueprint('battle_api', __name__)


@api_blueprint.route('/')
def index():
    return "hello world"
    # update usage stats

    # create a new match

    # send question to user


@api_blueprint.route('/battle')
def battle():
    return {'name': 'Battle of Alesia',
            '': ''}, 200
