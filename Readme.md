# Instagram Clone App


### Author
Bett kipkemoi

### instaclone project
An application where users can:
*   Sign up
*   Sign in (authentication)
*   Upload pictures
*   Follow other users and see their pictures
*   Like other users pictures
*   Comment on other users' pictures

## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: source virtual/bin/activate
* Install all the requirements found in requirements file.
* On your terminal run python3.8 manage.py runserver
* Access the live site using the local host provided
* Create your superuser account python manage.py createsuperuser inside virtual         environment.
* Add data from admin dashboard

# Getting started
### Prerequisites

* python3.6
* virtual environment
* pip
* postgresql
### Installing

Ensure that the MODE in the .env is set to development ('dev'), which will automatically set debug to true.

Now run the following command

```
python3.6 manage.py runserver
```

And view the site at the port provided which is most likely 127.0.0.1:8000

## Running the tests

To run the automated tests for this system, run the following command

```
python3.6 manage.py test instaclone
```
## Deployment

To deploy on heroku:
*   Have a Procfile in the project root;
*   Update requirements.txt file with all the requirements in the project root;
*   Have Gunicorn to requirements.txt;
*   Have runtime.txt to specify the correct Python version in the project root;
*   Ensure configuration whitenoise to serve static files.
*   Add a heroku remote by logging in
*   Configure all the settings in .env on heroku (set MODE to 'prod' on heroku)
*   git push to heroku
*   git push database and migrate to heroku server
## License

This project is licensed under the [MIT] License 