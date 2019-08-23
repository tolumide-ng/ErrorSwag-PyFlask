import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.models.user_model import User
from src.models.blog_model import Blog
from src.models.follow_model import Follow


from src.app import create_app, db

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
