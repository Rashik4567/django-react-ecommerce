import platform
import os

def database_sqlite3():
    if platform.system().lower() == "windows":
        os.system("python manage.py makemigrations && python manage.py migrate")
    else:
        os.system("python3 manage.py makemigrations && python3 manage.py migrate")
