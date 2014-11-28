from hashlib import md5
from flask.ext.security import UserMixin

from aikithoughts.models.authentications import role_assignments
from aikithoughts.runtime import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    created_at = db.Column(db.DateTime())

    roles = db.relationship(
        'Role',
        secondary=role_assignments,
        backref=db.backref('users', lazy='dynamic')
    )
    posts = db.relationship(
        'Post',
        backref='author', lazy='dynamic'
    )

    def __repr__(self):
        return '<User %r: %r (%s)>' % (self.id, self.nickname, self.email)

    def avatar(self, size=16):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % (
            md5(self.email.encode('utf-8')).hexdigest(), size
        )
