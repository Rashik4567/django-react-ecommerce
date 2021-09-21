import os
import platform

# this can run programme in parallal
''' ~~linux~~
some_command &
P1=$!
other_command &
P2=$!
wait $P1 $P2~

~~windows~~ 
(adding /b will stop creating new window of cmd.)
start "" first_comamnd
start "" second_command
'''

if platform.system().lower() == "windows":
    print(os.system('''start "backend" python manage.py runserver && cd frontend && start "frontend" npm start'''))
else:
    print(os.system("python3 manage.py runserver & P1=$! (cd frontend && npm start) & P2=$! wait $P1 $P2"))