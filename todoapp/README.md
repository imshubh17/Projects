TodoApp
-----
### Introduction
Todo app use to create task in different category and delete after completion.

### Overview

you should have a fully functioning site that is at least capable of doing the following, if not more, using a PostgreSQL database:

* creating new Task.
* checklist to complete.
* delete after completion.

### Tech Stack

Our tech stack will include:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
* **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend

 ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependences
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ├── static
  │   ├── css 
  └── templates
      ├── index.html
  ```
### Setup
1. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```
2. setup your database:
  ```
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/databaseName'
  ```
  in app.py file.

3. migrate && upgrade database:

  ```
  You can then generate an initial migration
    $ flask db migrate -m "Initial migration."

  Then you can apply the migration to the database:
    $ flask db upgrade
  ```
4. insert data into todolist table.

5. Run the development server:
  ```
  $ python app.py
  ```
![Home page](https://github.com/imshubh17/Projects/blob/master/images/todoapp.PNG?raw=true "TodoApp")

#### Extra activity
Install Flask-Migrate with pip:
pip install Flask-Migrate

With the above application you can create a migration repository with the following command:
$ flask db init

You can then generate an initial migration
$ flask db migrate -m "Initial migration."

Then you can apply the migration to the database:
$ flask db upgrade