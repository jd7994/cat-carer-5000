from application import app, db
from application.models import Tasks, ItemForm
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
#def home():
 #   return render_template('home.html', len = len, list_items = Tasks.query.all(), list_var = ["Very Important", "Important", "Quite Important", "Not So Important"])


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
