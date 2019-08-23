# ErrorSwag-PyFlask

Rebuilding the simulations backend project with python and flask

Use python appp.run() to run this application

Run Migrations initialization with `db.init` command:
`python manage.py db init`

`flask run` to start the server
`flask db migrate` to run migrations
`flask help` to view help options

To create a new migration:
create/update the model

- run flask db migrate '#title of migration#'
- run the migratin `flask db upgrade`
