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
  ├── category.py *** Before run app.py run this script
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

3. Run the development server:

  ```
  Create Migration 
    $  flask db init

  You can then generate an initial migration
    $ flask db migrate -m "Initial migration."

  Then you can apply the migration to the database:
    $ flask db upgrade
  ```
4. insert data into todolist table for Category.
    ```
    $ python category.py 
    for Default Category and create own category change catname inside category.py then run
    ```

5. Run Application:
  ```
  $ python app.py
  ```


# Deployment In Heroku
*** Important "Procfile" file
#### Steps
1. create account
   https://id.heroku.com/login 

2. create application in heroku 

4. Create database and click copy connection link and paste inside app.py for database connectivity

3. Upload project in github 


4. In heroku click on deployment inside application and select option  deploy with github then connect repo and deploy 

5. Use commandline interface of heroku for migration and run category.py for default category

6. finally Application will deploy click on URL and open application and Add your ToDo Task
