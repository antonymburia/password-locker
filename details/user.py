class User:
    '''
    This is a class to create instances of a user
    '''

    #empty users list
    users_list = []

    def __init__ (self, user_name, password):

        '''
        properties of user 

        args:
        user_name
        password
        '''
        self.user_name = user_name
        self.password = password

    def save_save_user(self):
        '''
        this method saves a user to the list
        '''
        User.users_list.append(self)
        
    