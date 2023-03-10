from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.user import User
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = User(name="vasya", surname='petrov', email='ruth@mail.ru', password="my_little_pony")
        u2 = User(name="ola", surname='ivanova', email='ivi@mail.ru', password="wassap")


app = create_app(Config())
app.debug = True

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=10001, debug=True)
