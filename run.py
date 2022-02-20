from details.user import User
from details.credentials import Credentials
import sys

def create_new_user(user_name, password):
    '''
    this function creates a new user instance
    '''
    new_user = User(user_name, password)

    return new_user

def save_new_user(user):
    user.save_this_user

def show_user(user):
    '''
    this function displays a user
    '''
    user.show_user()

def acc_login(user_name, password):
    '''
    this function validates user login by calling the validate function in the credentials class
    '''
    return User.validate_user(user_name, password)
    # validated_user = Credentials.validate_user(user_name, password)
    # return validated_user
    # return Credentials.search_user_credentials(credentials_list)

def create_credentials(user_account,user_name, password):
    '''
    create a credentials user account
    '''
    new_credentials = Credentials(user_account, user_name,password)
    return new_credentials

def save_credentials(credentials_list):
    Credentials.save_credentials(credentials_list)

def delete_credentials(credentials_list):
    Credentials.delete_credentials_account(credentials_list)

def search_credentials(credentials_list):
    return Credentials.search_user_credentials(credentials_list)

def list_credentials():
    return Credentials.show_credentials()

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
        user_name = input('enter prefered user_name ')

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
                
            else:
                print("password can't be empty")
            
            save_new_user(create_new_user(user_name, password))
            print(f"Hi {user_name} you account is ready use thispassword:  {password} to login")
            break
        
    elif user_input == '2':
        print('Enter your details to login')
        user_name = input('enter your user name')
        password = input('Input your password')

        if acc_login(user_name, password):
            acc = acc_login(user_name, password)
            print('welcome {acc.user_name} login was successful')

        # validated_user = acc_login(user_name,password)
        # if validated_user == acc_login(user_name, password):
        #     print('Hi {user_name} login was succesful')
        else:
            print('enter correct details and ensure you have an account')
            sys.exit("create an account and try again")

    while True:
        success_login = '''
        Enter 1 to create new credentials \n
        Enter 2 to display credentials \n
        Enter 3 to delete your credentials \n
        Enter 4 to search credentials \n
        '''
        logged_in = input(success_login).lower().strip()
        if logged_in == "1":
            print("Enter your  info to create a new credentials")
            user_account = input("Enter your account name: ")
            user_name = input("Enter your username: ")
            password_message = """
            Enter 1 to create a password for the account\n
            Enter 2  to generate password\n
            """
            this_response = input(password_message).lower().strip()
            if this_response == "1":
                password = input("Enter your password: ")
                print(f'Your credentials for {user_account} has been created')
            elif this_response == "2":
                password = generate_pass()
            save_credentials(create_credentials(user_account, user_name, password))
            print(f'Credentials for {user_account} created')

        elif logged_in == "4":
            print("Enter your credentials to search ")
            user_account = input("Enter your account name: ")
            if search_credentials(user_account):
                search_result = search_credentials(user_account)
                print(f'name : {search_result.user_name} password : {search_result.password}')
                print('-' * 50)
            else:
                print('the account is non existent \n')
            
                
        elif logged_in == "2":
            if list_credentials():
                print("Nice! Let's display credentials\n")
                print("Here's a list of all your credentials\n")
                for credential_list in list_credentials():
                    print(f'Account: {credential_list.user_account}\nUsername: {credential_list.user_name}\nPassword: {credential_list.password} \n')
            else:
                print("You don't have any credentials saved yet")
        elif logged_in== "3":
            print("Great! Let's delete credentials")
            user_account = input("Enter your account name: ")
            delete_credentials(user_account)


if __name__ == '__main__':
    password_lock()        