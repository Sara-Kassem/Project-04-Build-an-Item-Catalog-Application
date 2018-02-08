import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)


class Recipe(Base):
    __tablename__ = 'recipe'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    image = Column(String)
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship('Course')


class Ingredients(Base):
    __tablename__ = 'ingredients'

    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    ingr_id = Column(Integer, primary_key=True)
    ingredient = Column(String)


class Directions(Base):
    __tablename__ = 'directions'

    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    step_id = Column(Integer, primary_key=True)
    step = Column(String)


engine = create_engine('sqlite:///healthyRecipes.db')

Base.metadata.create_all(engine)

print ("Database Created!!")
