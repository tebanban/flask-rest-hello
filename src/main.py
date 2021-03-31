"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Favorite, User, Planet, Character

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager




app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

#JWT 
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this "super secret" with something else!
jwt = JWTManager(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# endpoints here...

@app.route('/favorite', methods=['GET'])
def list_favorite():

    response_body = {
        "msg": "Hello, this is your GET /favorite response",
    }
    return jsonify(response_body), 200

@app.route('/user', methods=['GET'])
def list_user():

    response_body = {
        "msg": "Hello, this is your GET /user response ",
    }
    return jsonify(response_body), 200

@app.route('/planet', methods=['GET'])
def list_planet():
    
    response_body = {
        "msg": "Hello, this is your GET /planet response",
    }
    return jsonify(response_body), 200

@app.route('/character', methods=['GET'])
def list_character():
    
    response_body = {
        "msg": "Hello, this is your GET /character response",
    }
    return jsonify(response_body), 200

#JWT
# Create a route to authenticate your users and return JWT Token. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # Query your database for username and password
    user = User.filter.query(username=username, password=password).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })


# POST method here...
@app.route('/addAll', methods=['POST'])
def list_addAll():
    body = request.get_json()
    people = body['character'] 
    planet = body['planet']
    vehicles = body['starship']

    for c in character:
        character1 = Character(
            name = c["Character Name"],
            heigth =c["Character heigth"],
            mass = c["Character mass"],
            hair_color = c["Character hair color"],
            skin_color = c["Character skin color"],
            gender = c["Character Gender"]
        )
        db.session.add(character1)

    for p in planet:
        planet1 = Planet (
            name = p["Name"],
            diameter = p["Diameter"],
            climate = p["Climate"],
            gravity= p["Gravity"],
            population = p["Population"]

        )
        db.session.add(planet1)

    for s in starship:
        starships1 = Starship (
            name = s["Vehicle name"],
            model = s["Model"],
            passengers = serialize["Passengers"],
            consumable = s["consumable"],
            cargo_capacity = s["Cargo capacity"],
            hyperdrive_rating = s["Hyperdrive rating"]

        )
        db.session.add(starship1)




        db.session.commit()


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
