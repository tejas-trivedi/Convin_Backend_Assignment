# Convin_Backend_Assignment

### Steps to run the local server

- Create a virtual enviroment using command: `python -m venv env`
- Activate the enviroment using command: `env\Scripts\activate` (for Windows)
- Install all the dependencies inside the activated enviromnent using the command: `pip install -r requirements.txt`
- Run the migrations using command: `python manage.py makemigrations` and `python manage.py migrate`
- Run the server using the command: `python manage.py runserver`


Once the server is up and running, go to the required URL and signin with your google account. A response with a list of 5 upcoming events will be displayed. If there are none, then a suitable message is shown.
