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
        '''
        check whether a user exists
        '''
        validate_user = ''
        for user in User.users_list:
            if user.user_name == user_name and user.password == password:
                validate_user = user.user_name
                return validate_user
    
    
    def save_credentials(self):
        '''
        add new credential to credentials_list
        '''
        Credentials.credentials_list.append(self)

    def search_user_credentials(cls, account):
        '''
        this method searches users credentials
        '''
    
    def display_credentials(cls):
        '''
        function displays user credentials
        '''
        return cls.credentials_list
    
    def check_credentials_existence(cls, account):
        '''
        check credentials existence in the list
        '''
        for credentials_list in cls.credentials_list:
            if credentials_list.account == account:
                return True
            return False
    
    def delete_credentials_account(cls, account):
        for credentials_list in cls.credentials_list:
            if credentials_list.account == account:
                cls.credentials_list.remove(account)
                return cls.credentials_list
    
    