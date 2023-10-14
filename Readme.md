# Shopping Store Api 

# Introduction

A fully functional API backend for an online store built with Django and using Django-Rest-Framework for serving endpoints.


# Application specifications

- The user is able to register through an endpoint
- The user is able login through an endpoint after registering
- A user is able to see product list.
- A user is able to see product details
- View products reviews
- Add items to cart
- make orders
- Celery Workers for running background apps
- Redis for caching rarely updated but frequently accessed endpoints

# Environment Install.

Follow the steps below to make sure the application running in the correct way:

- Makes sure you have installed `Mysql`, `Redis`, `NodeJs`, `PM2` on your local machine before starting the application
- Otherwise, you should use `Docker Container` to host the application.

# Application install instructions.

- Run the command `pipenv install` to install all the application dependencies.
- Run the command `python manage.py makemigration` to create a database migration file.
- Run the command `python manage.py migrate` to run all the current database migration.
- Run the command `python manage.py runserver` to starting development the application.
- Run the command `pytest` to performs the all the test.

# Run the application in Docker Environment:

- Make sure your local machine has been installed the Docker container.
- Run the command `docker-compose up` to starting development the application.
- Run the command `docker-compose down` to stop development the application.
- Run the command `docker-compose up --build` to rebuild the application.
- Run the command `docker-compose up -d` to build the application in the background.
  Note\*: There are some other docker command need to hand on by your self.

# The APIs document has issued via Open API.

- Landing on `http://127.0.0.1:8000/store/documention` to open the Open API docs for local environment.