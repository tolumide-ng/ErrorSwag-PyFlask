# src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt

# import user_api, blog_api, follow_api blueprint
from .views.user_view import user_api as user_blueprint
from .views.blog_view import blog_api as blog_blueprint
from .views.follow_view import follow_api as follow_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initialization
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    # initializing bcrypt and db
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users/')
    app.register_blueprint(blog_blueprint, url_prefix='/api/v1/blogs/')
    app.register_blueprint(follow_blueprint, url_prefix='/api/v1/socials/')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Welcome to Errorswag.py.fl'

    return app
