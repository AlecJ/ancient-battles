from flask import request
from util import loggingFactory
from sqlalchemy import exc
from src.model.db import Battle, Statistic
from datetime import datetime

_getLogger = loggingFactory('api.service')


"""
Handles CRUD operations.

The operations that will be performed are:

create_battle - inserts a new battle into the DB, this is used by the generate_battles celery task.
get_random_battle - get a random battle from the DB and send it to the user.
get_battle_by_id - get a specific battle by its ID and send it to the user.
update_statistic - update some usage statistic in the DB.
"""


def create_battle(session):
    """
    Creates a new battle.

    :param session: The current session
    :return: None
    """
    logger = _getLogger('create_battle')
    try:
        new_battle = Battle(room_code=room_code,
                            created_time=datetime.utcnow(),
                            last_read_time=datetime.utcnow())
        session.add(new_battle)
        session.commit()
        logger.debug('New object successfully inserted into DB: \n{}'.format(new_battle))
        return True
    except exc.SQLAlchemyError as e:
        logger.error(e)
        return False


def get_random_battle(session):
    """
    Query and return a random battle from the Battle table.

    :param session: The current session
    :return: Campaign row
    """
    logger = _getLogger('create_battle')
    try:
        campaign = session.query(RPGManagerCampaign) \
                    .filter(RPGManagerCampaign.room_code==room_code) \
                    .one_or_none()
        # Update last read time
        campaign.last_read_time = datetime.utcnow()
        session.merge(campaign)
        session.commit()
        return campaign
    except (exc.SQLAlchemyError, AttributeError) as e:
        # log e
        return


def update_campaign(session, room_code, name=None, region=None,
                    day=None, party_level=None, money_ratio=None,
                    notes=None, **kwargs):
    """
    Update the campaign that matches the room_code with any provided values.
    """
    try:
        campaign = get_campaign_by_room_code(session, room_code)
        
        # Name and region could be an empty string
        if not name is None:
            campaign.name = name
        if not region is None:
            campaign.region = region
        if day:
            campaign.day = day
        if party_level:
            campaign.party_level = party_level
        if money_ratio:
            campaign.money_ratio = money_ratio
        if not notes is None:
            campaign.notes = notes

        campaign.last_updated_time = datetime.utcnow()

        session.merge(campaign)
        session.commit()
        return campaign
    except exc.SQLAlchemyError as e:
        # log e
        return