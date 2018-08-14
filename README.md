# HabitBuilder
Web application created using Django and MySQL. 

HabitBuilder allows users to create an account and track the completion of their daily habits. Each habit displays the number of days in a row that it has been completed.

**To run on a local machine, have the latest versions of Python and MySQL installed.**

**Then execute the following commands while in the HabitBuilder directory:**

**Activate a virtualenvwrapper or a virtual environment of your choice:**
```
pip3 install virtualenvwrapper
mkvirtualenv HabitBuilderENV
workon HabitBuilderENV
```

**Install the necessary dependencies:**
```
pip3 install Django
pip3 install mysqlclient
```

**Create a new file named confidential.py in the habit_builder directory.**
**Add the following lines to confidential.py**
```
SECRET_KEY = {YOUR DJANGO SECRET_KEY HERE}
USER = {YOUR MYSQL USERNAME, i.e. root}
PASSWORD = {YOUR MYSQL PASSWORD}
ADMIN_URL = {PREFERRED URL FOR DJANGO ADMIN PAGE, i.e. 'admin/'}
```

**Create a new MySQL database named habitbuilderdb:**
```
CREATE DATABASE habitbuilderdb;
```

**Back in the HabitBuilder directory execute the following configuration commands:**
```
python manage.py collectstatic
python manage.py migrate
python manage.py loaddata day.json
```

**Run the server (default on localhost:8000)**
```
python manage.py runserver
```