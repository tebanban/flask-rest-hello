from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
# import os
# import sys
# from sqlalchemy import db.Column, ForeignKey, db.Integer, db.String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy import create_engine
# from eralchemy import render_er

db.Model = SQLAlchemy()


class Favorites(db.Model):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name= db.Column (db.String(250))

class Users(db.Model):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250))
    password = db.Column(db.String(10))
    favorites= db.relationship(Favorites)

    
    
class Characters(db.Model):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter= db.Column(db.Integer)
    gravity= db.Column(db.String(30))
    climate= db.Column(db.String(250))
    population= db.Column(db.Integer)
    
class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter= db.Column(db.Integer)
    gravity= db.Column(db.String(30))
    climate= db.Column(db.String(250))
    population= db.Column(db.Integer)
   

class Starships(db.Model):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height= db.Column(db.Integer)
    mass= db.Column(db.Integer)
    hair_color= db.Column(db.String(250))
    skin_color= db.Column(db.String(250))
    gender= db.Column(db.String(20))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
#render_er(db.Model, 'diagram.png')