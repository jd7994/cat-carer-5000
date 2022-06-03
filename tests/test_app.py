from flask import url_for
from flask_testing import TestCase

from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

def setUp(self):
    db.create_all()
    test_cat = Cats(cat_name="Jumbo-Puss, Pigeon Eater")
    #test_food = Food(food="A whole pigeon")
    db.session.add(test_cat, test_food)
    db.session.commit()

def tearDown(self):
    db.session.remove()
    db.drop_all()
#this isn't working, try the formatting from the examples on community
class TestView(TestBase):  
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        

#     def test_add_cat(self):
#         response = self.client.get(url_for('add_cat'))
#         self.assertEqual(response.status_code, 200)
    
#     def test_add_food(self):
#         response = self.client.get(url_for('add_food'))
#         self.assertEqual(response.status_code, 200)

#     def test_added(self):
#         response = self.client.get(url_for('added'))
#         self.assertEqual(response.status_code, 200)    

#     def test_added_cat(self):
#         response = self.client.get(url_for('added_cat'))
#         self.assertEqual(response.status_code, 200)

#     def test_cat_liked_food(self):
#         url = url_for(cat_liked_food)
#         response = self.client.get(url + "/0")
#         self.assertEqual(response.status_code, 200)

#     def test_edit_cat(self):
#         response = self.client.get(url_for('edit_cat') + "/0")
#         self.assertEqual(response.status_code, 200)

#     def test_delete_cat(self):
#         response = self.client.get(url_for('delete_cat') + "/0")
#         self.assertEqual(response.status_code, 200)

#     def test_edit_cat(self):
#         response = self.client.get(url_for('edit_cat') + "/0")
#         self.assertEqual(response.status_code, 200)
#     #todo: instigate cat_liked_food with id, foods instantiated
#     # delete_cat with id
#     #edit_cat with id
class TestAdd(TestBase):
    def test_add_cat(self):
        response=self.client.post(
            url_for('add_cat'), 
            data = dict(cat_name="Big Susan"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Big Susan', response.data)

#     def test_add_food(self):
#         response=self.client.post(
#             url_for('add_food'),
#             data = dict(food="Carrot")
#         )
#         assert Food.query.filter_by(food="Carrot").id == 2

# class TestDelete(TestBase):
#     def test_delete_cat(self):
#         response = self.client.delete(
#             url_for('delete_cat'),
#             data = dict(cat_name='Jumbo-Puss, Pigeon Eater')
#         )
#         assert len(Cat.query.all()) == 0
    
#     def test_delete_food(self):
#         response = self.client.delete(
#             url_for('delete_food'),
#             data = dict(food="A whole pigeon")
#         )
#         assert len(Food.query.all()) == 0