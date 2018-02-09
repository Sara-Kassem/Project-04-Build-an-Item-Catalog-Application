from flask import Flask, render_template, url_for, request, redirect
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Course, Recipe, Ingredients, Directions

app = Flask(__name__)


# ----------------------- #
#        SQLAlchemy       #
# ----------------------- #

engine = create_engine('sqlite:///healthyRecipes.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=7070)
