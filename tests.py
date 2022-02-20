import unittest
from details.user import User
from details.credentials import Credentials


class UserTest(unittest.TestCase):
    '''
    user cases for user
    '''
    def setUp(self):
        '''
        run this before the test
        '''
        self.user = User('Toni','1234')
    def test_add_user(self):
        '''
        test case to check if user instance is similar

        '''
        self.assertEqual(self.user.user_name,'Toni')
        self.assertEqual(self.user.password,'1234')

    def test_save_user(self):
        '''
        Test case to check if the new instance of the user object has been recreated
        '''
        User.users_list = []
        
        self.user.save_this_user()
        self.assertEqual(len(User.users_list), 1)

    def tearDown(self):
        '''
        this method clean up after test has run
        '''
        User.users_list = []
    
class CredentialsTest(unittest.TestCase):

    def setUp(self):
            '''
            this method runs before the test
            '''
            self.credentials_list = Credentials('facebook', 'toni', 'pass')

    def test_create_credentials(self):
    
        self.assertEqual(self.credentials_list.user_account, 'facebook')
        self.assertEqual(self.credentials_list.user_name, 'toni')
        self.assertEqual(self.credentials_list.password, 'pass')

    def test_save_credentials(self):
        '''
        this test checks if saved credentials object are in our list
        '''
        Credentials.credentials_list = []
        self.credentials_list.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
    

    def test_delete_credentials(self):
        '''
        this method deletes credentials
        '''
        self.credentials_list.save_credentials()
        test_credentials = Credentials('twitter','anto','test')
        test_credentials.save_credentials()
        self.credentials_list.delete_credentials_account(test_credentials.user_account)
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials(self):
        self.credentials_list.save_credentials()
        test_credentials = Credentials('youtube','antony','test')
        test_credentials.save_credentials()
        found_credentials = Credentials.search_user_credentials('test')

    def tearDown(self):
        '''
        this method cleans up after test has run
        '''
        Credentials.credentials_list = []

 






if __name__ == '__main__':
    unittest.main()