# /src/blog_view.py
from flask import request, g, Blueprint, json, Response
from marshmallow import ValidationError
from ..shared.Authentication import Auth
from ..models.blog_model import Blog, BlogSchema

blog_api = Blueprint('blog_api', __name__)
blog_schema = BlogSchema()


@blog_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    """
    Create Blog Function
    """

    try:
        req_data = request.get_json()
        req_data['author_id'] = g.user['id']
        data = blog_schema.load(req_data)
    except ValidationError as err:

        return custom_response(err.messages, 400)
    post = Blog(data)
    post.save()
    data = blog_schema.dump(post)
    return custom_response(data, 201)


@blog_api.route('/', methods=['GET'])
def get_all():
    """
    Get all Blogs
    """
    posts = Blog.get_all_blogs()
    print('this is a record of all the posts>>>>>>', len(posts))
    if len(posts) < 1:
        return custom_response({"message": "There are currently no blogpost"}, 200)

    data = blog_schema.dump(posts, many=True)
    return custom_response(data, 200)


@blog_api.route('<int:blog_id>', methods=['GET'])
def get_one(blog_id):
    """
    Get a specific blog
    """
    post = Blog.get_one_blog(blog_id)
    if not post:
        # 400 Resource not found
        # 404 Location not found
        return custom_response({'error': 'post not found'}, 400)
    data = blog_schema.dump(post)
    return custom_response(data, 200)


@blog_api.route('/<int:blog_id>', methods=['PUT'])
@Auth.auth_required
def update(blog_id):
    """
    Update a specific Blog
    """
    try:
        req_data = request.get_json()
        post = Blog.get_one_blog(blog_id)
        if not post:
            return custom_response({'error': 'post not found'}, 404)
        data = blog_schema.dump(post)
        if data.get('author_id') != g.user.get('id'):
            return custom_response({'error': 'permission denied'}, 400)

        data = blog_schema.load(req_data, partial=True)
    except ValidationError as err:
        return custom_response(err, 400)

    post.update(data)
    data = blog_schema.dump(post)
    return custom_response(data, 200)


@blog_api.route('/<int:blog_id>', methods=['DELETE'])
@Auth.auth_required
def delete(blog_id):
    """
    Delete a specific blog
    """
    post = Blog.get_one_blog(blog_id)
    if not post:
        # 400 Resource not found
        # 404 Location not found
        return custom_response({'error': 'post not found'}, 400)
    data = blog_schema.dump(post)
    if data.get('author_id') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    post.delete()
    return custom_response({'message': 'deleted'}, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
