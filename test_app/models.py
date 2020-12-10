from flask_login import UserMixin

from test_app import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'},
        )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=True)
    sex = db.Column(db.String(8))
    phone_num = db.Column(db.Integer)
    token = db.Column(db.String(128), nullable=True)
    login_time = db.Column(db.DATETIME)
    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


class Role():
    __tablename__ = 'role'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'},
        )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(128), nullable=True)
    role_level = db.Column(db.Integer, nullable=True)
    comments = db.Column(db.String, nullable=True)


class Permission():
    __tablename__ = 'permission'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'},
        )
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    permission_name = db.Column(db.String(128), nullable=True)
    permission_level = db.Column(db.Integer, nullable=True)
    comments = db.Column(db.String, nullable=True)


class PermissionRoleShip():
    __tablename__ = 'permission_role_ship'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'},
        )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'))


class Test(db.Model):
    __tablename__ = 'test'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'},
        )
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test_string = db.Column(db.String(128), nullable=True)