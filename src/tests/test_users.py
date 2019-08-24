import unittest
import os
import json
from ..app import create_app, db


class UsersTests(unittest.TestCase):
    """
    Users Tests Case
    """

    def setUp(self):
        """
        Test Setup
        """
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.user = {
            'username': 'eleniyan',
            'email': 'michael@email.com',
            'password': 'Passwoprd2019#'
        }

        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_user_creation(self):
        """test vali user credentials"""
        res = self.client().post('/api/v1/users/',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
        json_data = json.loads(res.data)
        self.assertTrue(json_data.get('jwt_token'))
        self.assertEqual(res.status_code, 201)

    def test_user_creation_with_existing_email(self):
        """test user creation with existing email"""
        res = self.client().post('/api/v1/users/',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        res = self.client().post('/api/v1/users/',
                                 headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertTrue(json_data.get('error'))

    def tearDown(self):
        """
        Tear Down
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
