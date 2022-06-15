from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Cats, Food, Food_Likes

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
        test_food = Food(food = "A carrot")
        test_cat = Cats(cat_name="Jumbo-Puss, Pigeon Eater", fav_food=1, approx_age=41)
        db.session.add_all([test_cat, test_food])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase):  
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

    def test_add_cat(self):
        response = self.client.get(url_for('add_cat'))
        self.assert200(response)       

    def test_likes(self):
        response = self.client.get(url_for('likes', id=1))
        self.assert200(response)   

    def test_added(self):
        response = self.client.get(url_for('added_cat'))
        self.assert200(response)

class TestAdd(TestBase):
    def test_add_cat(self):
        response=self.client.post(
            url_for('add_cat'), 
            data = dict(cat_name="Big Susan", fur_type = "Shorthair", approx_age=40, fav_food=1))
        self.assertEqual(response.status_code, 302)
        cat = Cats.query.filter_by(cat_name="Big Susan").first()
        assert cat.cat_id == 2

class TestDelete(TestBase):
    def test_delete_cat(self):
        response = self.client.get(
            url_for('delete', id=1))
        assert len(Cats.query.all()) == 0

class TestFoodLikes(TestBase):
    def test_cat_food_likes(self):
        repsonse = self.client.post(
            url_for('cat_liked_food', id = 1),
            data = dict(caul = True, pie = True, spid = True, chick = True, oink = True, pea = True, cake = True, cream = True))
        cat = Cats.query.first()
        list1 = Food_Likes.query.filter_by(cat_id=cat.cat_id).all()
        assert len(list1) == 8
        self.assertEqual(repsonse.status_code, 302)

        response = self.client.get(
            url_for('cat_liked_food', id = 1)
        )
        self.assert200(response)
        cat = Cats.query.first()
        list1 = Food_Likes.query.filter_by(cat_id=cat.cat_id).all()
        assert len(list1) == 0

class TestEditCat(TestBase):
    def test_cat_edit(self):
        response = self.client.get(
            url_for('edit_cat', id = 1)
        )
        self.assert200(response)    
        response = self.client.post(
            url_for('edit_cat', id = 1),
            data = dict(cat_name="Jumbo-Puss", fur_type = "Shorthair", fav_food=1, approx_age=40)
        )
        self.assertEqual(response.status_code, 302)
        cat = Cats.query.first()
        assert cat.cat_name == "Jumbo-Puss"
        assert cat.approx_age == 40