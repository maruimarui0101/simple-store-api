# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank."
    )
    parser.add_argument('store_id',
        type=float,
        required=True,
        help="Every item needs a store id."
    )

    #@jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found!'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name "{}" already exists'.format(name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured inserting!'}, 500 # Internal server error

        return item.json(), 201

    def delete(self, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "DELETE FROM items WHERE name = ?"
        # result = cursor.execute(query, (name,))
        #
        # connection.commit()
        # connection.close()
        #
        # return {'message': 'Item deleted!'}

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted!'}

    def put(self, name):
        data = self.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        if item is None:
            # try:
            #     updated_item.insert()
            # except:
            #     return {'message': 'An error occured inserting!'}, 500
            item = ItemModel(name, data['price'], data['store_id'])

        else:
            # try:
            #     updated_item.update()
            # except:
            #     return {'message': 'An error occured updating!'}, 500
            item.price = data['price']
            item.store_id = data['store_id']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #
    #     select_query = "SELECT * FROM items"
    #     result = cursor.execute(select_query)
    #     items = []
    #     for row in result:
    #         items.append(row)
    #
    #     connection.commit()
    #     connection.close()
    #
    #     return {'items': items}, 200

        return {'items': [item.json() for item in ItemModel.query.all()]}
