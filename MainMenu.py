from Settings import Login

user_login = Login.Login()

def main_menu():
    print("What would you like to do?")
    print("1. Update password.")
    print("2. Exit")
    choice = int(input("Choice: "))
    if choice == 2:
        exit()
    if choice == 1:
        user_login.update_passwd()