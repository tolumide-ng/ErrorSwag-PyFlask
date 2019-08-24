# src/views/user_view

from flask import request, json, Response, Blueprint, g
from marshmallow import ValidationError
from ..models.user_model import User, UserSchema
from ..shared.Authentication import Auth


user_api = Blueprint('user_api', __name__)
user_schema = UserSchema()


@user_api.route('/', methods=['POST'])
def create():
    """
    Create User Function
    """
    try:
        req_data = request.get_json()
        data = user_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err.messages, 400)

        # check if user already exist in the db
    user_in_db = User.get_user_by_email(data.get('email'))
    if user_in_db:
        message = {
            'error': 'User already exists, please supply another email address'}
        return custom_response(message, 400)

    user = User(data)
    user.save()

    ser_data = user_schema.dump(user)

    token = Auth.generate_token(ser_data.get('id'))

    return custom_response({'jwt_token': token}, 201)


@user_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
    users = User.get_all_users()
    ser_users = user_schema.dump(users, many=True)
    return custom_response(ser_users, 200)


@user_api.route('/login', methods=['POST'])
def login():
    try:
        req_data = request.get_json()
        data = user_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err.messages, 400)

    if not data.get('email') or not data.get('password'):
        return custom_response({'error': 'you need email and password to sign in'}, 400)

    user = User.get_user_by_email(data.get('email'))

    if not user:
        return custom_response({'error': 'invalid credentials'}, 400)

    if not user.check_hash(data.get('password')):
        return custom_response({'error': 'invalid credentials'}, 400)

    ser_data = user_schema.dump(user)

    token = Auth.generate_token(ser_data.get('id'))

    return custom_response({'jwt_token': token}, 200)


@user_api.route('/<int:user_id>', methods=['GET'])
@Auth.auth_required
def get_a_user(user_id):
    """
    Get a single user
    """
    user = User.get_one_user(user_id)
    if not user:
        return custom_response({'error': 'user not found'}, 404)

    ser_user = user_schema.dump(user)
    return custom_response(ser_user, 200)


@user_api.route('/me', methods=['PUT'])
@Auth.auth_required
def update():
    """
    Update my profile
    """
    try:
        req_data = request.get_json()
        # if req_data['email'] == None:
        #     return custom_response({'error': 'You can only update username and password'}, 403)
        data = user_schema.load(req_data, partial=True)
    except ValidationError as err:
        return custom_response(err.messages, 400)

    user = User.get_one_user(g.user.get('id'))
    user.update(data)
    ser_user = update_schema.dump(user)
    return custom_response(ser_user, 200)


@user_api.route('/me', methods=['DELETE'])
@Auth.auth_required
def delete():
    """
    Delete my account
    """
    user = User.get_one_user(g.user.get('id'))
    # if g.user.get('admin') == True:
    user.delete()
    return custom_response({'message': 'deleted'}, 204)
    # else:
    # return custom_response({'message': 'You do not have permission to delete users'}, 403)


@user_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
    """
    Get me
    """
    user = User.get_one_user(g.user.get('id'))
    ser_user = user_schema.dump(user)
    return custom_response(ser_user, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
