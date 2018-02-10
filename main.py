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

latestRecipesLimit = 3

# ----------------------- #
#        Home Page        #
# ----------------------- #


@app.route('/')
@app.route('/healthy-recipes')
def homePage():

    all_courses = session.query(Course).order_by(Course.id).all()

    latestRecipes = session.query(Recipe).order_by(Recipe.id.desc()).all()

    return render_template('index.html',
                           all_courses=all_courses,
                           latestRecipes=latestRecipes
                           )


@app.route('/course/<int:course_id>/')
@app.route('/course/<int:course_id>/recipes')
def courseRecipes(course_id):

    all_courses = session.query(Course).order_by(Course.id).all()

    course = session.query(Course).filter_by(id=course_id).one()

    courseRecipes = session.query(Recipe).order_by(Recipe.name).filter_by(
        course_id=course_id).all()

    return render_template('courseRecipes.html',
                           all_courses=all_courses,
                           courseRecipes=courseRecipes,
                           course=course)


@app.route('/course/<int:course_id>/recipes/<int:recipe_id>')
def viewRecipe(course_id, recipe_id):
    all_courses = session.query(Course).order_by(Course.id).all()

    viewRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    ingredients = session.query(Ingredients).filter_by(
        recipe_id=recipe_id).all()

    directions = session.query(Directions).filter_by(recipe_id=recipe_id).all()

    return render_template('viewRecipe.html',
                           all_courses=all_courses,
                           viewRecipe=viewRecipe,
                           recipeCourse=recipeCourse,
                           ingredients=ingredients,
                           directions=directions
                           )


@app.route('/course/<int:course_id>/recipes/<int:recipe_id>/delete',
           methods=['GET', 'POST'])
def deleteRecipe(course_id, recipe_id):

    all_courses = session.query(Course).order_by(Course.id).all()

    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    deleteRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    if request.method == 'POST':

        session.delete(deleteRecipe)
        session.commit()

        return redirect(url_for('courseRecipes',
                                course_id=recipeCourse.id))

    else:
        return render_template('deleteRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse,
                               deleteRecipe=deleteRecipe
                               )


@app.route('/course/<int:course_id>/recipes/<int:recipe_id>/edit',
           methods=['GET', 'POST'])
def editRecipe(course_id, recipe_id):

    all_courses = session.query(Course).order_by(Course.id).all()

    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    editRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    ingredients = session.query(Ingredients).filter_by(
        recipe_id=recipe_id).all()

    directions = session.query(Directions).filter_by(
        recipe_id=recipe_id).all()

    if request.method == 'POST':

        if request.form['updateName']:
            editRecipe.name = request.form['updateName']

        if request.form['updateCourse']:
            updateCourse = session.query(Course).filter_by(
                name=request.form['updateCourse']).one()
            editRecipe.course_id = updateCourse.id

        session.add(editRecipe)
        session.commit()

        for i in ingredients:
            session.delete(i)
            session.commit()

        ingredients_line = request.form['updateIngredients'].splitlines()

        for i in range(len(ingredients_line)):

            if ingredients_line[i]:

                newIngredient = Ingredients(
                    recipe_id=recipe_id,
                    ingr_number=i + 1,
                    ingredient=ingredients_line[i]
                )

                session.add(newIngredient)
                session.commit()

        for i in directions:
            session.delete(i)
            session.commit()

        directions_line = request.form['updateDirections'].splitlines()

        for i in range(len(directions_line)):

            if directions_line[i]:

                newDirection = Directions(
                    recipe_id=recipe_id,
                    step_number=i + 1,
                    step=directions_line[i]
                )

                session.add(newDirection)
                session.commit()

        return redirect(url_for('viewRecipe',
                                course_id=recipeCourse.id,
                                recipe_id=editRecipe.id))

    else:
        return render_template('editRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse,
                               editRecipe=editRecipe,
                               ingredients=ingredients,
                               directions=directions
                               )


@app.route('/course/<int:course_id>/recipes/new', methods=['GET', 'POST'])
def newRecipe(course_id):

    all_courses = session.query(Course).order_by(Course.id).all()

    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    if request.method == 'POST':

        newRecipe = Recipe(
            name=request.form['newRecipeName'],
            course_id=course_id
        )

        session.add(newRecipe)
        session.commit()

        addedRecipe = session.query(Recipe).filter_by(
            name=request.form['newRecipeName']).one()

        ingredients_line = request.form['newIngredients'].splitlines()

        for i in range(len(ingredients_line)):

            if ingredients_line[i]:

                newIngredient = Ingredients(
                    recipe_id=addedRecipe.id,
                    ingr_number=i + 1,
                    ingredient=ingredients_line[i]
                )

                session.add(newIngredient)
                session.commit()

        directions_line = request.form['newDirections'].splitlines()

        for i in range(len(directions_line)):

            if directions_line[i]:

                newDirection = Directions(
                    recipe_id=addedRecipe.id,
                    step_number=i + 1,
                    step=directions_line[i]
                )

                session.add(newDirection)
                session.commit()

        return redirect(url_for('viewRecipe',
                                course_id=course_id,
                                recipe_id=addedRecipe.id))

    else:
        return render_template('newRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=7070)
