# src/models/Follow.py

from . import db
import datetime
from marshmallow import fields, Schema


class Follow(db.Model):
    """
    Follow Model
    """

    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    followee_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, data):
        self.follower_id = data.get('follower_id')
        self.followee_id = data.get('followee_id')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_followings(follower_id):
        return Follow.query.get(follower_id)

    @staticmethod
    def get_all_followers(followee_id):
        return Follow.query.get(followee_id)

    @staticmethod
    def get_one_follow(id):
        return Follow.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

    class FollowSchema(Schema):
        """
        Follow Schema
        """
        id = fields.Int(dump_only=True)
        followee_id = fields.Int(required=True)
        follower_id = fields.Int(required=True)
