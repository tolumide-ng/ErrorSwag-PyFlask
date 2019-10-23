# ErrorSwag-PyFlask

[![Coverage Status](https://coveralls.io/repos/github/tolumide-ng/ErrorSwag-PyFlask/badge.svg?branch=staging)](https://coveralls.io/github/tolumide-ng/ErrorSwag-PyFlask?branch=staging) [![Build Status](https://travis-ci.com/tolumide-ng/ErrorSwag-PyFlask.svg?branch=staging)](https://travis-ci.com/tolumide-ng/ErrorSwag-PyFlask)

**https://forswagsanderrors.herokuapp.com/ is currently down as I am out of free apps on heroku** Please deploy the application using the the .env.sample

## About this Project:

ErroSwag Pyflask rebuilds the simulations backend application in python and flask

### Rebuilding the simulations backend project with python and flask

### Using ErroSwag

- Anyone can view blog posts on the application
- Authenticated users can follow one another
- Authenticated users can unfollowe one another
- Authenticated users can create blog posts, delete, or update there blogposts
- Authenticated users can view other users profiles, edit and delet there own features

### Working Routes

| Routes                                                                    | Purpose                            | Method |
| :------------------------------------------------------------------------ | :--------------------------------- | :----: |
| https://forswagsanderrors.herokuapp.com/api/v1/users                      | Singup on Errorswag                |  POST  |
| https://forswagsanderrors.herokuapp.com/api/v1/users                      | Get all users                      |  GET   |
| https://forswagsanderrors.herokuapp.com/api/v1/users/login                | Login to the application           |  POST  |
| https://forswagsanderrors.herokuapp.com/api/v1/users/<int: id>            | View secific user profile          |  GET   |
| https://forswagsanderrors.herokuapp.com/api/v1/users                      | Update your profile                |  PUT   |
| https://forswagsanderrors.herokuapp.com/api/v1/users/me                   | Delete your profile                | DELETE |
| https://forswagsanderrors.herokuapp.com/api/v1/users/me                   | View your profile                  |  GET   |
| https://forswagsanderrors.herokuapp.com/api/v1/blogs/                     | Create a blogpost                  |  POST  |
| https://forswagsanderrors.herokuapp.com/api/v1/blogs/                     | View all blogposts                 |  GET   |
| https://forswagsanderrors.herokuapp.com/api/v1/blogs/<int: id>            | View a specific blog post          |  GET   |
| https://forswagsanderrors.herokuapp.com/api/v1/blogs/<int: id>            | Edit a specfic blogpost            |  PUT   |
| https://forswagsanderrors.herokuapp.com/api/v1/blogs/<int: id>            | Delete a specific blogpost         | DELETE |
| https://forswagsanderrors.herokuapp.com/api/v1/socials/follow/<int: id>   | Follow a specific user             |  POST  |
| https://forswagsanderrors.herokuapp.com/api/v1/socials/unfollow/<int: id> | Unfollow a specific user           | DELETE |
| https://forswagsanderrors.herokuapp.com/api/v1/socials/followers          | View all your followers            |  GET   |
| https://forswagsanderrors.herokuapp.com/api/v1/socials/followings         | View users users you are following |  GET   |

Use python appp.run() to run this application

### Technologies used

- Python - [High level general purpose programming lanugauge](https://www.python.org/)
- Flask - [Popular extensible web microframework for building web applications with python](https://www.fullstackpython.com/flask.html)
- Pytest - [Framework for writing small python tests](https://docs.pytest.org/en/latest/)
- Unittest - [Unit testing Framework](https://docs.python.org/3/library/unittest.html)
- Bcrypt - [Encode user password before saving to the database](https://flask-bcrypt.readthedocs.io/en/latest/)
- Marshmallow - [ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes](https://marshmallow.readthedocs.io/en/stable/)
- SqlAlchemy - [Python SQL Toolkit and ORM](https://www.sqlalchemy.org/)

### Onboarding on this project

- Install all dependencies
- `flask db init` to initialize database
- `flask db migrate #title_of_db_migrations#` to run migrations
- `flask db upgrade` to upgrade the migrations
- `flask help` to view help options
- `flask run` to start the server
- `pytest --cov=src` to run tests that show coverage
