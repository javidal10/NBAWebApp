# NBAWebApp
This repo contains a web application that obtains the heights in inches of the NBA players  by querying the Endpoint
[Mac Eight](https://mach-eight.uc.r.appspot.com/). it ask the user to enter the add up of two players height in inches


## Setup &nbsp; [![pyVersion37](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-397/)

- Set up and activate the local development environment.


- Install the requirements using pip:

    ```sh
    pip install -r requirements.txt
    ```

- Setup local MySql database and use django migrations 

    ```sh
    python NBA/manage.py makemigrations
    python NBA/manage.py migrate
    # This will setup the local database based on django models. Make sure you are in the same directory as manage.py file
    ```
- Fetch and store information manually by going to endpoint below an click on PUT

    http://127.0.0.1:8000/player


- Run the server as follows:

    ```sh
    python Nba/manage.py runserver
    ```

- If your development server is at localhost then you can access the api by using:

http://127.0.0.1:8000/player


