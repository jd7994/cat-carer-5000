from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, IntegerField
from models import Food
from app import app, db

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
    fav_food = SelectField('Favourite food:', choices=[]) #we have to populate this using a for loop and then form.fav_food.choices.append
    submit = SubmitField('Done, let\'s go to more food!')

class Food_Likes_Form(FlaskForm):
    caul = BooleanField("A Raw Cauliflower")
    pie = BooleanField("A Freshly Baked Pie")
    spid = BooleanField("A Live, Wriggling Spider")
    chick = BooleanField("An Entire Roast Chicken")
    oink = BooleanField("Bacon, Cooked or Raw")
    pea = BooleanField("Frozen Peas")
    cake = BooleanField("A Victoria Sponge")
    cream = BooleanField("Fresh Cream")
    submit = SubmitField('Finished!')
#     all_food = list(Food.query.all())
#     for food in all_food:
#         locals()[food.food] = BooleanField(food.food)
#     submit = SubmitField("Finished!")