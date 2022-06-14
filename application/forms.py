from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, IntegerField

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
    submit = SubmitField('Done!')