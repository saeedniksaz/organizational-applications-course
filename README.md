
# Install Django project in your localhost

1) make directory on your laptop
2) open cmd(or terminal on Linux) and change the path to directory you made above
3) type command: git clone https://github.com/saeedniksaz/organizational-applications-course.git
4) type command: cd organizational-applications-course
5) type command: pip install -r requirements.txt
6) type command: python manage.py makemigrations 
7) type command: python manage.py migrate
8) type command: python manage.py createsuperuser 
9) insert username, email and passwor
10) python manage.py runserver