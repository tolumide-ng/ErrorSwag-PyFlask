# src/models/Follow.py

from . import db
import datetime
from marshmallow import fields, Schema
from sqlalchemy.orm import subqueryload


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
    def get_specific_follow(follower_id, followee_id):
        return Follow.query.filter_by(follower_id=follower_id, followee_id=followee_id).first()

    @staticmethod
    def get_all_followers(id):
        return Follow.query.filter_by(followee_id=id).all()

    @staticmethod
    def get_all_followings(id):
        return Follow.query.filter_by(follower_id=id).all()

    def __repr__(self):
        return '<id {}>'.format(self.id)


class FollowSchema(Schema):
    """
    Follow Schema
    """
    id = fields.Int(dump_only=True)
    followee_id = fields.Int(required=True)
    follower_id = fields.Int(required=True)
