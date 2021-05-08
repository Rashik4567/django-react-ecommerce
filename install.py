import platform
import os
import migrate

def install_win():
    os.system("python -m ensurepip & pip install -r requirements.txt")
    os.system("cd frontend && npm i && npm run build")
    migrate.database_sqlite3()
    print("Installation is done! You can start the server by using command 'python .'")

def install_mac():
    os.system("python3 -m ensurepip ; pip3 install -r requirements.txt")
    os.system("cd frontend && npm i && npm run build")
    migrate.database_sqlite3()
    print("Installation is done! You can start the server by using command 'python3 .'")

def install_linux():
    os.system("python3 -m ensurepip ; pip3 install -r requirements.txt")
    os.system("cd frontend && npm i && npm run build")
    migrate.database_sqlite3()
    print("Installation is done! You can start the server by using command 'python3 .'")

def install():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    print("This project is made under GNU General Public License v3.0")
    print("\n")
    print("You may use this project in any Commercial, Patent, Private usage. Please check the LICENSE file for more details.")
    print("\n")
    i_confirmation = input("Do you want to install this project in your current directory? [Default is yes, Y/N] >")
    if (i_confirmation.lower() == 'y') or (i_confirmation.lower() == "yes") or (i_confirmation == ""):
        if platform.system().lower() == "darwin":
            install_mac()
        elif platform.system().lower() == "windows":
            install_win()
        else:
            install_linux()



    else:
        print("If you want to install, run this file again.")
        quit()
