from details.user import User
from details.credentials import Credentials

def create_user(user_name, password):
    '''
    this function creates a new user instance
    '''
    new_user = User(user_name, password)

    return new_user

