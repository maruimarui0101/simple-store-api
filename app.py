from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db

# no need for use of jsonify, flask_restful takes care of it, ok to return dictionaries

app = Flask(__name__)
# Where does the database live?
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# specify configuration property
# turns off flask-sqlalchemy tracker, not sqlchemy tracker
# tracks changes to object and makes sure they are saved to the db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'key'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth endpoint

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
