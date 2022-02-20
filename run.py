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

def password_lock():
    output = '''
    Welcome to Pass Lock \n
    Select an option below \n
    Enter 1 to create a pass Lock account \n
    Enter 2 if you already have an existing account \n
    '''

    user_input =input(output).lower().strip()
    print(user_input)

    if user_input ==  '1':
        print('enter your details below to create a new account')
        user_name = ('enter prefered user_name ')

        while True:
            pass_input = '''
            press 1 to create a password for the account \n
            press 2 to auto-generate a password \n
            '''
            response = input(pass_input).lower().strip()
            if response =='1':
                password = input('Create your pasword:')
            elif response  == '2':
                password = generate_pass()
                break
            else:
                print("password can't be empty")
            
            save_new_user(create_new_user(user_name, password))
            print(f"Hi {user_name} you account is ready use thispassword:  {password} to login")
        
    elif user_input == 2:
        print('Enter your details to login')
        