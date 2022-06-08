from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Cats, Food

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
        test_food = Food(food="A whole pigeon")
        db.session.add(test_cat, test_food)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):  
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_cat(self):
        response = self.client.get(url_for('add_cat'))
        self.assertEqual(response.status_code, 200)     

    def test_add_food(self):
        response = self.client.get(url_for('add_food'))
        self.assertEqual(response.status_code, 200)

    def test_added(self):
        response = self.client.get(url_for('added'))
        self.assertEqual(response.status_code, 200)    


class TestAdd(TestBase):
    def test_add_cat(self):
        response=self.client.post(
            url_for('add_cat'), 
            data = dict(cat_name="Big Susan"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Big Susan', response.data)

    def test_add_food(self):
        response=self.client.post(
            url_for('add_food'),
            data = dict(food="Carrot")
        )
        self.assert200(response)
        self.assertIn(b'Carrot', response.data)

class TestDelete(TestBase):
    def test_delete_cat(self):
        url = str(url_for('delete')+"/0")
        response = self.client.delete(
            url,
            data = dict(cat_name='Jumbo-Puss, Pigeon Eater')
        )
        assert len(Cat.query.all()) == 0
#I don't think we have functionality to delete food actually??? #todo
    def test_delete_food(self):
        response = self.client.delete(
            url_for('delete_food'),
            data = dict(food="A whole pigeon")
        )
        assert len(Food.query.all()) == 0