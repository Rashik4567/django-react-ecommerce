import os
import platform

if platform.system().lower() == "windows":
    print(os.system("python manage.py runserver"))
else:
    print(os.system("python3 manage.py runserver"))