# src/views/UserView

from flask import request, json, Response, Blueprint
from ..models.user_model import User, UserSchema
from ..shared.Authentication import Auth


user_api = Blueprint('users', __name__)
user_schema = UserSchema()


@user_api.route('/', methods=['POST'])
def create():
    """
    Create User Function
    """
    req_data = request.get_json()
    data, error = user_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    # check if user already exist in the db
    user_in_db = User.get_user_by_
