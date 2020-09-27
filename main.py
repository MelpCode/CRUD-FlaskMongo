from flask import Flask,jsonify,Response,request
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import config;

app = Flask(__name__)

#Settings database:
app.config['MONGO_URI']=config.MONGODB_URI
mongo = PyMongo(app)

#Route to show all the menus:
@app.route('/api/menus/',methods=['GET'])
def get_menus():
    users = mongo.db.menus.find()
    response = json_util.dumps(users)
    return Response(response,mimetype='application/json')

#Route to create a new Menu:
@app.route('/api/menus/',methods=['POST'])
def create_menu():
    sideDish = request.json['sideDish']
    starter = request.json['starter']
    starterDet = request.json['starterDet']
    main = request.json['main']
    mainDet = request.json['mainDet']
    dessert = request.json['dessert']
    dessertDet = request.json['dessertDet']
    price = request.json['price']

    if starter and main and dessert and price:
        id = mongo.db.menus.insert(
            {'sideDish':sideDish,
             'starter':starter,
             'starterDet':starterDet,
             'main':main,
             'mainDet':mainDet,
             'dessert':dessert,
             'dessertDet':dessertDet,
             'price':price}
        )
        return jsonify({'status':'New Menu saved'})

#Route to update a specific menu:
@app.route('/api/menus/<id>',methods=["PUT"])
def update_menu(id):
    sideDish = request.json['sideDish']
    starter = request.json['starter']
    starterDet = request.json['starterDet']
    main = request.json['main']
    mainDet = request.json['mainDet']
    dessert = request.json['dessert']
    dessertDet = request.json['dessertDet']
    price = request.json['price']
    if starter and main and dessert and price:
        mongo.db.menus.update_one({'_id':ObjectId(id)},{'$set':{
            'sideDish':sideDish,
             'starter':starter,
             'starterDet':starterDet,
             'main':main,
             'mainDet':mainDet,
             'dessert':dessert,
             'dessertDet':dessertDet,
             'price':price
        }})
    response = jsonify({'status':'Menu updated'})
    return response

#Route to show an specific menu:
@app.route('/api/menus/<id>',methods=["GET"])
def get_menu(id):
    menu = mongo.db.menus.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(menu)
    return Response(response,mimetype='application/json')

#Route to delete a specific menu:
@app.route('/api/menus/<id>',methods=['DELETE'])
def delete_menu(id):
    mongo.db.menus.delete_one({'_id':ObjectId(id)})
    return jsonify({'status':'Menu deleted'})



#Server Inicialization:
if __name__ == '__main__':
    app.run(port=4000,debug=True)