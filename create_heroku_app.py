1. create virtual environment
pip iinstall virtualenv
virtualenv env1 #env1 is the name of the environment

2. activate virtual environment
source env1/bin/activate

3. requirements.txt
try to run app.py (python app.py)
see what's module is missing
pip install it, until successfully run app.py
pip freeze > requirements.txt

4. gunicorn part
pip install gunicorn
python --version #see the python version
touch runtime.txt
open runtime.txt
write python-3.6.2 #replace the version
touch Procfile
open Procfile
copy this line from website: https://github.com/datademofun/heroku-basic-flask
web: gunicorn app:app —log-file=-
touch .gitignore
open .gitignore
write
venv
__pycache__

5. create heroku
pip install heroku or pip install heroku --upgrade
heroku login
heroku create

6. git
git add .
git commit -m"first"
git push heroku master
git push
