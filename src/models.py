from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Favorite(db.Model):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    username = db.Column (db.String(250))

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250))
    password = db.Column(db.String(10))
    #favorites= db.relationship(Favorites)

    
    
class Character(db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    
    
class Planet(db.Model):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.String(30))
    climate = db.Column(db.String(250))
    population = db.Column(db.Integer)
   

class Starship(db.Model):
    __tablename__ = 'starship'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250))
    passengers = db.Column(db.Integer)
    consumable = db.Column(db.String(250))
    cargo_capacity = db.Column(db.Integer)
    hyperdrive_rating = db.Column(db.Integer)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
#render_er(db.Model, 'diagram.png')