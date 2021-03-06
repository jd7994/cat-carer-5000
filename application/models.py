from application import db
from flask import Flask


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
    food = db.Column(db.String(30), nullable=False)
    cats_faves = db.relationship('Cats', backref='fav_foodbr')
    liked_by = db.relationship('Food_Likes', backref='foodbr')
    
class Food_Likes(db.Model):
    likes_id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column('cat_id', db.Integer, db.ForeignKey('cats.cat_id'))
    food_id = db.Column('food_id', db.Integer, db.ForeignKey('food.food_id'))

# class FoodForm(FlaskForm):
#     food = StringField("What is this food item?")
#     flavour_prof = SelectField("How would you say it tastes?", choices=[
#         ("Salty", "Salty"),
#         ("Sweet", "Sweet"),
#         ("Spicy", "Spicy"),
#         ("Acidic", "Acidic"),
#         ("Umami", "Umami"),
#         ("Disgusting!", "Disgusting!")
#     ])
#     stock = IntegerField("How many do you have?")
#     submit = SubmitField('Done!')