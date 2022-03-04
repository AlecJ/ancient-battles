from sqlalchemy import exc
from sqlalchemy.sql.expression import func
from datetime import datetime
from src.util import loggingFactory
from src.models.models import Battle, Statistic


_getLogger = loggingFactory('api.service')


"""
Handles CRUD operations.

The operations that will be performed are:

create_battle - inserts a new battle into the DB, this is used by the generate_battles celery task.
get_shuffled_list_of_battles - gets a shuffled list of battles for the user to work through.
get_battle_by_id - get a specific battle by its ID and send it to the user.
update_statistic - update some usage statistic in the DB.
"""


def create_battle(session, battleName, date, location, answer, belligerentA, belligerentB, leaderAName, leaderBName, 
                  leaderAImageLink, leaderBImageLink, wikipediaBlurb=None, wikipediaLink=None):
    """
    Insert a battle into the database.

    This is used by a celery job that triggers the web scraper.
    No user endpoint hits this.

    :param session: The current session
    :return: None
    """
    logger = _getLogger('create_battle')
    try:
        new_battle = Battle(battleName=battleName,
                            date=date,
                            location=location,
                            answer=answer,
                            belligerentA=belligerentA,
                            belligerentB=belligerentB,
                            leaderAName=leaderAName,
                            leaderBName=leaderBName,
                            leaderAImageLink=leaderAImageLink,
                            leaderBImageLink=leaderBImageLink,
                            wikipediaBlurb=wikipediaBlurb,
                            wikipediaLink=wikipediaLink,
                            created_time=datetime.utcnow(),
                            last_read_time=datetime.utcnow())
        session.add(new_battle)
        session.commit()
        logger.debug('New object successfully inserted into DB: \n{}'.format(new_battle))
        return True
    except exc.SQLAlchemyError as e:
        logger.error(e)
        return False


def get_shuffled_list_of_battles(session):
    """
    Query the list of battles and return a randomly shuffled list
    of IDs for the user to begin working through.

    Also get and return the first battle in the list.

    :param session: The current session
    :return: List of int, Battle IDs
    """
    logger = _getLogger('get_shuffled_list_of_battles')
    try:
        battle_list = session.query(Battle.id) \
                          .order_by(func.random()) \
                          .all() #.limit(10)
        # convert tuples to simple list
        battle_list = [x.id for x in battle_list]
        logger.debug('List to give to user: \n{}'.format(battle_list))
        return battle_list
    except (exc.SQLAlchemyError, AttributeError) as e:
        logger.error(e)
        return None


def get_battle_by_id(session, id):
    """
    Query a battle by ID and send it to the user.

    :param session: The current session
    :param id: The ID of the battle to query
    :return: Dict, Battle object
    """
    logger = _getLogger('get_battle_by_id')
    try:
        battle = session.query(Battle) \
                        .filter(Battle.id==id) \
                        .one_or_none()
        logger.debug('Battle retrieved for user: \n{}'.format(battle))
        return battle
    except (exc.SQLAlchemyError, AttributeError) as e:
        logger.error(e)
        return []  # return empty list to make the endpoint checking the result easier