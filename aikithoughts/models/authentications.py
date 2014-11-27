from flask.ext.security import RoleMixin

from aikithoughts.runtime import db


class AuthRole(db.Model, RoleMixin):
    __tablename__ = 'auth_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


''' Helper table to use with user-role relationship '''
auth_assignments = db.Table(
    'auth_assignment',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('auth_role_id', db.Integer, db.ForeignKey('auth_role.id'))
)
