from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Course, Recipe, Ingredients, Directions, Base

engine = create_engine('sqlite:///healthyRecipes.db')

DBSession = sessionmaker(bind=engine)
session = DBSession()

# -------------------------------- #
#         Add all Courses          #
# -------------------------------- #

# Add Soup to courses
soup = Course(
    id='1',
    name='Soup'
    )

session.add(soup)
session.commit()

# Add Side Dish to courses
side_dish = Course(
    id="2",
    name="Side Dish"
    )
session.add(side_dish)
session.commit()

# Add Appetizer to courses
appetizer = Course(
    id="3",
    name="Appetizer"
    )
session.add(appetizer)
session.commit()

# Add Dessert to courses
dessert = Course(
    id="4",
    name="Dessert"
    )
session.add(dessert)
session.commit()

# Add Breakfast to courses
breakfast = Course(
    id="5",
    name="Breakfast"
    )
session.add(breakfast)
session.commit()

# Add Main Dish to courses
main_dish = Course(
    id="6",
    name="Main Dish"
    )
session.add(main_dish)
session.commit()

# Add Brunch to courses
brunch = Course(
    id="7",
    name="Brunch"
    )
session.add(brunch)
session.commit()

# Add Smoothie to courses
smoothie = Course(
    id="8",
    name="Smoothie"
    )
session.add(smoothie)
session.commit()

# Add Salad to courses
salad = Course(
    id="9",
    name="Salad"
    )
session.add(salad)
session.commit()

print ("All Courses were added successfully!")

# ----------------------------------------------------------------------------#
#                              Add Soup Recipes                               #
# ----------------------------------------------------------------------------#

# ------------------------------------------------------- #
#         Crushed Lentil Soup with Lamb Meatballs         #
# ------------------------------------------------------- #

lentil_soup = Recipe(
    id='1',
    name='Crushed Lentil Soup with Lamb Meatballs',
    image="",
    course_id=soup.id,
    course=soup
    )

session.add(lentil_soup)
session.commit()
