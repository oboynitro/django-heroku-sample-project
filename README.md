### Set up

+ clone the repo with git clone https://github.com/oboynitro/django-heroku-sample-project.git

+ you can rename the project folder to your site name

+ create a virtual environment
	+ `$ virtualenv venv`

+ activate virtual environment and install the requirements file packages
	+ `$ source venv/bin/activate` # for linux users
	+ `$ source venv\Scripts\activate` # for windows users with git bash
	+ `$ venv\Scripts\activate` # for windows users with command line

	+ `$ pip install -r requirements.txt` # for windows 
	+ `$ pip3 install -r requirements.txt` # for mac and linux

+ install [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli "heroku-cli")

+ run heroku login

+ create new app on heroku from the browser or from the command line using heroku-cli
	+ `$ heroku create my-app`

+ add your remote heroku app to your local git
	+ `$ heroku git:remote -a my-app`

+ edit your Procfile and change 'django_heroku_sample_project' to your heroku app name 'my-ap'

+ edit your runtime.txt file and change the python version as per your environment
	+ `$ python -V` # to check your python version. remember to activate your virtual environment first

+ push your app to heroku
	+ `$ git push heroku main`