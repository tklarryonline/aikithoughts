from flask.ext.security import UserMixin
from aikithoughts.models.authentications import auth_assignments

from aikithoughts.runtime import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    created_at = db.Column(db.DateTime())

    roles = db.relationship('Role',
                            secondary=auth_assignments,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r: %r>' % (self.id, self.nickname)
