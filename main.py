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

# --------------------------------------------------------------------------- #
#      Set the number of recipes to be shown in the latest recipes secion     #
# --------------------------------------------------------------------------- #

latestRecipesLimit = 3


# --------------------------------------------------------------------------- #
#                                 Home Page                                   #
# --------------------------------------------------------------------------- #
@app.route('/')
@app.route('/healthy-recipes')
def homePage():

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the latest added recipes
    latestRecipes = session.query(Recipe).order_by(
        Recipe.id.desc()).limit(latestRecipesLimit)

    # Load index.html
    return render_template('index.html',
                           all_courses=all_courses,
                           latestRecipes=latestRecipes
                           )


# --------------------------------------------------------------------------- #
#                         All Recipes in a course                             #
# --------------------------------------------------------------------------- #
@app.route('/course/<int:course_id>/')
@app.route('/course/<int:course_id>/recipes')
def courseRecipes(course_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with id from the database
    course = session.query(Course).filter_by(id=course_id).one()

    # Get all recipes in the selected courses
    courseRecipes = session.query(Recipe).order_by(Recipe.name).filter_by(
        course_id=course_id).all()

    # Load a page with all recipes in the course
    return render_template('courseRecipes.html',
                           all_courses=all_courses,
                           courseRecipes=courseRecipes,
                           course=course)


# --------------------------------------------------------------------------- #
#                           View a recipe details                             #
# --------------------------------------------------------------------------- #
@app.route('/course/<int:course_id>/recipes/<int:recipe_id>')
def viewRecipe(course_id, recipe_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with the specified ID
    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    # Get the recipe with the specified ID
    viewRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    # Get all the ingredients of the recipe
    ingredients = session.query(Ingredients).filter_by(
        recipe_id=recipe_id).all()

    # Get all the directions of the recipe
    directions = session.query(Directions).filter_by(recipe_id=recipe_id).all()

    # Load a page with the recipe details
    return render_template('viewRecipe.html',
                           all_courses=all_courses,
                           viewRecipe=viewRecipe,
                           recipeCourse=recipeCourse,
                           ingredients=ingredients,
                           directions=directions
                           )


# --------------------------------------------------------------------------- #
#                             Delete a Recipe                                 #
# --------------------------------------------------------------------------- #
@app.route('/course/<int:course_id>/recipes/<int:recipe_id>/delete',
           methods=['GET', 'POST'])
def deleteRecipe(course_id, recipe_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with the specified ID
    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    # Get the recipe with the specified ID
    deleteRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    # if the request method is POST, perform actions to the database
    if request.method == 'POST':

        # delete the selected recipe from database
        session.delete(deleteRecipe)
        session.commit()

        # redirect to all recipes in the course after deleting
        return redirect(url_for('courseRecipes',
                                course_id=recipeCourse.id))

    # else, load deleteRecipe.html
    else:
        return render_template('deleteRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse,
                               deleteRecipe=deleteRecipe
                               )


# --------------------------------------------------------------------------- #
#                               Edit a Recipe                                 #
# --------------------------------------------------------------------------- #
@app.route('/course/<int:course_id>/recipes/<int:recipe_id>/edit',
           methods=['GET', 'POST'])
def editRecipe(course_id, recipe_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with the specified ID
    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    # Get the recipe with the specified ID
    editRecipe = session.query(Recipe).filter_by(id=recipe_id).one()

    # Get all the ingredients of the recipe
    ingredients = session.query(Ingredients).filter_by(
        recipe_id=recipe_id).all()

    # Get all the directions of the recipe
    directions = session.query(Directions).filter_by(
        recipe_id=recipe_id).all()

    # if the request method is POST, perform actions to the database
    if request.method == 'POST':

        # update recipe name with the new one given in the form if provided
        if request.form['updateName']:
            editRecipe.name = request.form['updateName']

        # update recipe course with the new one given in the form if provided
        if request.form['updateCourse']:
            updateCourse = session.query(Course).filter_by(
                name=request.form['updateCourse']).one()
            editRecipe.course_id = updateCourse.id

        # update the database with the changes
        session.add(editRecipe)
        session.commit()

        # delete all current ingredients
        for i in ingredients:
            session.delete(i)
            session.commit()

        # store each line in ingredients input as an element of a list
        ingredients_line = request.form['updateIngredients'].splitlines()

        # iterate through new ingredients (the list) one by one
        for i in range(len(ingredients_line)):

            # if the current line isn't blank, process the code inside
            if ingredients_line[i]:

                # create a new instance of Ingredients with the input data
                newIngredient = Ingredients(
                    recipe_id=recipe_id,
                    ingr_number=i + 1,
                    ingredient=ingredients_line[i]
                )

                # add the new ingredient to the database
                session.add(newIngredient)
                session.commit()

        # delete all current directions
        for i in directions:
            session.delete(i)
            session.commit()

        # store each line in directions input as an element of a list
        directions_line = request.form['updateDirections'].splitlines()

        # iterate through new directions (the list) one by one
        for i in range(len(directions_line)):

            # if the current line isn't blank, process the code inside
            if directions_line[i]:

                # create a new instance of Directions with the input data
                newDirection = Directions(
                    recipe_id=recipe_id,
                    step_number=i + 1,
                    step=directions_line[i]
                )

                # add the new step to the database
                session.add(newDirection)
                session.commit()

        # after updating all the changes, redirect to the selected recipe page
        return redirect(url_for('viewRecipe',
                                course_id=recipeCourse.id,
                                recipe_id=editRecipe.id))

    # else, load editRecipe.html
    else:
        return render_template('editRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse,
                               editRecipe=editRecipe,
                               ingredients=ingredients,
                               directions=directions
                               )


# --------------------------------------------------------------------------- #
#                             Add a New Recipe                                #
# --------------------------------------------------------------------------- #
@app.route('/course/<int:course_id>/recipes/new', methods=['GET', 'POST'])
def newRecipe(course_id):

    # Get all courses in the database
    all_courses = session.query(Course).order_by(Course.id).all()

    # Get the course with the specified ID
    recipeCourse = session.query(Course).filter_by(id=course_id).one()

    # if the request method is POST, perform actions to the database
    if request.method == 'POST':

        # create a new instance of Recipe with the input data
        newRecipe = Recipe(
            name=request.form['newRecipeName'],
            course_id=course_id
        )

        # add the new recipe to the database
        session.add(newRecipe)
        session.commit()

        # get the added recipe from the database
        addedRecipe = session.query(Recipe).filter_by(
            name=request.form['newRecipeName']).one()

        # store each line in ingredients input as an element of a list
        ingredients_line = request.form['newIngredients'].splitlines()

        # iterate through new ingredients (the list) one by one
        for i in range(len(ingredients_line)):

            # if the current line isn't blank, process the code inside
            if ingredients_line[i]:

                # create a new instance of ingredients with the input data
                newIngredient = Ingredients(
                    recipe_id=addedRecipe.id,
                    ingr_number=i + 1,
                    ingredient=ingredients_line[i]
                )

                # add the new ingredient to the database
                session.add(newIngredient)
                session.commit()

        # store each line in directions input as an element of a list
        directions_line = request.form['newDirections'].splitlines()

        # iterate through new directions (the list) one by one
        for i in range(len(directions_line)):

            # if the current line isn't blank, process the code inside
            if directions_line[i]:

                # create a new instance of Directions with the input data
                newDirection = Directions(
                    recipe_id=addedRecipe.id,
                    step_number=i + 1,
                    step=directions_line[i]
                )

                # add the new step to the database
                session.add(newDirection)
                session.commit()

        # after adding the new recipe, redirect to its page
        return redirect(url_for('viewRecipe',
                                course_id=course_id,
                                recipe_id=addedRecipe.id))

    # else, load newRecipe.html
    else:
        return render_template('newRecipe.html',
                               all_courses=all_courses,
                               recipeCourse=recipeCourse)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=7070)
