from details.user import User
from details.credentials import Credentials

def create_new_user(user_name, password):
    '''
    this function creates a new user instance
    '''
    new_user = User(user_name, password)

    return new_user

def save_new_user(user):
    user.save_user

def show_user(user):
    '''
    this function displays a user
    '''
    user.show_user()

def acc_login(user_name, password):
    '''
    this function validates user login by calling the validate function in the credentials class
    '''
    validated_user = Credentials.validate_user(user_name, password)
    return validated_user

def create_credentials(user_account,user_name, password):
    '''
    create a credentials user account
    '''
    new_credentials = Credentials(user_account, user_name,password)
    return new_credentials

def save_credentials(credentials_list):
    Credentials.save_credentials(credentials_list)

def delete_credentials(credentials_account):
    Credentials.delete_credentials_account(credentials_account)

def search_credentials(user_account):
    return Credentials.search_user_credentials(user_account)

def list_credentials():
    return Credentials.display_credentials()

def generate_pass():
    auto_gen_password = Credentials.generate_password()
    return auto_gen_password
    