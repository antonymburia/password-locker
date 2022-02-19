import unittest
from details.user import User


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

 






if __name__ == '__main__':
    unittest.main()