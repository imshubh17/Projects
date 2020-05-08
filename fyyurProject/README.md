Fyyur
-----

### Introduction

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues.


### Test the functionality of this project

To start and run the local development server,

1. Initialize and activate a virtualenv:
    ```
    $ virtualenv -p python3 venv
    ```
2. Install the dependencies:
    ```
    $ pip install -r requirements.txt
    ```

3. Make migrations:
    ```
    $ flask db migrate
    $ flask db upgrate
    ```

4. Run the development server:
    ```
    $ python3 app.py
    ```

5. Navigate to Home page 