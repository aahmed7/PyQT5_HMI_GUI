from passlib.hash import pbkdf2_sha256
import stdiomask


class Login:
    """This class contains methods for directly interacting with the sensors.

    Attributes:
        login: login status
    """

    def set_passwd_hash(self, new_hash):
        '''
        Set hash for new user password.

            Parameters:
                    new_hash: hash for new user password.

            Returns:
                    none.
        '''
        with open("userpasswd", "w") as myfile:
            return myfile.write(new_hash)

    def set_adm_passwd_hash(self, new_hash):
        '''
        Set hash for new admin password.

            Parameters:
                    new_hash: hash for new admin password.

            Returns:
                    none.
        '''
        with open("adminpasswd", "w") as myfile:
            return myfile.write(new_hash)

    def get_passwd_hash(self):
        '''
        Get hash for new user password.

            Parameters:
                    none.

            Returns:
                    hash for user password.
        '''
        try:
            with open("userpasswd", "r") as myfile:
                return myfile.read()
        except:
            # Generate default password "1234"
            hash = '$pbkdf2-sha256$29000$MSYkJESodY5xjjEm5HyPcQ$cakngrW5RkHhaIQAvzLPmtJeH8PvuQ7Ac4pQmqZueoQ'
            self.set_passwd_hash(hash)
            return hash

    def get_adm_passwd_hash(self):
        '''
        Get hash for new admin password.

            Parameters:
                    none.

            Returns:
                    hash for admin password.
        '''
        try:
            with open("adminpasswd", "r") as myfile:
                return myfile.read()
        except:
            # Generate default password "1234"
            hash = '$pbkdf2-sha256$29000$MSYkJESodY5xjjEm5HyPcQ$cakngrW5RkHhaIQAvzLPmtJeH8PvuQ7Ac4pQmqZueoQ'
            self.set_passwd_hash(hash)
            return hash

    def update_passwd(self):
        '''
        Wrapper for updating password.

            Parameters:
                    none.

            Returns:
                    New password hash.
        '''
        new_passwd = input("Enter new password: ")
        hash = pbkdf2_sha256.hash(new_passwd)
        self.set_passwd_hash(hash)

    def check_login_user(self):
        '''
        Login for user. Doesn't use a database. Username is user, and 
        password is stored in a hash file.

            Parameters:
                    none.

            Returns:
                    bool: login success or fail
        '''
        passwd_hash = self.get_passwd_hash()
        username = input("Username: ")
        password = stdiomask.getpass(prompt="Password: ")
        try:
            assert username == "user"
            try:
                assert pbkdf2_sha256.verify(password, passwd_hash)
                print("Login successful.")
                return True
            except:
                print("Wrong Password.")
                return False
        except:
            print("Unknown user.")
            return False

    def check_login_password(self, passwd):
        '''
        Compare user password with hash

            Parameters:
                    none.

            Returns:
                    bool: password correct or not
        '''
        passwd_hash = self.get_passwd_hash()
        try:
            assert pbkdf2_sha256.verify(passwd, passwd_hash)
            print("Login successful.")
            return True
        except:
            print("Wrong Password.")
            return False


user_login = Login()
