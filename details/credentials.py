from .user import User
import string
import random

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

    @classmethod 

    def search_user_credentials(cls, user_account):

        '''
        this method searches users credentials
        '''
        
        for credential in cls.credentials_list:
            if credential.user_account == user_account:
                return credential
    
    @classmethod
    def show_credentials(cls):

        '''
        function displays user credentials
        '''


        return cls.credentials_list

    @classmethod
    
    def check_credentials_existence(cls, user_account):
        '''
        check credentials existence in the list
        '''

        for credentials_list in cls.credentials_list:
            if credentials_list.user_account == user_account:
                return True
            return False
    
    @classmethod
    def delete_credentials_account(cls, user_account):
        '''
        delete a credentials account
        '''
        
        for credentials_list in cls.credentials_list:
            if credentials_list.user_account == user_account:
                cls.credentials_list.remove(credentials_list)
                return cls.credentials_list
    
    
    def generate_password(length=6):
        '''
        generate random password
        '''
        
        password = string.ascii_lowercase + string.digits + string.ascii_uppercase + "'@#!&*$`"
        return ''.join(random.choice(password) for _ in range(length))