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

# ------------------------------------------------------- #
#   Crushed Lentil Soup with Lamb Meatballs Ingredients   #
# ------------------------------------------------------- #

ingredient001 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='1',
    ingredient='crushed Lentil Soup'
    )

session.add(ingredient001)
session.commit()

ingredient002 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='2',
    ingredient='2T. extra virgin Olive oil'
    )

session.add(ingredient002)
session.commit()

ingredient003 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='3',
    ingredient='1 lg. yellow onion, diced (about 2 cups)'
    )

session.add(ingredient003)
session.commit()

ingredient004 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='4',
    ingredient='1 lg. carrot, diced (about 1/2 cup)'
    )

session.add(ingredient004)
session.commit()

ingredient005 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='5',
    ingredient='1 celery stalk, diced (about 1/2 cup)'
    )

session.add(ingredient005)
session.commit()

ingredient006 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='6',
    ingredient='5 garlic cloves, minced'
    )

session.add(ingredient006)
session.commit()

ingredient007 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='7',
    ingredient='3 fresh bay leaves'
    )

session.add(ingredient007)
session.commit()

ingredient008 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='8',
    ingredient='1/2 c. red split lentils'
    )

session.add(ingredient008)
session.commit()

ingredient009 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='9',
    ingredient='1/2 c. brown rice'
    )

session.add(ingredient009)
session.commit()

ingredient010 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='10',
    ingredient='2 1/2 tsp. curry powder'
    )

session.add(ingredient010)
session.commit()

ingredient011 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='11',
    ingredient='1 1/2 tsp. sea salt'
    )

session.add(ingredient011)
session.commit()

ingredient012 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='12',
    ingredient='1/4 tsp. crushed red pepper'
    )

session.add(ingredient012)
session.commit()

ingredient013 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='13',
    ingredient='1/2 tsp. black pepper'
    )

session.add(ingredient013)
session.commit()

ingredient014 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='14',
    ingredient='7 c. vegetable broth, divided'
    )

session.add(ingredient014)
session.commit()

ingredient015 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='15',
    ingredient='Lamb Meatballs'
    )

session.add(ingredient015)
session.commit()

ingredient016 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='16',
    ingredient='3 T. olive oil'
    )

session.add(ingredient016)
session.commit()

ingredient017 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='17',
    ingredient='2 slices Udis Whole Grain Gluten Free Bread, crumbled'
    )

session.add(ingredient017)
session.commit()

ingredient018 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='18',
    ingredient='1/4 c. organic whole milk'
    )

session.add(ingredient018)
session.commit()

ingredient019 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='19',
    ingredient='1 lb. grassfed ground lamb'
    )

session.add(ingredient019)
session.commit()

ingredient020 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='20',
    ingredient='1 c. slivered and toasted almonds, chopped'
    )

session.add(ingredient020)
session.commit()

ingredient021 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='21',
    ingredient='1 smallish yellow onion (about &frac13; cup)'
    )

session.add(ingredient021)
session.commit()

ingredient022 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='22',
    ingredient='1/3 c. golden raisins, chopped'
    )

session.add(ingredient022)
session.commit()

ingredient023 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='23',
    ingredient='1 beaten egg'
    )

session.add(ingredient023)
session.commit()

ingredient024 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='24',
    ingredient='3 garlic cloves, minced'
    )

session.add(ingredient024)
session.commit()

ingredient025 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='25',
    ingredient='2 T. fresh chopped parsley'
    )

session.add(ingredient025)
session.commit()

ingredient026 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='26',
    ingredient='1 T. fresh chopped cilantro'
    )

session.add(ingredient026)
session.commit()

ingredient027 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='27',
    ingredient='1 tsp. kosher salt'
    )

session.add(ingredient027)
session.commit()

ingredient028 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='28',
    ingredient='Yogurt Sauce'
    )

session.add(ingredient028)
session.commit()

ingredient029 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='29',
    ingredient='1 c. organic plain yogurt'
    )

session.add(ingredient029)
session.commit()

ingredient030 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='30',
    ingredient='1 T. chopped mint'
    )

session.add(ingredient030)
session.commit()

ingredient031 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='31',
    ingredient='1/2 tsp. lemon zest'
    )

session.add(ingredient031)
session.commit()

ingredient032 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='32',
    ingredient='1/2 tsp. lemon juice'
    )

session.add(ingredient032)
session.commit()

ingredient033 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='33',
    ingredient='1 tsp. honey (optional since I gave up sugar)'
    )

session.add(ingredient033)
session.commit()

ingredient034 = Ingredients(
    recipe_id=recipe001.id,
    ingr_id='34',
    ingredient='Pinch of salt'
    )

session.add(ingredient034)
session.commit()
