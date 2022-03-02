import os
import logging
import logging.config
from environs import Env
# from contextlib import contextmanager
# import sqlalchemy
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy_utils import database_exists, create_database

'''
Config and Environment
'''

class Config(object):
    _env = None
    _DB_URL = None
    _engine = None

    @property
    def env(self):
        if self._env is None:
            self._env = Env()
            self._env.read_env()
        return self._env
    
    @property
    def ENVIRONMENT(self):
        return self.env.str("FLASK_ENV", default="production")

    # @property
    # def DB_URL(self):
    #     if self._DB_URL is None:
    #         if self.ENVIRONMENT == 'development':
    #             self._DB_URL = self.cfg_parser.get('database', 'db_dev_url')
    #         else:
    #             self._DB_URL = self.cfg_parser.get('database', 'db_prod_url')
    #     return self._DB_URL

    # @property
    # def engine(self):
    #     if self._engine is None:
    #         url = os.environ.get('DATABASE_URL')
    #         if not url:
    #             url = self.DB_URL

    #         # Queue pool is already there by default, and we can just set the
    #         # pool parameters without creating or referencing a pool object
    #         # pool size is how many connections to hand out, 15 is the
    #         # max, and the pool recycle parameter says that don't keep
    #         # a connection for more than 900 seconds (15 minutes).
    #         self._engine = sqlalchemy.create_engine(
    #             url,
    #             # json_serializer=custom_dumps,
    #             # json_deserializer=custom_loads,
    #             isolation_level='READ_COMMITTED',
    #             pool_size=5,
    #             max_overflow=15,
    #             pool_recycle=900
    #         )

    #         # make sure database exists
    #         # TODO does not work with heroku db
    #         # if not database_exists(url):
    #             # create_database(url)

    #     return self._engine

config = Config()


'''
Logging
'''
logging_config_path = os.path.join(os.path.dirname(__file__), 'logging.ini')
logging.config.fileConfig(logging_config_path)

def loggingFactory(module):
    """
    Factory method that returns a logger generation function with the
    prefix for the modules where it is used.
        _getLogger=loggingFactory('util.alstore')
        logger=_getLogger('method')
        logger.debug('Bla')
    :param module: optional namespace
    :return:
    """        

    def getLogger(method=None):
        name = "battles." + (module if method is None else module + "." + method)
        return logging.getLogger(name)

    return getLogger


'''
Session Management
'''

# Session = None

# @contextmanager
# def session_scope():
#     """Provide a transactional scope around a series of operations."""
#     # Init session
#     if Session is None:
#         Session = sessionmaker(bind=config.engine)

#     session = Session()
#     try:
#         yield session
#         session.commit()
#     except:
#         session.rollback()
#         raise
#     finally:
#         session.close()