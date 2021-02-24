from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db
from instance.config import app_config


def create_app(config_name):

    # no need for use of jsonify, flask_restful takes care of it, ok to return dictionaries

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # Where does the database live?
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    # specify configuration property
    # turns off flask-sqlalchemy tracker, not sqlchemy tracker
    # tracks changes to object and makes sure they are saved to the db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'key'
    api = Api(app)

   

    jwt = JWT(app, authenticate, identity) # /auth endpoint

    api.add_resource(Item, '/item/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(StoreList, '/stores')
    api.add_resource(UserRegister, '/register')

    db.init_app(app)

    return app

