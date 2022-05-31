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
        return redurect(url_for('cat_liked_food'))
    return render_template('add_cat.html', all_cats = Cats.query.all())

@app.route('/add_food', methods=['GET', 'POST'])
def add_food():
   return render_template('add_food.html')


# @app.route('/new', methods=['GET', 'POST'])
# def new_item():
#     form = ItemForm()
#     if form.validate_on_submit():
#         item = Tasks(
#             task_name = form.task_name.data,
#             importance = form.importance.data,
#             est_completion = form.est_completion.data,
#             done = form.done.data            
#         )
#         db.session.add(item)
#         db.session.commit()
#         return redirect(url_for('home')) 
#     return render_template('new.html', form=form)   

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update_item(id):
#     task = Tasks.query.get(id)
#     form = ItemForm(
#         task_name = task.task_name,
#         importance = task.importance,
#         est_completion = task.est_completion,
#         done = task.done
#     )
#     if form.validate_on_submit():
#         item = Tasks.query.get(id)
#         item.task_name = form.task_name.data
#         item.importance = form.importance.data
#         item.est_completion = form.est_completion.data 
#         item.done = form.done.data

#         db.session.commit()
#         return redirect(url_for('/home')) 
#     return render_template('new.html', form=form)   

# @app.route('/delete/<int:id>', methods=['GET'])
# def delete_item(id): 
#     item = Tasks.query.get(id)
#     db.session.delete(item)    
#     db.session.commit() 
#     return render_template('delete.html', item=item)
