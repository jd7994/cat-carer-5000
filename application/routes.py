from application import app, db
from application.models import Cats, CatForm
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
   return render_template('home.html', len = len, all_cats = Cats.query.all())

@app.route('/add_cat', methods=['GET', 'POST'])
def add_cat():
    form = CatForm()
    if form.validate_on_submit(): # populating food choices with what is in the food database
        foods = Food.query.all()
        for food in foods:
            form.fav_food.choices.append(
                food.id, f"{food.food}"
            )
        cat = Cats(
           cat_name = form.cat_name.data,
           fur_type = form.fur_type.data,
           fur_colour = form.fur_colour.data,
           temprament = form.temprament.data,
           approx_age = form.approx_age.data,
           fav_food = form.fav_food.data
        )
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('cat_liked_food'))
    return render_template('add_cat.html', all_cats = Cats.query.all())

@app.route('/add_food', methods=['GET', 'POST'])
def add_food():
    form = FoodForm()
    if form.validate_on_submit():
        food = Food(
            food = form.food.data,
            flavour_prof = form.flavour_prof.data,
            stock = form.stock.data
        )
   return render_template('add_food.html')

@app.route('/added', methods=['GET'])
def added():
   return render_template('added.html')

@app.route('/cat_liked_food/<int:id>', methods=['GET', 'POST'])
def cat_liked_food(id):
    form = Food_likes_form()
    cat = Cats.query.get(id)
    all_food = Food.query.all()
    fields = []
    for food in all_food:
        fields.append(locals()[food])
    cat_choices = []
    if form.validate_on_submit():
        for food in all_food:
            if form.(locals()[food]).data == True
                cat_choices.append(food.id)

        for choice in cat_choices:
            new_like = Food_Likes(
            Food_Likes.cat_id = cat.cat_id
            Food_likes.food_id = cat_choices
            )
            db.session.add(new_like)
        db.session.commit()
        cat_choices = []
        return redirect(url_for_('home'))
   
   return render_template('cat_food.html', fields)
