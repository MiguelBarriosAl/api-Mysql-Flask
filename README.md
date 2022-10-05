<h1 align="center"> Origen.ai - Api Service </h1>

# Table of Contents
- [Introduction](#Introduction)
- [Motivation](#Motivation)
- [Requirements](#Requirements)
- [Installation](#Installation)
- [Run](#Run)
- [Api_rest](#Api Rest)

# Introduction
Backend project in which Api service has been integrated with Flask in which database information can be accessed through Api Rest client requests.

- Total registered executions
- List existing Simulation runs, including those with pending status (waiting to be scheduled into a machine), running (already being allocated to a machine and being currently run) and finished (run completed).

- Filter the list of Simulations by status (pending, running, and finished`).

- Order the list by name, creation date or update date.

- List Machines in wich simulations can be run. Machines are pre-registered in database as fixtures.

- Create a new Simulation by specifying its name and the Machine in which he'd like to schedule it.

- Click on an element in the list to see detailed information about the Simulation.

- The detail view may include a convergence graph showing how the Simulation run converged or is converging if the status is running. In the latter case, the UI may pool the backend every few seconds to re-draw the graph with further information.

# Motivation
For this project I wanted to integrate the [Flask](https://flask.palletsprojects.com/en/2.2.x/) framework with Sqlite to develop Api Rest in which you could store the data and make searches.
On the other hand, I have considered Sqlite for testing since it is a less powerful database engine than others such as mysql or PostgreSql, it is sufficient for testing.


# Requirements
- Pip == 22.2.2
- Python == 3.10.7
- Flask==2.2.2
- Flask-SQLAlchemy==2.5.1
- SQLAlchemy==1.4.41

# Middleware
To be able to access with authorization to the requests, you must create a file with environment variable .env , which includes the following fields

- USER_MIDDLEWARE= 'Miguel'
- PASS_MIDDLEWARE = 'Barrios'

In my case add the values Miguel and Barrios
# Installation
- Install python==3.10.7

        sudo apt update

        sudo apt install python3.10

        python --version

- Clone the repository

        git clone https://github.com/MiguelBarriosAlvarez/Api-Mysql-Flask.git

- Install virtual enviroment: 

        sudo apt-get install python3-pip

        sudo pip3 install virtualenv

        virtualenv venv

        source venv/bin/activate

- Install requirements

        pip install -r requirements.txt

# Run 
## Create Database
In order to be able to make the Request in Flask, the Database have to be created of the next way: 
If the database is not created, the following command must be executed:

`python3 models.py`

Test data will be included to test the application.
For production it should be integrated with the service that is dedicated to ingest data.
As I comment before, I have considered Sqlite for testing since it is a less powerful database engine than others such as mysql or PostgreSql, it is sufficient for testing.
## Flask

    cd \Api-Mysql-Flask
    python3 app.py

# Api Rest
In this section I show some examples to be able to make requests to the API:


### Count Data

    curl -u Miguel:Barrios http://localhost:5000/count


### Order By created_at

    curl -u Miguel:Barrios -X GET http://localhost:5000/order_by/"created_at"


### Insert Data

    curl -u Miguel:Barrios -X POST http://localhost:5000/insert -H "Content-Type: application/json" -d '{"id": 12, "state": "pending", "fixture": "fixtures_010rth"}'


### Check id Simulations per State


    curl -u Miguel:Barrios -X GET http://localhost:5000/state -H "Content-Type: application/json" -d '{"state": "finished"}'


### Get a Loss Graph
Through this request we can modify the value of a field of our choice, selecting the recipe by its name

    curl -u Miguel:Barrios -X GET http://localhost:5000/graph -H "Content-Type: application/json" -d '{"id": 3}'


