import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set config variables for the flask app.
    Using Env. variables where available
    Otherwise create the config variable if not done already
    """

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')


    SECRET_KEY = os.environ.get('SECRET') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get(import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgres://dqozjmhc:tZdN1aJQTdolbXSDkg-U19j6ZAKbrBer@chunee.db.elephantsql.com/dqozjmhc')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages from sqlaclchemy