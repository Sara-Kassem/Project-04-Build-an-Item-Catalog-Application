from flask import Flask, render_template, url_for, request, redirect
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Course, Recipe, Ingredients, Directions

app = Flask(__name__)

latestRecipesLimit = 3

# ----------------------- #
#        SQLAlchemy       #
# ----------------------- #

engine = create_engine('sqlite:///healthyRecipes.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# ----------------------- #
#        Home Page        #
# ----------------------- #

@app.route('/')
@app.route('/healthy-recipes')
def homePage():
    courses = session.query(Course).order_by(Course.id).all()
    latestRecipes = session.query(Recipe).order_by(Recipe.id.desc()).all()

    return render_template('index.html',
    courses=courses,
    latestRecipes=latestRecipes)

@app.route('/course/<int:course_id>/')
@app.route('/course/<int:course_id>/recipes')
def courseRecipes(course_id):
    courses = session.query(Course).order_by(Course.id).all()
    recipes = session.query(Recipe).order_by(Recipe.name).filter_by(course_id=course_id).all()

    return render_template('courseRecipes.html',
    courses=courses,
    recipes=recipes)

@app.route('/recipes/<int:recipe_id>')
def recipe(recipe_id):
    courses = session.query(Course).order_by(Course.id).all()
    recipe = session.query(Recipe).filter_by(id=recipe_id).one()
    ingredients = session.query(Ingredients).filter_by(recipe_id=recipe_id).all()
    directions = session.query(Directions).filter_by(recipe_id=recipe_id).all()

    return render_template('recipe.html',
    courses=courses,
    recipe=recipe,
    ingredients=ingredients,
    directions=directions
    )

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=7070)
