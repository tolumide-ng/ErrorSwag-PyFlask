# src/models/__init__.py

# from .follow_model import Follow, FollowSchema
# from .blog_model import Blog, BlogSchema
# from .user_model import User, UserSchema
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()
