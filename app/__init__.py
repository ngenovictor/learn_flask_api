from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from instance import config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    """
    function wraps the creation of a new Flask object, and returns it after 
    it's loaded up with configuration settings using app.config and connected 
    to the DB using db.init_app(app)
    :param config_name: name of the server environment use to run the app
    :type config_name: str 
    """
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(config.get_config(config_name))
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    return app
