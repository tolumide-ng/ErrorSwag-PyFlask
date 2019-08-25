# import unittest
# import os
# import json
# from ..app import create_app, db
# from ..models.user_model import User
# from ..shared.Authentication import Auth


# class FollowTests(unittest.TestCase):
#     """
#     Follow Test Case
#     """

#     def setup(self):
#         """
#         Test Setup
#         """

#         self.app = create_app('testing')
#         self.client = self.app.test_client

#         with self.app.app_context():
#             # create akk tables
#             db.create_all()

#     def test_follow_user(self):
#         "test follow user"
#         # theuser = User.insert().values(
#         #     username='jack', email='Jack@Jones.com', password='Pass*word2010#')

#         newFollow = Follow (
#             username='jack', email='Jack@Jones.com', password='Pass*word2010#')


# dbsession.add(newToner)
# dbsession.flush()

#         print('yhhhhjjjp', theuser)
#         # token = Auth.generate_token(ser_data.get('id'))

#     def tearDown(self):
#         """
#         Tears Down
#         """
#         with self.app.app_context():
#             db.session.remove()
#             db.drop_all()


# if __name__ == '__main__':
#     unittest.main()
