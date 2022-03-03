from multiprocessing.sharedctypes import Value
from flask import Blueprint
from flask_restful import Api, Resource
from src.util import session_scope, loggingFactory
from src.api.service import get_shuffled_list_of_battles, get_battle_by_id
from src.tasks.seed import seed_battles

_getLogger = loggingFactory('api')


"""
Routes and methods:

GET /
    When the user first arrives, they will get a random list of IDs of battles.

    The list is stored in local storage. This ensures they get a random battle each time
    and lessens the chance of repeats.

    To save time, they are also given their first battle along with the list.


GET /battle/<int:id>
    Get a battle by ID and send it to the user.
"""

api_blueprint = Blueprint('battle_api', __name__)
api = Api(api_blueprint)


class BattleAPI(Resource):
    def get(self, id=None):
        logger = _getLogger('BattleAPI.get')

        logger.debug('seeding csv')
        seed_battles('/app/src/seed.csv')

        # with session_scope() as session:
        #     result = {}
        #     if id is None:
        #         # fetch a list of battles
        #         list_of_battle_ids = get_shuffled_list_of_battles(session)
        #         # now fetch the first battle from the list
                
        #         if len(list_of_battle_ids) == 0:
        #             error_msg = 'Empty list of battle IDs returned from get_shuffled_list_of_battles.'
        #             logger.error(error_msg)
        #             raise ValueError(error_msg)

        #         result['list_of_battle_IDs'] = list_of_battle_ids

        #     # fetch battle by ID
        #     battle = get_battle_by_id(session, id or list_of_battle_ids[0])
        #     result['battle'] = battle

        #     return result


api.add_resource(BattleAPI, '/', '/battle/<int:id>')