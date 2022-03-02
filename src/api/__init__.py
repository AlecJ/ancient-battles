from flask import Blueprint
from flask_restful import Api, Resource

api_blueprint = Blueprint('battle_api', __name__)
api = Api(api_blueprint)


class BattleItem(Resource):
    def get(self):
        return {'name': 'Battle of Alesia',
                '': ''}

api.add_resource(BattleItem, '/')


# class TodoItem(Resource):
#     def get(self, id):
#         return {'task': 'Say "Hello, World!"'}

# api.add_resource(TodoItem, '/todos/<int:id>')