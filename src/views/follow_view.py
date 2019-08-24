# /src/follow_view.py
from flask import request, g, Blueprint, json, Response
from marshmallow import ValidationError
from ..shared.Authentication import Auth
from ..models.follow_model import Follow, FollowSchema
from ..models.user_model import User

follow_api = Blueprint('follow_api', __name__)
follow_schema = FollowSchema()


@follow_api.route('/follow/<int:followee_id>', methods=['POST'])
@Auth.auth_required
def follow(followee_id):
    """
    Follow a User
    """
    # 404 Location does not exist
    # 400 in this case - Resource does not exist
    if followee_id == g.user['id']:
        return custom_response({'error': 'You cannot follow/unfollow yourself'}, 400)

    user_exist = User.get_one_user(followee_id)
    if not user_exist:
        return custom_response({'error': 'user does not exist'}, 400)

    confirm_follow = Follow.get_specific_follow(g.user.get('id'), followee_id)
    if confirm_follow and confirm_follow is not None:
        return custom_response({'message': 'You are already following this user'}, 400)
    try:
        req_data = {}
        req_data['follower_id'] = g.user['id']
        req_data['followee_id'] = followee_id
        data = follow_schema.load(req_data)
    except ValidationError as err:
        return custom_response(err.messages, 400)

    follow_user = Follow(data)
    follow_user.save()
    data = follow_schema.dump(follow_user)
    return custom_response(data, 201)


@follow_api.route('/unfollow/<int:followee_id>', methods=['DELETE'])
@Auth.auth_required
def unfollow(followee_id):
    """
    Unfollow a User
    """
    # follower_id
    if followee_id == g.user.get('id'):
        return custom_response({'error': 'You cannot follow/unfollow yourself'}, 400)

    user_exist = User.get_one_user(followee_id)
    if not user_exist:
        return custom_response({'error': 'user does not exist'}, 400)

    confirm_follow = Follow.get_specific_follow(g.user.get('id'), followee_id)
    print('this is the confirm p[oint ??>>>>>>>', confirm_follow)
    if confirm_follow is None:
        return custom_response({'error': 'You were not following this user'}, 400)

    confirm_follow.delete()
    return custom_response({'message': 'user unfollowed'}, 200)


@follow_api.route('/followers', methods=['GET'])
@Auth.auth_required
def followers():
    """
    Get all Followers
    """
    followers = Follow.get_all_followers(g.user['id'])
    if len(followers) < 1:
        return custom_response({'message': 'You do not have any followers at the moment'}, 200)

    data = follow_schema.dump(followers, many=True)
    return custom_response(data, 200)


@follow_api.route('/following', methods=['GET'])
@Auth.auth_required
def followees():
    """
    Get all followings
    """
    followings = Follow.get_all_followings(g.user['id'])
    if len(followings) < 1:
        return custom_response({'message': 'You are not following anyone at the moment'}, 200)

    data = follow_schema.dump(followings, many=True)
    return custom_response(data, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
