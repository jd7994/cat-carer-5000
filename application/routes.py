from application import app, db
from application.models import Cats,  Food, Food_Likes
from application.forms import CatForm, Food_Likes_Form
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
    foods = Food.query.all()
    for food in foods:
        form.fav_food.choices.append(
            (food.food_id, f"{food.food}")
        )
    if form.validate_on_submit(): # populating food choices with what is in the food database
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
        return redirect('cat_liked_food/' + str(cat.cat_id))
    return render_template('add_cat.html', form = form, all_cats = Cats.query.all())

# @app.route('/add_food', methods=['GET', 'POST'])
# def add_food():
#     form = FoodForm()
#     if form.validate_on_submit():
#         food = Food(
#             food = form.food.data,
#             flavour_prof = form.flavour_prof.data,
#             stock = form.stock.data
#         )
#         db.session.add(food)
#         db.session.commit()
#         return redirect(url_for('added'))
#     return render_template('add_food.html', form = form)

@app.route('/added', methods=['GET'])
def added():
    return render_template('added.html')

@app.route('/cat_liked_food/<int:id>', methods=['GET', 'POST'])
def cat_liked_food(id):
    form = Food_Likes_Form()
    prev_likes = Food_Likes.query.filter_by(cat_id=id).all()
    for likes in prev_likes:
        db.session.delete(likes)
    db.session.commit()
    cat = Cats.query.get(id)
    all_food = Food.query.all()
    cat_choices = []
    if form.validate_on_submit():
        if (form.caul.data):
            cat_choices.append(1)
        if (form.pie.data):
            cat_choices.append(2)
        if (form.spid.data):
            cat_choices.append(3)
        if (form.chick.data):
            cat_choices.append(4)
        if (form.oink.data):
            cat_choices.append(5)
        if (form.pea.data):
            cat_choices.append(6)
        if (form.cake.data):
            cat_choices.append(7)
        if (form.cream.data):
            cat_choices.append(8)    
        for choice in cat_choices:
            new_like = Food_Likes(
                cat_id = cat.cat_id,
                food_id = choice
            )
            db.session.add(new_like)
        db.session.commit()    
        return render_template('added_cat.html')
    return render_template('cat_liked_food.html', form = form) 

@app.route('/delete_cat/<int:id>', methods=['GET'])
def delete(id):
    cat_to_delete = Cats.query.get(id)
    db.session.delete(cat_to_delete)
    db.session.commit()
    return render_template('delete_cat.html')

@app.route('/edit_cat/<int:id>', methods=['GET', 'POST'])
def edit_cat(id):
    cat = Cats.query.get(id)
    form = CatForm(
        cat_name = cat.cat_name,
        fur_type = cat.fur_type,
        fur_colour = cat.fur_colour,
        temprament = cat.temprament,
        approx_age = cat.approx_age,
        fav_food = cat.fav_food
    )
    foods = Food.query.all()
    for food in foods:
        form.fav_food.choices.append(
            (food.food_id, f"{food.food}")
        )
    if form.validate_on_submit():
        cat.cat_name = form.cat_name.data
        cat.fur_type = form.fur_type.data
        cat.fur_colour = form.fur_colour.data
        cat.temprament = form.temprament.data
        cat.approx_age = form.approx_age.data
        cat.fav_food = form.fav_food.data

        db.session.commit()
        return render_template('added_cat.html')
    return render_template('add_cat.html', form=form)   

@app.route('/likes/<int:id>', methods=['GET'])
def likes(id):
    cat = Cats.query.get(id)
    likes = []
    list = Food_Likes.query.filter_by(cat_id=id).all()
    for item in list:
        likes.append(item.foodbr.food)
    return render_template('likes.html', likes = likes, cat = cat)