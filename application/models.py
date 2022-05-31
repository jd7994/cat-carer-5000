from application import db
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, SelectField, BooleanField

class Cats(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20), nullable=False)
    fur_type = db.Column(db.String(20))
    fur_colour = db.Column(db.String(20))
    temprament = db.Column(db.String(20))
    approx_age = db.Column(db.Integer)
    fav_food = db.Column(db.Integer, db.ForeignKey('Food.food_id'))
    liked_food = db.relationship('Food_Likes', backref='catsbr')
    
class Food_Likes(db.Model):
     likes_id = db.Column(db.Integer, primary_key=True)
     cat_id = db.Column('cat_id', db.Integer, db.ForeignKey('cat_id'))
     food_id = db.Column('food_id', db.Integer, db.ForeignKey('food_id'))
     
class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(20), nullable=False)
    flavour_prof = db.Column(db.String(20))
    stock = db.Column(db.Integer, default=0)
    cats_faves = db.relationship('Cats', backref='fav_foodbr')
    liked_by = db.relationship('Food_Likes', backref='foodbr')



#class ItemForm(FlaskForm):
#    task_name = StringField('Task Name:')
#    importance = SelectField('Importance:', choices=[
#        ("Very Important", "Very Important"),
#        ("Important", "Important"),
#        ("Quite Important", "Quite Important"),
#        ("Not So Important", "Not So Important")
#    ])
#    est_completion = StringField('When do we hope this will be done?')
#    done = BooleanField('Check when completed!')
#    submit = SubmitField('Submit Task!')




