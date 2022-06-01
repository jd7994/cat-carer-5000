from application import db
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, IntegerField

class Cats(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20), nullable=False)
    fur_type = db.Column(db.String(20))
    fur_colour = db.Column(db.String(20))
    temprament = db.Column(db.String(20))
    approx_age = db.Column(db.Integer)
    fav_food = db.Column(db.Integer, db.ForeignKey('food.food_id'))
    liked_food = db.relationship('Food_Likes', backref='catsbr')
     
class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(20), nullable=False)
    flavour_prof = db.Column(db.String(20))
    stock = db.Column(db.Integer, default=0)
    cats_faves = db.relationship('Cats', backref='fav_foodbr')
    liked_by = db.relationship('Food_Likes', backref='foodbr')

class Food_Likes(db.Model):
    likes_id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column('cat_id', db.Integer, db.ForeignKey('cats.cat_id'))
    food_id = db.Column('food_id', db.Integer, db.ForeignKey('food.food_id'))


class CatForm(FlaskForm):
    cat_name = StringField('What is your new cat\'s name?')
    fur_type = SelectField('What type of fur do they have?', choices=[
        ("Shorthair", "Shorthair"),
        ("Longhair", "Longhair"), 
        ("Hairless", "Hairless")
    ])
    fur_colour = StringField('Fur Colour:')
    temprament = StringField('Typical Temprament:')
    approx_age = IntegerField('Approximate age:')
    fav_food = SelectField('Favourite food:', choices=[("Unknown", "Unknown")]) #we have to populate this using a for loop and then form.fav_food.choices.append
    #liked_food will be a seperate page
    submit = SubmitField('Done!')

class FoodForm(FlaskForm):
    food = StringField("What is this food item?")
    flavour_prof = SelectField("How would you say it tastes?", choices=[
        ("Salty", "Salty"),
        ("Sweet", "Sweet"),
        ("Spicy", "Spicy"),
        ("Acidic", "Acidic"),
        ("Umami", "Umami"),
        ("Disgusting!", "Disgusting!")
    ])
    stock = IntegerField("How many do you have?")
    submit = SubmitField('Done!')

class Food_likes_form(FlaskForm):
    all_food = list(Food.query.all())
    for food in all_food:
        locals()[food.food] = BooleanField(food.food)
    submit = SubmitField("Finished!")
    
