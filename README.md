# WorkConnect
creating virtual environment
-python -m venv env

Activate virtual environment
-source env/Scripts/activate

#Add .gitignore file
Create a .gitignore file in the project root and add the relative path of the virtual environment so it is not tracked by Git:

#install django: pip install Django


#Create the Django Project

Use the Django CLI to create a new project:

-django-admin startproject WorkConnect

This generates a new folder named WorkConnect containing the main project files.
Creating Django Applications
--python manage.py startapp