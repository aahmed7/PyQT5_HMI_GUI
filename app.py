from Settings import Login
import MainMenu

# sensors = Sensors()
# actuators = Actuators()

user_login = Login.Login()

if __name__ == "__main__":
    # Get User Login. Exit if invalid
    login_success = user_login.check_login_user()
    if login_success != True:
        print("Login Failed. Exiting.")
        exit()

    # Display the main menu.
    MainMenu.main_menu()