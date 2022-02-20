from .user import User
import string

class Credentials:
    '''
    add credentials to the credentials list
    '''
    credentials_list = []

    def __init__ (self, user_account, user_name, password):
        '''
        properties of credentials

        args:
        user_account
        user_name
        password

        '''
        self.user_account = user_account
        self.user_name = user_name
        self.password = password


    @classmethod
    def validate_user(cls, user_name, password):
        validate_user = ''
        for user in User.users_list:
            if user.user_name == user_name and user.password == password:
                validate_user = user.user_name
                return validate_user
    
    
    def save_credentials(self):
        Credentials.credentials_list.append(self)

    