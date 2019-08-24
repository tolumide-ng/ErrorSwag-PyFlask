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


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
